import logging
import pymysql
from fastapi import HTTPException

from app.db.connect import (
    close_connection,
    close_cursor,
    get_db_connection,
)
from app.schemas.report import (
    LocalStoreTop5Menu,
)

logger = logging.getLogger(__name__)


def select_rising_menu_top5_by_store_business_number(
    store_business_id: str,
) -> LocalStoreTop5Menu:

    try:
        with get_db_connection() as connection:
            with connection.cursor(pymysql.cursors.DictCursor) as cursor:
                select_query = """
                    SELECT 
                        DETAIL_CATEGORY_TOP1_ORDERED_MENU,
                        DETAIL_CATEGORY_TOP2_ORDERED_MENU,
                        DETAIL_CATEGORY_TOP3_ORDERED_MENU,
                        DETAIL_CATEGORY_TOP4_ORDERED_MENU,
                        DETAIL_CATEGORY_TOP5_ORDERED_MENU
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
                        detail=f"LocalStoreTop5Menu {store_business_id}에 해당하는 매장 정보를 찾을 수 없습니다.",
                    )

                result = LocalStoreTop5Menu(
                    detail_category_top1_ordered_menu=row[
                        "DETAIL_CATEGORY_TOP1_ORDERED_MENU"
                    ],
                    detail_category_top2_ordered_menu=row[
                        "DETAIL_CATEGORY_TOP2_ORDERED_MENU"
                    ],
                    detail_category_top3_ordered_menu=row[
                        "DETAIL_CATEGORY_TOP3_ORDERED_MENU"
                    ],
                    detail_category_top4_ordered_menu=row[
                        "DETAIL_CATEGORY_TOP4_ORDERED_MENU"
                    ],
                    detail_category_top5_ordered_menu=row[
                        "DETAIL_CATEGORY_TOP5_ORDERED_MENU"
                    ],
                )

                return result

    except pymysql.Error as e:
        logger.error(f"Database error occurred: {str(e)}")
        raise HTTPException(status_code=503, detail=f"데이터베이스 연결 오류: {str(e)}")
    except Exception as e:
        logger.error(f"Unexpected error occurred LocalStoreTop5Menu: {str(e)}")
        raise HTTPException(status_code=500, detail=f"내부 서버 오류: {str(e)}")
