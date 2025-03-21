import logging
import time
from datetime import datetime

logger = logging.getLogger(__name__)


def log_crud_start(crud_name: str):
    """CRUD 함수 시작 시 로깅"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    logger.info(f"[{timestamp}] CRUD Operation Start: {crud_name}")


def log_crud_query(crud_name: str, query: str, params: tuple):
    """쿼리 실행 전 로깅 (완성된 SQL 포함)"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_query = query.replace("%s", "{}").format(*params)  # 완성된 SQL 생성
    logger.info(f"[{timestamp}] Executing query in {crud_name}")
    logger.info(f"[{timestamp}] Query: {formatted_query}")  # SQL 출력



def log_crud_error(crud_name: str, error: Exception):
    """CRUD 함수 에러 발생 시 로깅"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    error_msg = str(error)
    logger.error(f"[{timestamp}] ERROR in CRUD Operation: {crud_name}")
    logger.error(f"[{timestamp}] Error: {error_msg}")
