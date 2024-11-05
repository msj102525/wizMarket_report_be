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
                select_query = """
                    SELECT 
                        R.STORE_NAME,
                        R.ROAD_NAME,
                        R.BUILDING_NAME,
                        R.FLOOR_INFO,
                        R.LATITUDE,
                        R.LONGITUDE,
                        LSI.LOCAL_STORE_IMAGE_URL
                    FROM
                        REPORT R
                    LEFT JOIN LOCAL_STORE_IMAGE LSI ON LSI.STORE_BUSINESS_NUMBER = R.STORE_BUSINESS_NUMBER
                    WHERE R.STORE_BUSINESS_NUMBER = %s
                    ;
                """
                
                # logger.info(f"Executing query: {select_query}")
                cursor.execute(select_query, (store_business_id,))
                
                rows = cursor.fetchall()  # 모든 행 가져오기
                
                if not rows:
                    raise HTTPException(
                        status_code=404,
                        detail=f"LocalStoreBasicInfo {store_business_id}에 해당하는 매장 정보를 찾을 수 없습니다.",
                    )

                # 매장 기본 정보는 첫 행에서 가져오고, 이미지 URL은 리스트로 수집
                first_row = rows[0]
                image_urls = [
                    row["LOCAL_STORE_IMAGE_URL"]
                    for row in rows
                    if row["LOCAL_STORE_IMAGE_URL"] is not None
                ]

                result = LocalStoreBasicInfo(
                    store_name=first_row["STORE_NAME"],
                    road_name=first_row["ROAD_NAME"],
                    building_name=first_row["BUILDING_NAME"],
                    floor_info=first_row["FLOOR_INFO"],
                    latitude=first_row["LATITUDE"],
                    longitude=first_row["LONGITUDE"],
                    local_store_image_url=image_urls,
                )

                return result

    except pymysql.Error as e:
        logger.error(f"Database error occurred: {str(e)}")
        raise HTTPException(status_code=503, detail=f"데이터베이스 연결 오류: {str(e)}")
    except Exception as e:
        logger.error(f"Unexpected error occurred LocalStoreBasicInfo: {str(e)}")
        raise HTTPException(status_code=500, detail=f"내부 서버 오류: {str(e)}")