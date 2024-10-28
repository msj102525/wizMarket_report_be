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
)
logger = logging.getLogger(__name__)


def select_local_store_info_by_store_business_number(
    store_business_id: str,
) -> LocalStoreBasicInfo:

    try:
        with get_db_connection() as connection:
            with connection.cursor(pymysql.cursors.DictCursor) as cursor:
                select_query = """
                    SELECT 
                        R.CITY_NAME,
                        R.DISTRICT_NAME,
                        R.SUB_DISTRICT_NAME,
                        R.DETAIL_CATEGORY_NAME,
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

                row = cursor.fetchone()

                if not row:
                    raise HTTPException(
                        status_code=404,
                        detail=f"LocalStoreBasicInfo {store_business_id}에 해당하는 매장 정보를 찾을 수 없습니다.",
                    )

                result = LocalStoreBasicInfo(
                    city_name=row["CITY_NAME"],
                    district_name=row["DISTRICT_NAME"],
                    sub_district_name=row["SUB_DISTRICT_NAME"],
                    detail_category_name=row["DETAIL_CATEGORY_NAME"],
                    store_name=row["STORE_NAME"],
                    road_name=row["ROAD_NAME"],
                    building_name=row["BUILDING_NAME"],
                    floor_info=row["FLOOR_INFO"],
                    latitude=row["LATITUDE"],
                    longitude=row["LONGITUDE"],
                )

                return result

    except pymysql.Error as e:
        logger.error(f"Database error occurred: {str(e)}")
        raise HTTPException(status_code=503, detail=f"데이터베이스 연결 오류: {str(e)}")
    except Exception as e:
        logger.error(f"Unexpected error occurred: {str(e)}")
        raise HTTPException(status_code=500, detail=f"내부 서버 오류: {str(e)}")
