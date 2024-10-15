from datetime import datetime
from pydantic import BaseModel, Field
from typing import List, Optional, Dict

from app.schemas.statistics import CommercialStatistics


class CommercialDistrict(BaseModel):
    commercial_district_id: int

    city_id: int
    district_id: int
    sub_district_id: int

    biz_main_category_id: int
    biz_sub_category_id: int
    biz_detail_category_id: int

    national_density: float
    city_density: float
    district_density: float
    sub_district_density: float

    market_size: Optional[int] = None

    average_payment: Optional[int] = None
    usage_count: Optional[int] = None

    average_sales: Optional[int] = None
    operating_cost: Optional[int] = None
    food_cost: Optional[int] = None
    employee_cost: Optional[int] = None
    rental_cost: Optional[int] = None
    tax_cost: Optional[int] = None
    family_employee_cost: Optional[int] = None
    ceo_cost: Optional[int] = None
    etc_cost: Optional[int] = None
    average_profit: Optional[int] = None

    avg_profit_per_mon: Optional[float] = None
    avg_profit_per_tue: Optional[float] = None
    avg_profit_per_wed: Optional[float] = None
    avg_profit_per_thu: Optional[float] = None
    avg_profit_per_fri: Optional[float] = None
    avg_profit_per_sat: Optional[float] = None
    avg_profit_per_sun: Optional[float] = None

    avg_profit_per_06_09: Optional[float] = None
    avg_profit_per_09_12: Optional[float] = None
    avg_profit_per_12_15: Optional[float] = None
    avg_profit_per_15_18: Optional[float] = None
    avg_profit_per_18_21: Optional[float] = None
    avg_profit_per_21_24: Optional[float] = None
    avg_profit_per_24_06: Optional[float] = None

    avg_client_per_m_20: Optional[float] = None
    avg_client_per_m_30: Optional[float] = None
    avg_client_per_m_40: Optional[float] = None
    avg_client_per_m_50: Optional[float] = None
    avg_client_per_m_60: Optional[float] = None
    avg_client_per_f_20: Optional[float] = None
    avg_client_per_f_30: Optional[float] = None
    avg_client_per_f_40: Optional[float] = None
    avg_client_per_f_50: Optional[float] = None
    avg_client_per_f_60: Optional[float] = None

    top_menu_1: str = None
    top_menu_2: str = None
    top_menu_3: str = None
    top_menu_4: str = None
    top_menu_5: str = None

    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class CommercialDistrictInsert(BaseModel):
    city_id: int
    district_id: int
    sub_district_id: int

    biz_main_category_id: int
    biz_sub_category_id: int
    biz_detail_category_id: int

    national_density: float
    city_density: float
    district_density: float
    sub_district_density: float

    market_size: Optional[int] = None

    average_payment: Optional[int] = None
    usage_count: Optional[int] = None

    average_sales: Optional[int] = None
    operating_cost: Optional[int] = None
    food_cost: Optional[int] = None
    employee_cost: Optional[int] = None
    rental_cost: Optional[int] = None
    tax_cost: Optional[int] = None
    family_employee_cost: Optional[int] = None
    ceo_cost: Optional[int] = None
    etc_cost: Optional[int] = None
    average_profit: Optional[int] = None

    avg_profit_per_mon: Optional[float] = None
    avg_profit_per_tue: Optional[float] = None
    avg_profit_per_wed: Optional[float] = None
    avg_profit_per_thu: Optional[float] = None
    avg_profit_per_fri: Optional[float] = None
    avg_profit_per_sat: Optional[float] = None
    avg_profit_per_sun: Optional[float] = None

    avg_profit_per_06_09: Optional[float] = None
    avg_profit_per_09_12: Optional[float] = None
    avg_profit_per_12_15: Optional[float] = None
    avg_profit_per_15_18: Optional[float] = None
    avg_profit_per_18_21: Optional[float] = None
    avg_profit_per_21_24: Optional[float] = None
    avg_profit_per_24_06: Optional[float] = None

    avg_client_per_m_20: Optional[float] = None
    avg_client_per_m_30: Optional[float] = None
    avg_client_per_m_40: Optional[float] = None
    avg_client_per_m_50: Optional[float] = None
    avg_client_per_m_60: Optional[float] = None
    avg_client_per_f_20: Optional[float] = None
    avg_client_per_f_30: Optional[float] = None
    avg_client_per_f_40: Optional[float] = None
    avg_client_per_f_50: Optional[float] = None
    avg_client_per_f_60: Optional[float] = None

    top_menu_1: str = None
    top_menu_2: str = None
    top_menu_3: str = None
    top_menu_4: str = None
    top_menu_5: str = None

    class Config:
        from_attributes = True


class CommercialDistrictOutput(BaseModel):
    commercial_district_id: int

    city_name: str
    district_name: str
    sub_district_name: str

    biz_main_category_name: str
    biz_sub_category_name: str
    biz_detail_category_name: str

    national_density: Optional[float] = None
    city_density: Optional[float] = None
    district_density: Optional[float] = None
    sub_district_density: Optional[float] = None

    market_size: Optional[int] = None

    average_payment: Optional[int] = None
    usage_count: Optional[int] = None

    average_sales: Optional[int] = None
    operating_cost: Optional[int] = None
    food_cost: Optional[int] = None
    employee_cost: Optional[int] = None
    rental_cost: Optional[int] = None
    tax_cost: Optional[int] = None
    family_employee_cost: Optional[int] = None
    ceo_cost: Optional[int] = None
    etc_cost: Optional[int] = None
    average_profit: Optional[int] = None

    avg_profit_per_mon: Optional[float] = None
    avg_profit_per_tue: Optional[float] = None
    avg_profit_per_wed: Optional[float] = None
    avg_profit_per_thu: Optional[float] = None
    avg_profit_per_fri: Optional[float] = None
    avg_profit_per_sat: Optional[float] = None
    avg_profit_per_sun: Optional[float] = None

    avg_profit_per_06_09: Optional[float] = None
    avg_profit_per_09_12: Optional[float] = None
    avg_profit_per_12_15: Optional[float] = None
    avg_profit_per_15_18: Optional[float] = None
    avg_profit_per_18_21: Optional[float] = None
    avg_profit_per_21_24: Optional[float] = None
    avg_profit_per_24_06: Optional[float] = None

    avg_client_per_m_20: Optional[float] = None
    avg_client_per_m_30: Optional[float] = None
    avg_client_per_m_40: Optional[float] = None
    avg_client_per_m_50: Optional[float] = None
    avg_client_per_m_60: Optional[float] = None
    avg_client_per_f_20: Optional[float] = None
    avg_client_per_f_30: Optional[float] = None
    avg_client_per_f_40: Optional[float] = None
    avg_client_per_f_50: Optional[float] = None
    avg_client_per_f_60: Optional[float] = None

    top_menu_1: Optional[str] = None
    top_menu_2: Optional[str] = None
    top_menu_3: Optional[str] = None
    top_menu_4: Optional[str] = None
    top_menu_5: Optional[str] = None

    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class CommercialStatisticsData(BaseModel):
    market_size: Optional[CommercialStatistics] = None
    average_sales: Optional[CommercialStatistics] = None
    average_payment: Optional[CommercialStatistics] = None
    usage_count: Optional[CommercialStatistics] = None
    sub_district_density: Optional[CommercialStatistics] = None

    class Config:
        from_attributes = True


class CommercialStatisticsOutput(BaseModel):
    commercial_district_data: CommercialDistrictOutput
    statistics_data: Optional[CommercialStatisticsData] = None

    class Config:
        from_attributes = True
