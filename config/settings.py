import logging
from os import getenv
from pathlib import Path

from dotenv import load_dotenv
from sqlalchemy import create_engine
from oracledb import init_oracle_client


try:
    import tomllib
except ModuleNotFoundError:
    import tomli as tomllib


logger = logging.getLogger(__name__)


class AppSettings:
    _instance = None  # Patrón Singleton para asegurar una única instancia

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(AppSettings, cls).__new__(cls)
            cls._instance._load_settings()
        return cls._instance

    def _load_settings(self):
        init_oracle_client()
        if load_dotenv():
            self.F_REP_USER = getenv('BILLER_USER')
            self.F_REP_PASS = getenv('BILLER_PASS')
            self.F_REP_HOST = getenv('BILLER_HOST')
            self.F_REP_PORT = getenv('BILLER_PORT')
            self.F_REP_NAME = getenv('BILLER_NAME')
            self.F_REP_SCHE = getenv('BILLER_SCHE')
            self.J_PRE_USER = getenv('JANO_USER')
            self.J_PRE_PASS = getenv('JANO_PASS')
            self.J_PRE_HOST = getenv('JANO_HOST')
            self.J_PRE_PORT = getenv('JANO_PORT')
            self.J_PRE_NAME = getenv('JANO_NAME')
            logger.debug('Environment variables loaded')

            self.fact_engine = create_engine(
                f'postgresql://{self.F_REP_USER}:{self.F_REP_PASS}@{self.F_REP_HOST}:{self.F_REP_PORT}/{self.F_REP_NAME}',
                pool_size=5, max_overflow=10,
                connect_args={'options': f'-csearch_path={self.F_REP_SCHE}'}
            )
            self.jano_engine = create_engine(
                f'oracle+oracledb://{self.J_PRE_USER}:{self.J_PRE_PASS}@{self.J_PRE_HOST}:{self.J_PRE_PORT}/{self.J_PRE_NAME}',
                pool_size=5, max_overflow=10
            )
            logger.debug('Engines created')

            try:
                config_file = Path(__file__).parent / 'config.toml'
                with config_file.open('rb') as config_file:
                    cfg = tomllib.load(config_file)

                self.OUTPUT_DIR = Path(Path(__file__).parent.parent / cfg['OUTPUT_DIR'])
                if not self.OUTPUT_DIR.exists():
                    self.OUTPUT_DIR.mkdir(parents=True)
                    logger.info(f'Created output directory: {self.OUTPUT_DIR}')

                self.REPORT_NAME = cfg['REPORT_NAME']
                self.STORES = ', '.join([str(st) for st in cfg['STORES']])
                self.START_DATE = cfg['DATETIME']['START_DATE']
                self.END_DATE = cfg['DATETIME']['END_DATE']
            except FileNotFoundError:
                logger.exception(f'No configuration file found')
                raise RuntimeError('No configuration file found, application cannot proceed.')
            except Exception as e:
                logger.exception(f'Error loading configuration file: {e}')
                raise RuntimeError(f'Error loading configuration file: {e}')
        else:
            logger.error('No environment variables found')
            raise RuntimeError('No .env file found, application cannot proceed.')


settings = AppSettings()
