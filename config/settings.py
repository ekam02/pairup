from os import getenv
from pathlib import Path

from dotenv import load_dotenv
from sqlalchemy import create_engine
from oracledb import init_oracle_client


try:
    import tomllib
except ModuleNotFoundError:
    import tomli as tomllib


init_oracle_client()
# load_dotenv()
if load_dotenv():
    F_REP_USER = getenv('F_REP_USER')
    F_REP_PASS = getenv('F_REP_PASS')
    F_REP_HOST = getenv('F_REP_HOST')
    F_REP_PORT = getenv('F_REP_PORT')
    F_REP_NAME = getenv('F_REP_NAME')
    F_REP_SCHE = getenv('F_REP_SCHE')
    J_PRE_USER = getenv('J_PRE_USER')
    J_PRE_PASS = getenv('J_PRE_PASS')
    J_PRE_HOST = getenv('J_PRE_HOST')
    J_PRE_PORT = getenv('J_PRE_PORT')
    J_PRE_NAME = getenv('J_PRE_NAME')
else:
    raise Exception('No .env file found')


fact_engine = create_engine(
    f'postgresql://{F_REP_USER}:{F_REP_PASS}@{F_REP_HOST}:{F_REP_PORT}/{F_REP_NAME}',
    pool_size=5, max_overflow=10,
    connect_args={'options': f'-csearch_path={F_REP_SCHE}'}
)
jano_engine = create_engine(
    f'oracle+oracledb://{J_PRE_USER}:{J_PRE_PASS}@{J_PRE_HOST}:{J_PRE_PORT}/{J_PRE_NAME}',
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
