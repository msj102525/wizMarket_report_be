import logging
from datetime import datetime

logger = logging.getLogger(__name__)


def log_service_start(service_name: str):
    """서비스 호출 시작 시 로깅"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    logger.info(f"[{timestamp}] Service Called Start: {service_name}")


def log_db_fetch(service_name: str):
    """DB 조회 시작 로깅"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    logger.info(f"[{timestamp}] Fetching data from DB in {service_name}...")


def log_service_end(service_name: str, process_time: float):
    """서비스 호출 종료 시 로깅"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    logger.info(f"[{timestamp}] Successfully processed in {process_time}s")
    logger.info(f"[{timestamp}] Service Called End: {service_name}")


def log_service_error(
    service_name: str, process_time: float, error: Exception
):
    """서비스 에러 발생 시 로깅"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    error_msg = str(error)

    logger.error(f"[{timestamp}] ERROR in {process_time}s | Service: {service_name}")
    logger.error(f"[{timestamp}] Error: {error_msg}")
