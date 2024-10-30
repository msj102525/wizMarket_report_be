import logging
import pymysql
from fastapi import HTTPException

from app.db.connect import (
    close_connection,
    close_cursor,
    get_db_connection,
)
from app.schemas.report import (
    LocalStoreRisingBusinessNTop5SDTop3,
)

logger = logging.getLogger(__name__)


def select_rising_business_by_store_business_id(
    store_business_id: str,
) -> LocalStoreRisingBusinessNTop5SDTop3:

    try:
        with get_db_connection() as connection:
            with connection.cursor(pymysql.cursors.DictCursor) as cursor:
                select_query = """
                    SELECT 
                        RISING_BUSINESS_NATIONAL_RISING_SALES_TOP1_INFO,
                        RISING_BUSINESS_NATIONAL_RISING_SALES_TOP2_INFO,
                        RISING_BUSINESS_NATIONAL_RISING_SALES_TOP3_INFO,
                        RISING_BUSINESS_NATIONAL_RISING_SALES_TOP4_INFO,
                        RISING_BUSINESS_NATIONAL_RISING_SALES_TOP5_INFO,
                        RISING_BUSINESS_SUB_DISTRICT_RISING_SALES_TOP1_INFO,
                        RISING_BUSINESS_SUB_DISTRICT_RISING_SALES_TOP2_INFO,
                        RISING_BUSINESS_SUB_DISTRICT_RISING_SALES_TOP3_INFO
                    FROM
                        REPORT 
                    WHERE STORE_BUSINESS_NUMBER = %s
                    ;
                """

                # logger.info(f"Executing query: {select_query}")
                cursor.execute(select_query, (store_business_id,))

                row = cursor.fetchone()

                if not row:
                    raise HTTPException(
                        status_code=404,
                        detail=f"LocalStoreRisingBusinessNTop5SDTop3 {store_business_id}에 해당하는 매장 정보를 찾을 수 없습니다.",
                    )

                result = LocalStoreRisingBusinessNTop5SDTop3(
                    rising_business_national_rising_sales_top1_info=row[
                        "RISING_BUSINESS_NATIONAL_RISING_SALES_TOP1_INFO"
                    ],
                    rising_business_national_rising_sales_top2_info=row[
                        "RISING_BUSINESS_NATIONAL_RISING_SALES_TOP2_INFO"
                    ],
                    rising_business_national_rising_sales_top3_info=row[
                        "RISING_BUSINESS_NATIONAL_RISING_SALES_TOP3_INFO"
                    ],
                    rising_business_national_rising_sales_top4_info=row[
                        "RISING_BUSINESS_NATIONAL_RISING_SALES_TOP4_INFO"
                    ],
                    rising_business_national_rising_sales_top5_info=row[
                        "RISING_BUSINESS_NATIONAL_RISING_SALES_TOP5_INFO"
                    ],
                    rising_business_sub_district_rising_sales_top1_info=row[
                        "RISING_BUSINESS_SUB_DISTRICT_RISING_SALES_TOP1_INFO"
                    ],
                    rising_business_sub_district_rising_sales_top2_info=row[
                        "RISING_BUSINESS_SUB_DISTRICT_RISING_SALES_TOP2_INFO"
                    ],
                    rising_business_sub_district_rising_sales_top3_info=row[
                        "RISING_BUSINESS_SUB_DISTRICT_RISING_SALES_TOP3_INFO"
                    ],
                )

                return result

    except pymysql.Error as e:
        logger.error(f"Database error occurred: {str(e)}")
        raise HTTPException(status_code=503, detail=f"데이터베이스 연결 오류: {str(e)}")
    except Exception as e:
        logger.error(
            f"Unexpected error occurred LocalStoreRisingBusinessNTop5SDTop3: {str(e)}"
        )
        raise HTTPException(status_code=500, detail=f"내부 서버 오류: {str(e)}")
