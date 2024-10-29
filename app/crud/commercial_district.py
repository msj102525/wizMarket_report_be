import logging
import pymysql
from fastapi import HTTPException

from app.db.connect import (
    close_connection,
    close_cursor,
    get_db_connection,
)
from app.schemas.report import (
    LocalStoreCDJSWeightedAverage,
)

logger = logging.getLogger(__name__)


def select_c_d_j_score_average_by_store_business_number(
    store_business_id: str,
) -> LocalStoreCDJSWeightedAverage:

    try:
        with get_db_connection() as connection:
            with connection.cursor(pymysql.cursors.DictCursor) as cursor:
                select_query = """
                    SELECT 
                        COMMERCIAL_DISTRICT_J_SCORE_AVERAGE
                    FROM
                        REPORT 
                    WHERE STORE_BUSINESS_NUMBER = %s
                    ;
                """

                # logger.info(
                #     f"Executing query: {select_query} with business ID: {store_business_id}"
                # )
                cursor.execute(select_query, (store_business_id,))

                row = cursor.fetchone()

                if not row:
                    raise HTTPException(
                        status_code=404,
                        detail=f"LocalStoreCDJSWeightedAverage {store_business_id}에 해당하는 매장 정보를 찾을 수 없습니다.",
                    )

                result = LocalStoreCDJSWeightedAverage(
                    commercial_district_j_score_average=round(
                        row.get("COMMERCIAL_DISTRICT_J_SCORE_AVERAGE"), 1
                    ),
                )

                # logger.info(f"Result for business ID {store_business_id}: {result}")
                return result

    except pymysql.Error as e:
        logger.error(f"Database error occurred: {str(e)}")
        raise HTTPException(status_code=503, detail=f"데이터베이스 연결 오류: {str(e)}")
    except Exception as e:
        logger.error(
            f"Unexpected error occurred in select_c_d_j_score_average_by_store_business_number: {str(e)}"
        )
        raise HTTPException(status_code=500, detail=f"내부 서버 오류: {str(e)}")
