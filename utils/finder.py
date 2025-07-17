from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import date, datetime, timedelta
import re
from typing import Tuple, Optional

from dateutil.parser import parse
from sqlalchemy import Engine, TextClause
import pandas as pd
from pandas import DataFrame, read_sql, Series
from pandas.errors import MergeError

from config import biller_engine, jano_engine, log_console_level, log_file_level
from config.logger_config import setup_logger
from models import BILLER_FIND_DOC_BY_ATTRIBUTES, JANO_FIND_INVOICE_BY_ATTRIBUTES, JANO_FIND_MEMO_BY_ATTRIBUTES


logger = setup_logger(__name__, console_level=log_console_level, file_level=log_file_level)


def calculate_date_range(central_date: date, days: int = 4) -> tuple[str, str]:
    """
    Calculate the start and end dates around a central date with specified days extension.

    Args:
        central_date (date): The central date around which to calculate the range
        days (int): Number of days to extend in both directions (negative values will be
                   converted to positive, floats will be truncated to integer)

    Returns:
        tuple[str, str]: Tuple with start and end dates in 'dd/mm/YYYY' format

    Examples:
        >>> from datetime import date
        >>> calculate_date_range(date(2024, 8, 31), 4)
        ('27/08/2024', '04/09/2024')

        >>> calculate_date_range(date(2023, 3, 1), 2)
        ('27/02/2023', '03/03/2023')

        >>> calculate_date_range(date(2024, 2, 28), 1.9)
        ('27/02/2024', '29/02/2024')

        >>> calculate_date_range(date(2024, 5, 15), -3)
        ('12/05/2024', '18/05/2024')
    """
    processed_days = abs(int(days))
    start_date = central_date - timedelta(days=processed_days)
    end_date = central_date + timedelta(days=processed_days)
    return (
        start_date.strftime('%Y-%m-%d'),
        end_date.strftime('%Y-%m-%d')
    )


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


def differential_matching(
        df1: DataFrame, df2: DataFrame, pivot: str = 'pair_up'
) -> Optional[Tuple[DataFrame, DataFrame, DataFrame]]:
    """Devuelve tres DataFrames: la intersección de df1 y df2, los elementos únicos de df1 y los elementos únicos de df2."""
    try:
        if not isinstance(df1, DataFrame) or not isinstance(df2, DataFrame):
            raise TypeError("Se espera que 'df1' y 'df2' sean de tipo 'DataFrame' de Pandas.")
        if df1.empty or df2.empty:
            raise ValueError("Se espera que 'df1' y 'df2' tengan contenido.")
        if not isinstance(pivot, str):
            raise TypeError("Se espera que 'pivot' sea de tipo 'str'.")
        if pivot not in df1.columns or pivot not in df2.columns:
            raise KeyError(f"La clave '{pivot}' no se encuentra en los DataFrames proporcionados.")
        inner_df = pd.merge(df1, df2, on=pivot, how='inner')  # df1 | df2
        df1 = df1[~df1[pivot].isin(inner_df[pivot])]          # df1 - inner_df
        df2 = df2[~df2[pivot].isin(inner_df[pivot])]          # df2 - inner_df
        return inner_df, df1, df2
    except TypeError:
        logger.exception(f"Los tipos proporcionados no son válidos.")
    except MergeError:
        logger.exception(f"Error al intentar realizar la unión de DataFrames.")
    except KeyError:
        logger.exception(f"Error al intentar acceder a la clave '{pivot}' en los DataFrames proporcionados.")
    except Exception as e:
        logger.error(f"Se ha producido un error inesperado mientras se procesaba la unión de DataFrames: {e}")


def data_frame_slicer(main_df: DataFrame) -> Optional[Tuple[DataFrame, DataFrame, DataFrame]]:
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


def find_biller_document_by_attributes(
        s: Series, 
        clause: TextClause = BILLER_FIND_DOC_BY_ATTRIBUTES,
        engine: Engine = biller_engine
) -> Optional[dict]:
    """Devuelve un diccionario con datos encontrados en el Facturador."""
    try:
        if not isinstance(s, Series):
            raise TypeError("Se espera que 's' sea de tipo 'Series' de Pandas.")
        if s.empty:
            raise ValueError("Se espera que 's' tenga contenido.")
        if not isinstance(clause, TextClause):
            raise TypeError("Se espera que 'clause' sea de tipo 'TextClause' de SQLAlchemy.")
        if not isinstance(engine, Engine):
            raise TypeError("Se espera que 'engine' sea de tipo 'Engine' de SQLAlchemy.")
        billed_at = parse(s["fecha_cierre"])
        started_at = parse(s["fecha_ini"])
        finished_at = parse(s["fecha_fin"])
        params = {
            'doc_num': s["factura_jan"],
            'store': int(s["tienda_jan"]),
            'pos': int(s["caja_jan"]),
            'trx': int(s["trx_jan"]),
            'billed_at_i': billed_at - timedelta(days=1),
            'billed_at_j': billed_at + timedelta(days=1),
            'started_at_i': started_at - timedelta(days=1),
            'started_at_j': started_at + timedelta(days=1),
            'finished_at_i': finished_at - timedelta(days=1),
            'finished_at_j': finished_at + timedelta(days=1),
        }
        partner = read_sql(clause, engine, params=params)
        if not partner.empty:
            if s["tipo_tr"] == 'F':
                replaces = partner[partner['prefijo_fct'] == 'RASU']
                if not replaces.empty:
                    return replaces.iloc[0].to_dict()  # Devuelve el primer documento de remplazo
                contingency = partner[partner['c_origen'] == '13']
                if not contingency.empty:
                    return contingency.iloc[0].to_dict()  # Devuelve el primer documento de contingencia
                invoice = partner[partner['c_origen'] == '5']
                if not invoice.empty:
                    return invoice.iloc[0].to_dict()  # Devuelve el primer documento factura
            else:
                credit_memo = partner[partner['c_origen'] == '9']
                if not credit_memo.empty:
                    return credit_memo.iloc[0].to_dict()  # Devuelve la primera nota crédito
                debit_memo = partner[partner['c_origen'] == '15']
                if not debit_memo.empty:
                    return debit_memo.iloc[0].to_dict()  # Devuelve la primera nota crédito
    except TypeError:
        logger.exception("Los tipos proporcionados no son válidos.")
    except ValueError:
        logger.exception("Los valores proporcionados no son válidos.")
    except KeyError:
        logger.exception("Error al buscar una palabra clave dentro del DataFrame de Pandas.")
    except Exception as e:
        logger.error(f"Se ha producido un error al buscar información sobre el Facturador: {e}")
    return None


def find_jano_document_by_attributes(
        s: Series,
        clause: TextClause = JANO_FIND_INVOICE_BY_ATTRIBUTES,
        engine: Engine = jano_engine
) -> Optional[dict]:
    try:
        if not isinstance(s, Series):
            raise TypeError("Se espera que 's' sea de tipo 'Series' de Pandas.")
        if s.empty:
            raise ValueError("Se espera que 's' tenga contenido.")
        if not isinstance(clause, TextClause):
            raise TypeError("Se espera que 'clause' sea de tipo 'TextClause' de SQLAlchemy.")
        if not isinstance(engine, Engine):
            raise TypeError("Se espera que 'engine' sea de tipo 'Engine' de SQLAlchemy.")
        match = row_empty()
        match.update(s.to_dict())
        billed_at = parse(s['fecha_fct'])
        params = {
            'store': int(s['tienda_fct']),
            'pos': int(s['caja_fct']),
            'trx': int(s['trx_fct']),
            'start_date': billed_at - timedelta(days=1),
            'end_date': billed_at + timedelta(days=1)
        }
        partner = read_sql(clause, engine, params=params)
        if not partner.empty:
            match.update(partner.iloc[0].to_dict())

        return match
    except TypeError:
        logger.exception("Los tipos proporcionados no son válidos.")
    except ValueError:
        logger.exception("Los valores proporcionados no son válidos.")
    except Exception as e:
        logger.error(f"Se ha producido un error al buscar información sobre Jano: {e}")


def find_biller_pair(df: DataFrame) -> Optional[DataFrame]:
    """Crea una estructura de consultas en paralelo para hallar parejas de documentos disponibles en Jano"""
    try:
        if not isinstance(df, DataFrame):
            raise TypeError("Se espera que 'df' sea de tipo 'DataFrame' de Pandas.")
        if df.empty:
            return df  # Devuelve el DataFrame vacío si no hay datos
        with ThreadPoolExecutor(max_workers=5) as executor:
            futures = [executor.submit(find_biller_document_by_attributes, row) for _, row in df.iterrows()]
            biller_pairs_df = pd.DataFrame([future.result() for future in as_completed(futures)])
            if not biller_pairs_df.empty:
                return biller_pairs_df
    except TypeError:
        logger.exception("Los tipos proporcionados no son válidos.")
    except ValueError:
        logger.exception("Los valores proporcionados no son válidos.")
    except Exception as e:
        logger.error(f"Se ha producido un error inesperado mientras se procesaba el DataFrame pasado por argumento: {e}")
    return 


def find_jano_pair(df: DataFrame) -> Optional[DataFrame]:
    try:
        if not isinstance(df, DataFrame):
            raise TypeError("Se espera que 'df' sea de tipo 'DataFrame' de Pandas.")
        if df.empty:
            return df  # Devuelve el DataFrame vacío si no hay datos
        with ThreadPoolExecutor(max_workers=5) as executor:
            futures = []
            for _, r in df.iterrows():
                if str(r['c_origen']) in ('5', '8', '13'):
                    futures.append(executor.submit(find_jano_document_by_attributes, r, JANO_FIND_INVOICE_BY_ATTRIBUTES))
                elif str(r['c_origen']) in ('4', '9'):
                    futures.append(executor.submit(find_jano_document_by_attributes, r, JANO_FIND_MEMO_BY_ATTRIBUTES))

            jano_pairs_df = pd.DataFrame([future.result() for future in as_completed(futures)])
        return jano_pairs_df
    except Exception as e:
        logger.error(f"Se ha producido un error inesperado mientras se procesaba el DataFrame pasado por argumento: {e}")
    return None
