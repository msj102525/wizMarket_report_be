import logging
from fastapi import APIRouter, Request
import time

router = APIRouter()
logger = logging.getLogger(__name__)


def log_request_start(endpoint: str, request: Request):
    """요청 시작 시 로깅"""
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    client_ip = request.client.host
    request_url = str(request.url)
    params_dict = dict(request.query_params)  # 모든 요청 파라미터를 dict로 변환

    logger.warning(
        f"[{timestamp}] ======================================================="
    )
    logger.info(f"[{timestamp}] Controller Called Start: {endpoint}")
    logger.info(f"[{timestamp}] Request URL: {request_url}")
    logger.info(f"[{timestamp}] Request received from IP: {client_ip}")
    logger.info(f"[{timestamp}] Parameters: {params_dict}")  # 모든 파라미터 로깅


def log_request_end(endpoint: str, process_time: float, response_data):
    """요청 성공 시 로깅 (응답 데이터 포함)"""
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

    # 응답 데이터 크기가 크면 일부만 로깅
    response_str = str(response_data)
    if len(response_str) > 500:  # 500자 이상이면 자름
        response_str = response_str[:200] + "... [Truncated]"

    logger.info(f"[{timestamp}] Response Data: {response_str}")  # 응답 데이터 로깅
    logger.info(f"[{timestamp}] Successfully processed request in {process_time}s")
    logger.info(f"[{timestamp}] Controller Called End: {endpoint}")
    logger.warning(
        f"[{timestamp}] ======================================================="
    )


def log_error(
    endpoint: str, store_business_id: str, process_time: float, error: Exception
):
    """예외 발생 시 로깅"""
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    error_msg = str(error)
    logger.error(f"[{timestamp}] ERROR in {process_time}s | Endpoint: {endpoint}")
    logger.error(f"[{timestamp}] Business ID: {store_business_id}")
    logger.error(f"[{timestamp}] Error: {error_msg}")
