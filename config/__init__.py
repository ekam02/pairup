from datetime import date, timedelta
from pathlib import Path
from dotenv import load_dotenv
from sqlalchemy import create_engine
import os
try:
    import tomllib
except ModuleNotFoundError:
    import tomli as tomllib


load_dotenv()
F_REP_USER = os.getenv('F_REP_USER')
F_REP_PASS = os.getenv('F_REP_PASS')
F_REP_HOST = os.getenv('F_REP_HOST')
F_REP_PORT = os.getenv('F_REP_PORT')
F_REP_NAME = os.getenv('F_REP_NAME')
F_REP_SCHE = os.getenv('F_REP_SCHE')
J_PRE_USER = os.getenv('J_PRE_USER')
J_PRE_PASS = os.getenv('J_PRE_PASS')
J_PRE_HOST = os.getenv('J_PRE_HOST')
J_PRE_PORT = os.getenv('J_PRE_PORT')
J_PRE_NAME = os.getenv('J_PRE_NAME')


engine_fct = create_engine(
    f'postgresql://{F_REP_USER}:{F_REP_PASS}@{F_REP_HOST}:{F_REP_PORT}/{F_REP_NAME}',
    pool_size=5, max_overflow=10,
    connect_args={'options': f'-csearch_path={F_REP_SCHE}'}
)
engine_jan = create_engine(
    f'oracle+cx_oracle://{J_PRE_USER}:{J_PRE_PASS}@{J_PRE_HOST}:{J_PRE_PORT}/{J_PRE_NAME}',
    pool_size=5, max_overflow=10
)

try:
    config_file = Path(__file__).parent / 'config.toml'
    with config_file.open('rb') as config_file:
        cfg = tomllib.load(config_file)
        DATABASE_NAME = cfg['DATABASE_NAME']
        OUTPUT_DIR = Path(cfg['OUTPUT_DIR'])
        REPORT_NAME = cfg['REPORT_NAME']
        STORES = ', '.join([str(st) for st in cfg['STORES']])
        START_DATE = cfg['DATETIME']['START_DATE']
        END_DATE = cfg['DATETIME']['END_DATE']
except FileNotFoundError:
    pass
except Exception as e:
    pass


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
