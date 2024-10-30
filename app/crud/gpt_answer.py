import logging
import pymysql
from fastapi import HTTPException

from app.db.connect import (
    close_connection,
    close_cursor,
    get_db_connection,
)
from app.schemas.report import (
    GPTAnswerRegionDetailCategoryName
)

logger = logging.getLogger(__name__)

def select_region_detail_category_name_by_store_business_number(
    store_business_id: str,
) -> GPTAnswerRegionDetailCategoryName:

    try:
        with get_db_connection() as connection:
            with connection.cursor(pymysql.cursors.DictCursor) as cursor:
                select_query = """
                    SELECT 
                        CITY_NAME,
                        DISTRICT_NAME,
                        SUB_DISTRICT_NAME,
                        DETAIL_CATEGORY_NAME
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
                        detail=f"GPTAnswerRegionDetailCategoryName {store_business_id}에 해당하는 매장 정보를 찾을 수 없습니다.",
                    )

                result = GPTAnswerRegionDetailCategoryName(
                    city_name=row["CITY_NAME"],
                    district_name=row["DISTRICT_NAME"],
                    sub_district_name=row["SUB_DISTRICT_NAME"],
                    detail_category_name=row["DETAIL_CATEGORY_NAME"],
                )
                print(result)
                return result

    except pymysql.Error as e:
        logger.error(f"Database error occurred: {str(e)}")
        raise HTTPException(status_code=503, detail=f"데이터베이스 연결 오류: {str(e)}")
    except Exception as e:
        logger.error(f"Unexpected error occurred GPTAnswerRegionDetailCategoryName: {str(e)}")
        raise HTTPException(status_code=500, detail=f"내부 서버 오류: {str(e)}")


