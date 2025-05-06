from typing import Tuple, Optional
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
import re

from sqlalchemy import create_engine
import pandas as pd
from pandas.errors import MergeError


from config import engine_fct, calculate_date_range
from models import PAIR_EDOC_FCT_SQL, PAIR_SPTD_FCT_SQL


def row_empty() -> dict:
    return {
    "id_tra": None,
    "tipo_tr": None,
    "estado": None,
    "prefijo_jan": None,
    "consecutivo_jan": None,
    "factura_jan": None,
    "line_jan": None,
    "tienda_desc_jan": None,
    "tienda_jan": None,
    "caja_jan": None,
    "trx_jan": None,
    "fecha_cierre": None,
    "fecha_ini": None,
    "fecha_fin": None,
    "valor_jan": None,
    "cliente_jan": None,
    "tipo_identificacion": None,
    "canal": None,
    "id_fct": None,
    "c_origen": None,
    "prefijo_fct": None,
    "consecutivo_fct": None,
    "factura_fct": None,
    "nro_factura_afec": None,
    "line_fct": None,
    "tienda_desc_fct": None,
    "tienda_fct": None,
    "caja_fct": None,
    "trx_fct": None,
    "fecha_fct": None,
    "mes": None,
    "valor_fct": None,
    "cliente_fct": None,
    "duplicada": None,
    "f_envio_dian": None,
    "estado_dian": None,
    "log_errores_dian": None,
    "cufe": None,
}


def sql_executor(sql, engine):
    return pd.read_sql(sql, engine, coerce_float=False, dtype=str)


def dtype_to_str(df: pd.DataFrame) -> pd.DataFrame:
    def _dtype_to_str(name: str, s: pd.Series) -> Tuple[str, pd.Series]:
        s = s.astype(str)
        s = s.apply(lambda x: re.sub(r'(\.0$|nan|NaT|None|\s+$|^\s+)', '', x))
        return name, s

    df_columns = df.columns
    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = [executor.submit(_dtype_to_str, column, df[column]) for column in df.columns]
        df = pd.concat([pd.Series(future.result()[1], name=future.result()[0]) for future in as_completed(futures)], axis=1)

    df = df[df_columns]
    return df


def differential_matching(df1: pd.DataFrame, df2: pd.DataFrame, pivot: str = 'pair_up') -> Optional[Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]]:
    try:
        inner_df = pd.merge(df1, df2, on=pivot, how='inner')  # df1 | df2
        df1 = df1[~df1[pivot].isin(inner_df[pivot])]          # df1 - inner_df
        df2 = df2[~df2[pivot].isin(inner_df[pivot])]          # df2 - inner_df
        inner_df = inner_df.drop([pivot], axis=1)
        df1 = df1.drop([pivot], axis=1)
        df2 = df2.drop([pivot], axis=1)
        return inner_df, df1, df2
    except TypeError as e:
        pass
    except MergeError as e:
        pass
    except KeyError as e:
        pass
    except Exception as e:
        pass


def data_frame_slicer(main_df: pd.DataFrame):
    left_df = main_df[main_df['id_fct'].isna()]
    left_df = left_df.drop(['id_fct', 'c_origen', 'prefijo_fct', 'consecutivo_fct', 'factura_fct', 'nro_factura_afec', 'line_fct', 'tienda_desc_fct', 'tienda_fct', 'caja_fct', 'trx_fct', 'fecha_fct', 'mes', 'valor_fct', 'cliente_fct', 'duplicada', 'f_envio_dian', 'estado_dian', 'log_errores_dian', 'cufe'], axis=1)
    main_df = main_df[~main_df['id_fct'].isna()]
    right_df = main_df[main_df['id_tra'].isna()]
    right_df = right_df.drop(['id_tra', 'tipo_tr', 'estado', 'prefijo_jan', 'consecutivo_jan', 'factura_jan', 'line_jan', 'tienda_desc_jan', 'tienda_jan', 'caja_jan', 'trx_jan', 'fecha_cierre', 'fecha_ini', 'fecha_fin', 'valor_jan', 'cliente_jan', 'tipo_identificacion', 'canal'], axis=1)
    main_df = main_df[~main_df['id_tra'].isna()]
    return main_df, left_df, right_df


# Crea un nuevo campo por el cual realizar el emparejamiento
def identifier(line: str, store: str, pos: str, trx: str, date: str):
    line = str(line) if line is not None else ''
    store = str(store) if store is not None else ''
    pos = str(pos) if pos is not None else ''
    trx = str(trx) if trx is not None else ''
    date = str(date) if date is not None else ''

    line = re.sub(r'(\.0$|nan|NaT|None|\s+$|^\s+)', '', line)
    store = re.sub(r'(\.0$|nan|NaT|None|\s+$|^\s+)', '', store)
    pos = re.sub(r'(\.0$|nan|NaT|None|\s+$|^\s+)', '', pos)
    trx = re.sub(r'(\.0$|nan|NaT|None|\s+$|^\s+)', '', trx)
    date = re.sub(r'(\.0$|nan|NaT|None|\s+$|^\s+)', '', date)
    return line + store.zfill(4) + pos.zfill(4) + trx.zfill(5) + date.replace('-', '')


def find_pair_fct_row(_row) -> dict:
    _re = row_empty()
    _re.update(_row.to_dict())

    dates = calculate_date_range(datetime.strptime(_row['fecha_cierre'], '%Y-%m-%d'), 1)
    _result = pd.read_sql(PAIR_EDOC_FCT_SQL.format_map({
        'edoc': _row['factura_jan'],
        'trx': _row['trx_jan'],
        'start_date': dates[0],
        'end_date': dates[1]
    }), engine_fct)
    if not _result.empty:
        _re.update(_result.iloc[0].to_dict())
    else:
        # dates = calculate_date_range(datetime.strptime(_row['fecha_cierre'], '%Y-%m-%d'), 1)
        _result = pd.read_sql(PAIR_SPTD_FCT_SQL.format_map({
            'store': _row['tienda_jan'],
            'pos': _row['caja_jan'].zfill(2),
            'trx': _row['trx_jan'],
            'start_date': dates[0],
            'end_date': dates[1]
        }), engine_fct)
        if not _result.empty:
            if _row['tipo_tr'] == 'F':
                if not _result[(_result['c_origen'] == '5') & (_result['prefijo_fct'] == 'RASU')].empty:
                    _re.update(_result[(_result['c_origen'] == '5') & (_result['prefijo_fct'] == 'RASU')].iloc[0].to_dict())
                elif not _result[_result['c_origen'] == '13'].empty:
                    _re.update(_result[_result['c_origen'] == '13'].iloc[0].to_dict())
                else:
                    _re.update(_result[_result['c_origen'] == '5'].iloc[0].to_dict())
            else:
                _re.update(_result[_result['c_origen'] == '9'].iloc[0].to_dict())
        else:
            dates = calculate_date_range(datetime.strptime(_row['fecha_ini'], '%Y-%m-%d'), 1)
            _result = pd.read_sql(PAIR_SPTD_FCT_SQL.format_map({
                'store': _row['tienda_jan'],
                'pos': _row['caja_jan'].zfill(2),
                'trx': _row['trx_jan'],
                'start_date': dates[0],
                'end_date': dates[1]
            }), engine_fct)
            if not _result.empty:
                if _row['tipo_tr'] == 'F':
                    if not _result[(_result['c_origen'] == '5') & (_result['prefijo_fct'] == 'RASU')].empty:
                        _re.update(_result[(_result['c_origen'] == '5') & (_result['prefijo_fct'] == 'RASU')].iloc[0].to_dict())
                    elif not _result[_result['c_origen'] == '13'].empty:
                        _re.update(_result[_result['c_origen'] == '13'].iloc[0].to_dict())
                    else:
                        _re.update(_result[_result['c_origen'] == '5'].iloc[0].to_dict())
                else:
                    _re.update(_result[_result['c_origen'] == '9'].iloc[0].to_dict())
            else:
                dates = calculate_date_range(datetime.strptime(_row['fecha_fin'], '%Y-%m-%d'), 1)
                _result = pd.read_sql(PAIR_SPTD_FCT_SQL.format_map({
                    'store': _row['tienda_jan'],
                    'pos': _row['caja_jan'].zfill(2),
                    'trx': _row['trx_jan'],
                    'start_date': dates[0],
                    'end_date': dates[1]
                }), engine_fct)
                if not _result.empty:
                    if _row['tipo_tr'] == 'F':
                        if not _result[(_result['c_origen'] == '5') & (_result['prefijo_fct'] == 'RASU')].empty:
                            _re.update(_result[(_result['c_origen'] == '5') & (_result['prefijo_fct'] == 'RASU')].iloc[0].to_dict())
                        elif not _result[_result['c_origen'] == '13'].empty:
                            _re.update(_result[_result['c_origen'] == '13'].iloc[0].to_dict())
                        else:
                            _re.update(_result[_result['c_origen'] == '5'].iloc[0].to_dict())
                    else:
                        _re.update(_result[_result['c_origen'] == '9'].iloc[0].to_dict())

    return _re


def find_pair_jan_row(_row: pd.Series, query: str, engine: create_engine) -> dict:
    _re = row_empty()
    _re.update(_row.to_dict())
    dates = calculate_date_range(datetime.strptime(_row['fecha_fct'], '%Y-%m-%d'), 1)
    fct = pd.read_sql_query(query.format_map({
        'store': _row['tienda_fct'],
        'pos': _row['caja_fct'],
        'trx': _row['trx_fct'],
        'start_date': dates[0],
        'end_date': dates[1]
    }), engine)
    if not fct.empty:
        _re.update(fct.iloc[0].to_dict())

    return _re