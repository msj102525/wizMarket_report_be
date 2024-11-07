from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime


class CommonInformation(BaseModel):
    common_information_id: Optional[int] = None
    title: Optional[str] = None
    content: Optional[str] = None
    file_group_id: Optional[int] = None
    is_deleted: str = "N"
    etc: Optional[str] = None
    reg_id: Optional[int] = None
    reg_date: Optional[datetime] = None
    mod_id: Optional[int] = None
    mod_date: Optional[datetime] = None

    class Config:
        from_attributes = True

class FileOutput(BaseModel):
    file_id: int
    file_group_id: int
    original_name: Optional[str] = None
    save_path: Optional[str] = None
    save_name: Optional[str] = None
    url: Optional[str] = None
    is_deleted: str = "N"
    etc: Optional[str] = None
    reg_id: Optional[int] = None
    reg_date: Optional[datetime] = None
    mod_id: Optional[int] = None
    mod_date: Optional[datetime] = None

class FileGroupOutput(BaseModel):
    file_group_id: Optional[int] = None
    reg_id: Optional[int] = None
    reg_date: Optional[datetime] = None

class CommonInformationOutput(BaseModel):
    common_information_id: Optional[int] = None
    title: Optional[str] = None
    content: Optional[str] = None
    file_group_id: Optional[int] = None
    is_deleted: Optional[str] = "N"
    etc: Optional[str] = None
    reg_id: Optional[int] = None
    reg_date: Optional[datetime] = None
    mod_id: Optional[int] = None
    mod_date: Optional[datetime] = None
    file_groups: Optional[List[FileGroupOutput]] = []
    files: Optional[List[FileOutput]] = []
