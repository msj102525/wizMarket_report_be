import logging
from typing import Dict, List
import pymysql
import pandas as pd
from app.db.connect import (
    get_db_connection,
    get_report_db_connection,
    close_connection,
    close_cursor,
    commit,
    rollback,
)
from app.schemas.common_information import (
    CommonInformation,
    CommonInformationOutput,
    FileGroupOutput,
    FileOutput,
)


def get_all_report_common_information() -> List[CommonInformationOutput]:
    results: Dict[int, CommonInformationOutput] = {}

    try:
        with get_report_db_connection(False) as connection:
            with connection.cursor(pymysql.cursors.DictCursor) as cursor:
                select_query = """
                    SELECT 
                        ci.common_information_id,
                        ci.title,
                        ci.content,
                        ci.file_group_id,
                        ci.is_deleted,
                        ci.etc,
                        ci.reg_id,
                        ci.reg_date,
                        ci.mod_id,
                        ci.mod_date,
                        fg.file_group_id AS fg_file_group_id,
                        fg.reg_id AS fg_reg_id,
                        fg.reg_date AS fg_reg_date,
                        f.file_id,
                        f.original_name,
                        f.save_path,
                        f.save_name,
                        f.url,
                        f.is_deleted AS f_is_deleted,
                        f.etc AS f_etc,
                        f.reg_id AS f_reg_id,
                        f.reg_date AS f_reg_date,
                        f.mod_id AS f_mod_id,
                        f.mod_date AS f_mod_date
                    FROM 
                        t_common_information ci
                    LEFT JOIN 
                        t_file_group fg ON ci.file_group_id = fg.file_group_id
                    LEFT JOIN 
                        t_file f ON fg.file_group_id = f.file_group_id AND f.is_deleted = 'N'
                    WHERE 
                        ci.is_deleted = 'N'
                    ORDER BY ci.common_information_id DESC
                    ;
                """
                cursor.execute(select_query)
                rows = cursor.fetchall()

                # print(rows)

                # 결과가 없으면 빈 리스트 반환
                if not rows:
                    return []

                for row in rows:
                    common_information_id = row["common_information_id"]

                    if common_information_id not in results:
                        results[common_information_id] = CommonInformationOutput(
                            common_information_id=common_information_id,
                            title=row["title"],
                            content=row["content"],
                            file_group_id=row["file_group_id"],
                            is_deleted=row["is_deleted"],
                            etc=row["etc"],
                            reg_id=row["reg_id"],
                            reg_date=row["reg_date"],
                            mod_id=row["mod_id"],
                            mod_date=row["mod_date"],
                            file_groups=[],
                            files=[],
                        )

                    file_group_output = FileGroupOutput(
                        file_group_id=row["fg_file_group_id"],
                        reg_id=row["fg_reg_id"],
                        reg_date=row["fg_reg_date"],
                    )
                    if (
                        file_group_output
                        not in results[common_information_id].file_groups
                    ):
                        results[common_information_id].file_groups.append(
                            file_group_output
                        )

                    if (
                        row["file_id"] is not None
                    ):  # 파일이 있는 경우에만 FileOutput 생성
                        file_output = FileOutput(
                            file_id=row["file_id"],
                            file_group_id=row["fg_file_group_id"],
                            original_name=row["original_name"],
                            save_path=row["save_path"],
                            save_name=row["save_name"],
                            url=row["url"],
                            is_deleted=row["f_is_deleted"],
                            etc=row["f_etc"],
                            reg_id=row["f_reg_id"],
                            reg_date=row["f_reg_date"],
                            mod_id=row.get("f_mod_id"),
                            mod_date=row.get("f_mod_date"),
                        )
                        if file_output not in results[common_information_id].files:
                            results[common_information_id].files.append(file_output)

        return list(results.values())

    except Exception as e:
        logging.error("Error fetching common information: %s", e)
        raise e
