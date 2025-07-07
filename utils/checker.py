from typing import Optional

from sqlalchemy.engine import Engine
from sqlalchemy import text
from sqlalchemy.exc import OperationalError, ProgrammingError, SQLAlchemyError

from config import biller_engine, jano_engine, log_console_level, log_file_level
from config.logger_config import setup_logger


logger = setup_logger(__name__, console_level=log_console_level, file_level=log_file_level)


def check_database_availability(engine: Engine) -> Optional[bool]:
    """Comprueba la disponibilidad de la base de datos."""
    try:
        # Intenta conectar y ejecutar una consulta simple
        with engine.connect() as connection:
            # Ejecuta una consulta básica que funciona en la mayoría de bases de datos
            result = connection.execute(text("SELECT 1"))
            result.fetchone()
        return True
    except OperationalError:
        logger.exception(f"Error al conectar con la base de datos")
    except ProgrammingError:
        logger.exception(f"Error al ejecutar la consulta")
    except SQLAlchemyError:
        logger.exception(f"Error al conectar con la base de datos")
    except Exception as e:
        logger.error(f"Error inesperado al verificar la base de datos: {e}")
    return False


def check_availability_of_the_biller_database() -> bool:
    """Comprueba la disponibilidad de la base de datos Biller."""
    return check_database_availability(biller_engine)


def check_availability_of_the_jano_database() -> bool:
    """Comprueba la disponibilidad de la base de datos Jano."""
    return check_database_availability(jano_engine)


def check_all_databases() -> dict:
    """Comprueba la disponibilidad de todas las bases de datos configuradas."""
    return {
        "biller": check_availability_of_the_biller_database(),
        "jano": check_availability_of_the_jano_database()
    }
