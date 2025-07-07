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
            biller_user = getenv('BILLER_USER')
            biller_pass = getenv('BILLER_PASS')
            biller_host = getenv('BILLER_HOST')
            biller_port = getenv('BILLER_PORT')
            biller_name = getenv('BILLER_NAME')
            biller_sche = getenv('BILLER_SCHE')
            jano_user = getenv('JANO_USER')
            jano_pass = getenv('JANO_PASS')
            jano_host = getenv('JANO_HOST')
            jano_port = getenv('JANO_PORT')
            jano_name = getenv('JANO_NAME')
            logger.debug('Environment variables loaded')

            self.biller_engine = create_engine(
                f'postgresql://{biller_user}:{biller_pass}@{biller_host}:{biller_port}/{biller_name}',
                pool_size=5, max_overflow=10,
                connect_args={'options': f'-csearch_path={biller_sche}'}
            )
            self.jano_engine = create_engine(
                f'oracle+oracledb://{jano_user}:{jano_pass}@{jano_host}:{jano_port}/{jano_name}',
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
