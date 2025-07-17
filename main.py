from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime

import pandas as pd

from config import biller_engine, jano_engine, OUTPUT_DIR, START_DATE, END_DATE, STORES, REPORT_NAME, log_console_level, log_file_level
from config.logger_config import setup_logger
from models import QUERY_FCT, QUERY_JAN
from utils.checker import check_all_databases
from utils.finder import sql_executor, data_frame_slicer, identifier, row_empty, \
    dtype_to_str, differential_matching, calculate_date_range, find_biller_pair, find_jano_pair


logger = setup_logger(__name__, console_level=log_console_level, file_level=log_file_level)


def main() -> None:
    try:
        # Comprobar que las bases de datos estén disponibles antes de la ejecución
        logger.info("Comprobando las bases de datos disponibles")
        if all(check_all_databases().values()):
            logger.info("Se han encontrado todas las bases de datos disponibles")
            logger.info("Lanzando consultas sobre las bases de datos, en paralelo. Esto puede tardar unos minutos...")
            with ThreadPoolExecutor(max_workers=2) as executor:
                fct_thread = executor.submit(sql_executor, QUERY_FCT.format_map(
                    {'start_date': START_DATE, 'end_date': END_DATE, 'stores': STORES}), biller_engine)
                jan_thread = executor.submit(sql_executor, QUERY_JAN.format_map(
                    {'start_date': START_DATE, 'end_date': END_DATE, 'stores': STORES}), jano_engine)

                fct_df = fct_thread.result()
                jan_df = jan_thread.result()
                logger.info("Se han creado los DataFrame: 'fct_df' y 'jan_df'.")

            jan_df.columns = [attribute.lower() for attribute in jan_df.columns]

            logger.info("Creando el campo 'pair_up' para emparejar ambos DataFrames.")
            fct_df['trx_fct'] = fct_df['trx_fct'].apply(lambda x: x.zfill(5))
            fct_df['pair_up'] = fct_df['factura_fct'] + fct_df['trx_fct']
            jan_df['trx_jan'] = jan_df['trx_jan'].apply(lambda x: x.zfill(5))
            jan_df['pair_up'] = jan_df['factura_jan'] + jan_df['trx_jan']

            logger.info("Usando la funcionalidad `differential_matching()` para emparejar los DataFrames 'jan_df' y 'fct_df'.")
            pair_up_df, jan_df, fct_df = differential_matching(jan_df, fct_df)

            logger.info("Eliminando la columna 'pair_up' de los DataFrames")
            pair_up_df = pair_up_df.drop(['pair_up'], axis=1)
            jan_df = jan_df.drop(['pair_up'], axis=1)
            fct_df = fct_df.drop(['pair_up'], axis=1)

            logger.info("Aplicando segúnda lógica para crear el campo 'pair_up', usado para emparejar los DataFrames 'jan_df' y 'fct_df'.")
            jan_df['pair_up'] = jan_df.apply(
                lambda x: identifier(str(x['line_jan']), str(x['tienda_jan']), str(x['caja_jan']), str(x['trx_jan']),
                                     str(x['fecha_cierre'])),
                axis=1
            )
            fct_df['pair_up'] = fct_df.apply(
                lambda x: identifier(str(x['line_fct']), str(x['tienda_fct']), str(x['caja_fct']), str(x['trx_fct']),
                                     str(x['fecha_fct'])),
                axis=1
            )

            logger.info("Volviendo a emparejar los DataFrames 'jan_df' y 'fct_df'. Esto puede tardar unos minutos...")
            pair_up_2_df, jan_df, fct_df = differential_matching(jan_df, fct_df)

            logger.info("Volviendo a eliminar la columna 'pair_up' de los DataFrames")
            pair_up_2_df = pair_up_2_df.drop(['pair_up'], axis=1)
            jan_df = jan_df.drop(['pair_up'], axis=1)
            fct_df = fct_df.drop(['pair_up'], axis=1)

            logger.info("Usando la funcionalidad `dtype_to_str()` para convertir los tipos de datos de los DataFrames a 'str'.")
            fct_df = dtype_to_str(fct_df)
            jan_df = dtype_to_str(jan_df)

            new_set = set()

            logger.info(
                "Se emplea como método recorrer el DataFrame 'jan_df' para hallar pareja sobre 'fct_df'. "
                "Esto puede tardar unos minutos..."
            )
            for _, _row in jan_df.iterrows():
                _re = row_empty()
                _re.update(_row.to_dict())
                dates = calculate_date_range(datetime.strptime(_row['fecha_cierre'], '%Y-%m-%d'), 1)
                pair = fct_df[
                    (fct_df['tienda_fct'] == _row['tienda_jan']) &
                    (fct_df['caja_fct'] == _row['caja_jan']) &
                    (fct_df['trx_fct'] == _row['trx_jan']) &
                    (fct_df['fecha_fct'] >= dates[0]) &
                    (fct_df['fecha_fct'] <= dates[1])
                    ]
                if not pair.empty:
                    _re.update(pair.iloc[0].to_dict())
                else:
                    dates = calculate_date_range(datetime.strptime(_row['fecha_ini'], '%Y-%m-%d'), 1)
                    pair = fct_df[
                        (fct_df['tienda_fct'] == _row['tienda_jan']) &
                        (fct_df['caja_fct'] == _row['caja_jan']) &
                        (fct_df['trx_fct'] == _row['trx_jan']) &
                        (fct_df['fecha_fct'] >= dates[0]) &
                        (fct_df['fecha_fct'] <= dates[1])
                        ]
                    if not pair.empty:
                        _re.update(pair.iloc[0].to_dict())
                    else:
                        dates = calculate_date_range(datetime.strptime(_row['fecha_fin'], '%Y-%m-%d'), 1)
                        pair = fct_df[
                            (fct_df['tienda_fct'] == _row['tienda_jan']) &
                            (fct_df['caja_fct'] == _row['caja_jan']) &
                            (fct_df['trx_fct'] == _row['trx_jan']) &
                            (fct_df['fecha_fct'] >= dates[0]) &
                            (fct_df['fecha_fct'] <= dates[1])
                            ]
                        if not pair.empty:
                            _re.update(pair.iloc[0].to_dict())

                new_set.add(tuple(_re.items()))

            logger.info(
                "Se emplea como método recorrer el DataFrame 'fct_df' para hallar pareja sobre 'jan_df'. "
                "Esto puede tardar unos minutos..."
            )
            for _, _row in fct_df.iterrows():
                _re = row_empty()
                _re.update(_row.to_dict())
                dates = calculate_date_range(datetime.strptime(_row['fecha_fct'], '%Y-%m-%d'), 1)
                pair = jan_df[
                    (jan_df['tienda_jan'] == _row['tienda_fct']) &
                    (jan_df['caja_jan'] == _row['caja_fct']) &
                    (jan_df['trx_jan'] == _row['trx_fct']) &
                    (jan_df['fecha_cierre'] >= dates[0]) &
                    (jan_df['fecha_cierre'] <= dates[1])
                    ]
                if not pair.empty:
                    _re.update(pair.iloc[0].to_dict())
                else:
                    pair = jan_df[
                        (jan_df['tienda_jan'] == _row['tienda_fct']) &
                        (jan_df['caja_jan'] == _row['caja_fct']) &
                        (jan_df['trx_jan'] == _row['trx_fct']) &
                        (jan_df['fecha_ini'] >= dates[0]) &
                        (jan_df['fecha_ini'] <= dates[1])
                        ]
                    if not pair.empty:
                        _re.update(pair.iloc[0].to_dict())
                    else:
                        pair = jan_df[
                            (jan_df['tienda_jan'] == _row['tienda_fct']) &
                            (jan_df['caja_jan'] == _row['caja_fct']) &
                            (jan_df['trx_jan'] == _row['trx_fct']) &
                            (jan_df['fecha_fin'] >= dates[0]) &
                            (jan_df['fecha_fin'] <= dates[1])
                            ]
                        if not pair.empty:
                            _re.update(pair.iloc[0].to_dict())

                new_set.add(tuple(_re.items()))

            logger.info("Se crea un DataFrame 'pair_up_3_df' con el resultado de los métodos anteriores.")
            pair_up_3_df = pd.DataFrame([dict(i) for i in new_set], dtype=str)

            logger.info("Se emplea la funcionalidad `data_frame_slicer`, para separar registros no emparejados de los emparejados.")
            pair_up_3_df, jan_df, fct_df = data_frame_slicer(pair_up_3_df)

            #  Como del Facturador hacia Jano. Dos hilos que contengan 5 hilos, en total 10 hilos.
            logger.info(
                f"Inicia búsqueda para {len(jan_df)} documentos del DataFrame 'jan_df' en el Facturador. "
                "Esto puede tardar unos minutos..."
            )
            jan_df = find_biller_pair(jan_df)


            logger.info(
                f"Inicia búsqueda para {len(fct_df)} documentos del DataFrame 'fct_df' en Jano. "
                "Esto puede tardar unos minutos..."
            )
            fct_df = find_jano_pair(fct_df)
            

            pair_up_df = pd.concat([pair_up_df, pair_up_2_df, pair_up_3_df, jan_df, fct_df], axis=0)
            logger.info("Se concatenan todos los DataFrames para formar el DataFrame 'pair_up_df'.")

            del jan_df
            del fct_df
            del new_set
            del pair_up_2_df
            del pair_up_3_df
            logger.info("Se eliminan objetos innecesarios.")

            logger.info("Se vuelve a emplear la funcionalidad `dtype_to_str()` para convertir los tipos de datos del DataFrame 'pair_up_df' a 'str'.")
            pair_up_df = dtype_to_str(pair_up_df)

            logger.info("Agrega el campo 'tienda' al DataFrame 'pair_up_df'.")
            pair_up_df['tienda'] = pair_up_df.apply(
                lambda x: x['tienda_desc_jan'] if x['tienda_desc_jan'] else x['tienda_desc_fct'],
                axis=1
            )
            logger.info("Agrega el campo 'fecha' al DataFrame 'pair_up_df'.")
            pair_up_df['fecha'] = pair_up_df.apply(
                lambda x: x['fecha_cierre'] if x['fecha_cierre'] else x['fecha_fct'],
                axis=1
            )

            file_name = f"{REPORT_NAME}_{START_DATE}_{END_DATE}_{datetime.today().strftime('%Y%m%d%H%M%S')}"
            pair_up_df.to_csv(
                rf"{OUTPUT_DIR}/{file_name}.zip",
                index=False,
                sep=';',
                encoding='utf-8',
                compression={
                    'method': 'zip',
                    'archive_name': f"{file_name}.csv"
                }
            )
            logger.info(f"Guarda el resultado del proceso en el archivo {file_name}.zip")

            del pair_up_df
        else:
            logger.error("No se pudo ejecutar el programa porque no se encuentran las bases de datos disponibles.")
    except Exception as e:
        logger.error(f"Error en la ejecución del programa: {e}")


if __name__ == '__main__':
    main()
