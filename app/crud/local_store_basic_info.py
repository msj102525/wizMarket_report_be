import logging
import pymysql
from fastapi import HTTPException

from app.db.connect import (
    close_connection,
    close_cursor,
    get_db_connection,
)
from app.schemas.report import (
    LocalStoreBasicInfo,
    LocalStoreRedux,
)

logger = logging.getLogger(__name__)


def select_local_store_info_redux_by_store_business_number(
    store_business_id: str,
) -> LocalStoreRedux:

    try:
        with get_db_connection() as connection:
            with connection.cursor(pymysql.cursors.DictCursor) as cursor:
                select_query = """
                    SELECT 
                        CITY_NAME,
                        DISTRICT_NAME,
                        SUB_DISTRICT_NAME,
                        DETAIL_CATEGORY_NAME,
                        LOC_INFO_DATA_REF_DATE,
                        NICE_BIZ_MAP_DATA_REF_DATE,
                        POPULATION_DATA_REF_DATE
                    FROM
                        REPORT 
                    WHERE STORE_BUSINESS_NUMBER = %s
                    ;
                """

                # logger.info(f"Executing query: {select_query}")
                cursor.execute(select_query, (store_business_id,))

                row = cursor.fetchone()

                # logger.info(row)

                if not row:
                    raise HTTPException(
                        status_code=404,
                        detail=f"LocalStoreBasicInfo {store_business_id}에 해당하는 매장 정보를 찾을 수 없습니다.",
                    )

                result = LocalStoreRedux(
                    city_name=row["CITY_NAME"],
                    district_name=row["DISTRICT_NAME"],
                    sub_district_name=row["SUB_DISTRICT_NAME"],
                    detail_category_name=row["DETAIL_CATEGORY_NAME"],
                    loc_info_data_ref_date=row["LOC_INFO_DATA_REF_DATE"],
                    nice_biz_map_data_ref_date=row["NICE_BIZ_MAP_DATA_REF_DATE"],
                    population_data_ref_date=row["POPULATION_DATA_REF_DATE"],
                )

                return result

    except pymysql.Error as e:
        logger.error(f"Database error occurred: {str(e)}")
        raise HTTPException(status_code=503, detail=f"데이터베이스 연결 오류: {str(e)}")
    except Exception as e:
        logger.error(f"Unexpected error occurred LocalStoreRedux: {str(e)}")
        raise HTTPException(status_code=500, detail=f"내부 서버 오류: {str(e)}")


def select_local_store_info_by_store_business_number(
    store_business_id: str,
) -> LocalStoreBasicInfo:

    try:
        with get_db_connection() as connection:
            with connection.cursor(pymysql.cursors.DictCursor) as cursor:

                # REPORT 테이블에서 기본 매장 정보 조회
                report_query = """
                    SELECT 
                        STORE_NAME,
                        ROAD_NAME,
                        BUILDING_NAME,
                        FLOOR_INFO,
                        LATITUDE,
                        LONGITUDE,
                        CITY_NAME,
                        SUB_DISTRICT_NAME,
                        DETAIL_CATEGORY_NAME,
                        LOC_INFO_SHOP_K,
                        LOC_INFO_AVERAGE_SALES_K,
                        LOC_INFO_INCOME_WON,
                        LOC_INFO_AVERAGE_SPEND_K,
                        LOC_INFO_MOVE_POP_K,
                        LOC_INFO_RESIDENT_K,
                        LOC_INFO_HOUSE_K,
                        COMMERCIAL_DISTRICT_SUB_DISTRICT_MARKET_SIZE,
                        COMMERCIAL_DISTRICT_SUB_DISTRICT_AVERAGE_SALES,
                        COMMERCIAL_DISTRICT_SUB_DISTRICT_AVERAGE_PAYMENT,
                        COMMERCIAL_DISTRICT_SUB_DISTRICT_USAGE_COUNT,
                        COMMERCIAL_DISTRICT_AVERAGE_SALES_PERCENT_MON,
                        COMMERCIAL_DISTRICT_AVERAGE_SALES_PERCENT_TUE,
                        COMMERCIAL_DISTRICT_AVERAGE_SALES_PERCENT_WED,
                        COMMERCIAL_DISTRICT_AVERAGE_SALES_PERCENT_THU,
                        COMMERCIAL_DISTRICT_AVERAGE_SALES_PERCENT_FRI,
                        COMMERCIAL_DISTRICT_AVERAGE_SALES_PERCENT_SAT,
                        COMMERCIAL_DISTRICT_AVERAGE_SALES_PERCENT_SUN,
                        COMMERCIAL_DISTRICT_AVERAGE_SALES_PERCENT_06_09,
                        COMMERCIAL_DISTRICT_AVERAGE_SALES_PERCENT_09_12,
                        COMMERCIAL_DISTRICT_AVERAGE_SALES_PERCENT_12_15,
                        COMMERCIAL_DISTRICT_AVERAGE_SALES_PERCENT_15_18,
                        COMMERCIAL_DISTRICT_AVERAGE_SALES_PERCENT_18_21,
                        COMMERCIAL_DISTRICT_AVERAGE_SALES_PERCENT_21_24,
                        COMMERCIAL_DISTRICT_AVG_CLIENT_PER_M_20S,
                        COMMERCIAL_DISTRICT_AVG_CLIENT_PER_M_30S,
                        COMMERCIAL_DISTRICT_AVG_CLIENT_PER_M_40S,
                        COMMERCIAL_DISTRICT_AVG_CLIENT_PER_M_50S,
                        COMMERCIAL_DISTRICT_AVG_CLIENT_PER_M_60_over,
                        COMMERCIAL_DISTRICT_AVG_CLIENT_PER_F_20S,
                        COMMERCIAL_DISTRICT_AVG_CLIENT_PER_F_30S,
                        COMMERCIAL_DISTRICT_AVG_CLIENT_PER_F_40S,
                        COMMERCIAL_DISTRICT_AVG_CLIENT_PER_F_50S,
                        COMMERCIAL_DISTRICT_AVG_CLIENT_PER_F_60_over
                    FROM REPORT
                    WHERE STORE_BUSINESS_NUMBER = %s
                """
                cursor.execute(report_query, (store_business_id,))
                row = cursor.fetchone()

                if not row:
                    raise HTTPException(
                        status_code=404,
                        detail=f"LocalStoreBasicInfo {store_business_id}에 해당하는 매장 정보를 찾을 수 없습니다.",
                    )

                # LOCAL_STORE_IMAGE 테이블에서 이미지 URL 조회
                image_query = """
                    SELECT LOCAL_STORE_IMAGE_URL
                    FROM LOCAL_STORE_IMAGE
                    WHERE STORE_BUSINESS_NUMBER = %s
                    AND STATUS = 'Y'
                """
                cursor.execute(image_query, (store_business_id,))
                images = cursor.fetchall()
                image_urls = [
                    row["LOCAL_STORE_IMAGE_URL"]
                    for row in images
                    if row["LOCAL_STORE_IMAGE_URL"] is not None
                ]

                age_gender_mapping = {
                    "COMMERCIAL_DISTRICT_AVG_CLIENT_PER_M_20S": "20대 남성",
                    "COMMERCIAL_DISTRICT_AVG_CLIENT_PER_M_30S": "30대 남성",
                    "COMMERCIAL_DISTRICT_AVG_CLIENT_PER_M_40S": "40대 남성",
                    "COMMERCIAL_DISTRICT_AVG_CLIENT_PER_M_50S": "50대 남성",
                    "COMMERCIAL_DISTRICT_AVG_CLIENT_PER_M_60_over": "60대 이상 남성",
                    "COMMERCIAL_DISTRICT_AVG_CLIENT_PER_F_20S": "20대 여성",
                    "COMMERCIAL_DISTRICT_AVG_CLIENT_PER_F_30S": "30대 여성",
                    "COMMERCIAL_DISTRICT_AVG_CLIENT_PER_F_40S": "40대 여성",
                    "COMMERCIAL_DISTRICT_AVG_CLIENT_PER_F_50S": "50대 여성",
                    "COMMERCIAL_DISTRICT_AVG_CLIENT_PER_F_60_over": "60대 이상 여성",
                }

                # 주요 고객 비율 중 최고 2개 추출
                sorted_client_data = sorted(
                    (
                        (k, v)
                        for k, v in row.items()
                        if k in age_gender_mapping and v is not None
                    ),
                    key=lambda item: item[1] or 0,  # None일 경우 0으로 처리
                    reverse=True,
                )

                top1 = (
                    sorted_client_data[0] if len(sorted_client_data) > 0 else (None, 0)
                )

                # 요일별 최대 및 최소 판매 비율 찾기
                weekdays = [
                    ("월요일", row["COMMERCIAL_DISTRICT_AVERAGE_SALES_PERCENT_MON"]),
                    ("화요일", row["COMMERCIAL_DISTRICT_AVERAGE_SALES_PERCENT_TUE"]),
                    ("수요일", row["COMMERCIAL_DISTRICT_AVERAGE_SALES_PERCENT_WED"]),
                    ("목요일", row["COMMERCIAL_DISTRICT_AVERAGE_SALES_PERCENT_THU"]),
                    ("금요일", row["COMMERCIAL_DISTRICT_AVERAGE_SALES_PERCENT_FRI"]),
                    ("토요일", row["COMMERCIAL_DISTRICT_AVERAGE_SALES_PERCENT_SAT"]),
                    ("일요일", row["COMMERCIAL_DISTRICT_AVERAGE_SALES_PERCENT_SUN"]),
                ]

                # None이거나 0인 경우 필터링
                weekdays_filtered = [
                    (day, percent)
                    for day, percent in weekdays
                    if percent is not None and percent != 0
                ]

                max_weekday = (
                    max(weekdays_filtered, key=lambda x: x[1])
                    if weekdays_filtered
                    else ("-", 0)
                )


                # 시간대별 최대 판매 비율 찾기
                time_slots = [
                    ("06~09", row["COMMERCIAL_DISTRICT_AVERAGE_SALES_PERCENT_06_09"]),
                    ("09~12", row["COMMERCIAL_DISTRICT_AVERAGE_SALES_PERCENT_09_12"]),
                    ("12~15", row["COMMERCIAL_DISTRICT_AVERAGE_SALES_PERCENT_12_15"]),
                    ("15~18", row["COMMERCIAL_DISTRICT_AVERAGE_SALES_PERCENT_15_18"]),
                    ("18~21", row["COMMERCIAL_DISTRICT_AVERAGE_SALES_PERCENT_18_21"]),
                    ("21~24", row["COMMERCIAL_DISTRICT_AVERAGE_SALES_PERCENT_21_24"]),
                ]

                # None이거나 0인 경우 필터링
                time_slots_filtered = [
                    (slot, percent)
                    for slot, percent in time_slots
                    if percent is not None and percent != 0
                ]

                max_time = (
                    max(time_slots_filtered, key=lambda x: x[1])
                    if time_slots_filtered
                    else ("-", 0)
                )


                logger.info(f'top1 : {top1}')
                logger.info(f'max_weekday : {max_weekday}')
                logger.info(f'max_time : {max_time}')
                
                # LocalStoreBasicInfo 객체 생성
                result = LocalStoreBasicInfo(
                    store_name=row["STORE_NAME"],
                    road_name=row["ROAD_NAME"],
                    building_name=row["BUILDING_NAME"],
                    floor_info=row["FLOOR_INFO"],
                    latitude=row["LATITUDE"],
                    longitude=row["LONGITUDE"],
                    local_store_image_url=image_urls,
                )

                return result

    except pymysql.Error as e:
        logger.error(f"Database error occurred: {str(e)}")
        raise HTTPException(status_code=503, detail=f"데이터베이스 연결 오류: {str(e)}")
    except Exception as e:
        logger.error(f"Unexpected error occurred LocalStoreBasicInfo: {str(e)}")
        raise HTTPException(status_code=500, detail=f"내부 서버 오류: {str(e)}")
