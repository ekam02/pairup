from os import getenv
from pathlib import Path

from dotenv import load_dotenv
from sqlalchemy import create_engine
from oracledb import init_oracle_client
import tomllib

from .logger_config import setup_logger


class AppSettings:
    _instance = None  # Patrón Singleton para asegurar una única instancia

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(AppSettings, cls).__new__(cls)
            cls._instance._load_settings()
        return cls._instance

    def _load_settings(self):
        try:
            init_oracle_client()
            load_dotenv()

            cfg_dir_path = Path(__file__).parent     # Config Directory
            app_dir_path = cfg_dir_path.parent       # App Directory
            cfg_file = cfg_dir_path / 'config.toml'  # Config File

            if not cfg_file.exists():
                raise RuntimeError('No configuration file found, application cannot proceed.')

            with cfg_file.open('rb') as cfg_file:
                cfg = tomllib.load(cfg_file)

            db_pool_size = cfg.get("db_pool_size", 5)
            db_max_overflow = cfg.get("db_max_overflow", 10)
            self.log_console_level = cfg.get("log_console_level", 20)
            self.log_file_level = cfg.get("log_file_level", 30)
            self.OUTPUT_DIR = app_dir_path / cfg.get("OUTPUT_DIR", "output")
            self.REPORT_NAME = cfg.get("REPORT_NAME", "conciliation")
            self.STORES = ', '.join([str(st) for st in cfg.get("STORES")])
            self.START_DATE = cfg['DATETIME']['START_DATE']
            self.END_DATE = cfg['DATETIME']['END_DATE']

            logger = setup_logger(__name__, console_level=self.log_console_level, file_level=self.log_file_level)
            logger.info(f"Loading settings from {cfg_file.name}")

            biller_user = getenv('BILLER_USER')
            biller_pass = getenv('BILLER_PASS')
            biller_host = getenv('BILLER_HOST')
            biller_port = getenv('BILLER_PORT')
            biller_name = getenv('BILLER_NAME')
            biller_sche = getenv('BILLER_SCHE')

            if not all([biller_user, biller_pass, biller_host, biller_port, biller_name, biller_sche]):
                logger.error('Missing environment variables')
                raise RuntimeError('Missing environment variables, application cannot proceed.')

            self.biller_engine = create_engine(
                f'postgresql://{biller_user}:{biller_pass}@{biller_host}:{biller_port}/{biller_name}',
                pool_size=db_pool_size, max_overflow=db_max_overflow,
                connect_args={'options': f'-csearch_path={biller_sche}'}
            )

            jano_user = getenv('JANO_USER')
            jano_pass = getenv('JANO_PASS')
            jano_host = getenv('JANO_HOST')
            jano_port = getenv('JANO_PORT')
            jano_name = getenv('JANO_NAME')

            if not all([jano_user, jano_pass, jano_host, jano_port, jano_name]):
                logger.error('Missing environment variables')
                raise RuntimeError('Missing environment variables, application cannot proceed.')

            self.jano_engine = create_engine(
                f'oracle+oracledb://{jano_user}:{jano_pass}@{jano_host}:{jano_port}/{jano_name}',
                pool_size=db_pool_size, max_overflow=db_max_overflow
            )
        except Exception as e:
            raise Exception(e)


settings = AppSettings()
