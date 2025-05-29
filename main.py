from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime

import pandas as pd

from config import fact_engine, jano_engine, OUTPUT_DIR, START_DATE, END_DATE, STORES, REPORT_NAME
from models import QUERY_FCT, QUERY_JAN, PAIR_FT_JAN_SQL, PAIR_NT_JAN_SQL
from utils import sql_executor, data_frame_slicer, identifier, row_empty, find_pair_fct_row, find_pair_jan_row, \
    dtype_to_str, differential_matching, calculate_date_range

if __name__ == '__main__':
    with ThreadPoolExecutor(max_workers=2) as executor:
        fct_thread = executor.submit(sql_executor, QUERY_FCT.format_map({'start_date': START_DATE, 'end_date': END_DATE, 'stores': STORES}), fact_engine)
        jan_thread = executor.submit(sql_executor, QUERY_JAN.format_map({'start_date': START_DATE, 'end_date': END_DATE, 'stores': STORES}), jano_engine)

        fct_df = fct_thread.result()
        jan_df = jan_thread.result()


    jan_df.columns = [attribute.lower() for attribute in jan_df.columns]

    fct_df['trx_fct'] = fct_df['trx_fct'].apply(lambda x: x.zfill(5))
    fct_df['pair_up'] = fct_df['factura_fct'] + fct_df['trx_fct']
    jan_df['trx_jan'] = jan_df['trx_jan'].apply(lambda x: x.zfill(5))
    jan_df['pair_up'] = jan_df['factura_jan'] + jan_df['trx_jan']


    pair_up_df, jan_df, fct_df = differential_matching(jan_df, fct_df)
    pair_up_df = pair_up_df.drop(['pair_up'], axis=1)
    jan_df = jan_df.drop(['pair_up'], axis=1)
    fct_df = fct_df.drop(['pair_up'], axis=1)


    jan_df['pair_up'] = jan_df.apply(
        lambda x: identifier(str(x['line_jan']), str(x['tienda_jan']), str(x['caja_jan']), str(x['trx_jan']), str(x['fecha_cierre'])),
        axis=1
    )
    fct_df['pair_up'] = fct_df.apply(
        lambda x: identifier(str(x['line_fct']), str(x['tienda_fct']), str(x['caja_fct']), str(x['trx_fct']), str(x['fecha_fct'])),
        axis=1
    )


    pair_up_2_df, jan_df, fct_df = differential_matching(jan_df, fct_df)
    pair_up_2_df = pair_up_2_df.drop(['pair_up'], axis=1)
    jan_df = jan_df.drop(['pair_up'], axis=1)
    fct_df = fct_df.drop(['pair_up'], axis=1)


    fct_df = dtype_to_str(fct_df)
    jan_df = dtype_to_str(jan_df)

    new_set = set()

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


    pair_up_3_df = pd.DataFrame([dict(i) for i in new_set], dtype=str)

    pair_up_3_df, jan_df, fct_df = data_frame_slicer(pair_up_3_df)


    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(find_pair_fct_row, _row) for _, _row in jan_df.iterrows()]

        jan_df = pd.DataFrame([future.result() for future in as_completed(futures)])


    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = []
        for _, r in fct_df.iterrows():
            if str(r['c_origen']) in ('5', '8', '13'):
                futures.append(executor.submit(find_pair_jan_row, r, PAIR_FT_JAN_SQL, jano_engine))
            elif str(r['c_origen']) in ('4', '9'):
                futures.append(executor.submit(find_pair_jan_row, r, PAIR_NT_JAN_SQL, jano_engine))

        fct_df = pd.DataFrame([future.result() for future in as_completed(futures)])


    pair_up_df = pd.concat([pair_up_df, pair_up_2_df, pair_up_3_df, jan_df, fct_df], axis=0)

    del jan_df
    del fct_df
    del new_set
    del pair_up_2_df
    del pair_up_3_df


    pair_up_df = dtype_to_str(pair_up_df)


    pair_up_df['tienda'] = pair_up_df.apply(
        lambda x: x['tienda_desc_jan'] if x['tienda_desc_jan'] else x['tienda_desc_fct'],
        axis=1
    )
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

    del pair_up_df
