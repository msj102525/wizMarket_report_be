from typing import Optional
from pydantic import BaseModel, Field
from datetime import date, datetime


class Report(BaseModel):
    store_business_number: str  # VARCHAR(100)
    city_name: Optional[str] = None  # VARCHAR(50)
    district_name: Optional[str] = None  # VARCHAR(50)
    sub_district_name: Optional[str] = None  # VARCHAR(50)
    detail_category_name: str  # VARCHAR(100)
    store_name: str  # VARCHAR(255)
    road_name: Optional[str] = None  # VARCHAR(255)
    building_name: Optional[str] = None  # VARCHAR(255)
    floor_info: Optional[str] = None  # VARCHAR(10)
    latitude: Optional[float] = None  # DOUBLE
    longitude: Optional[float] = None  # DOUBLE
    detail_category_top1_ordered_menu: Optional[str] = None  # VARCHAR(50)
    detail_category_top2_ordered_menu: Optional[str] = None  # VARCHAR(50)
    detail_category_top3_ordered_menu: Optional[str] = None  # VARCHAR(50)
    detail_category_top4_ordered_menu: Optional[str] = None  # VARCHAR(50)
    detail_category_top5_ordered_menu: Optional[str] = None  # VARCHAR(50)
    loc_info_j_score_average: Optional[float] = None  # FLOAT
    population_total: Optional[int] = None  # INT
    population_male_percent: Optional[float] = None  # FLOAT
    population_female_percent: Optional[float] = None  # FLOAT
    population_age_10_under: Optional[int] = None  # INT
    population_age_10s: Optional[int] = None  # INT
    population_age_20s: Optional[int] = None  # INT
    population_age_30s: Optional[int] = None  # INT
    population_age_40s: Optional[int] = None  # INT
    population_age_50s: Optional[int] = None  # INT
    population_age_60_over: Optional[int] = None  # INT
    loc_info_resident_k: Optional[int] = None  # INT
    loc_info_work_pop_k: Optional[int] = None  # INT
    loc_info_move_pop_k: Optional[int] = None  # INT
    loc_info_shop_k: Optional[int] = None  # INT
    loc_info_income_won: Optional[int] = None  # INT
    loc_info_resident_j_score: Optional[float] = None  # FLOAT
    loc_info_work_pop_j_score: Optional[float] = None  # FLOAT
    loc_info_move_pop_j_score: Optional[float] = None  # FLOAT
    loc_info_shop_j_score: Optional[float] = None  # FLOAT
    loc_info_income_j_score: Optional[float] = None  # FLOAT
    loc_info_mz_population_j_score: Optional[float] = None  # FLOAT
    loc_info_average_spend_j_score: Optional[float] = None  # FLOAT
    loc_info_average_sales_j_score: Optional[float] = None  # FLOAT
    loc_info_house_j_score: Optional[float] = None  # FLOAT
    loc_info_resident: Optional[int] = None  # INT
    loc_info_work_pop: Optional[int] = None  # INT
    loc_info_resident_percent: Optional[float] = None  # FLOAT
    loc_info_work_pop_percent: Optional[float] = None  # FLOAT
    loc_info_move_pop: Optional[int] = None  # INT
    loc_info_city_move_pop: Optional[int] = None  # INT
    commercial_district_j_score_average: Optional[float] = None  # FLOAT
    commercial_district_food_business_count: Optional[int] = None  # INT
    commercial_district_healthcare_business_count: Optional[int] = None  # INT
    commercial_district_education_business_count: Optional[int] = None  # INT
    commercial_district_entertainment_business_count: Optional[int] = None  # INT
    commercial_district_lifestyle_business_count: Optional[int] = None  # INT
    commercial_district_retail_business_count: Optional[int] = None  # INT
    commercial_district_market_size_j_score: Optional[float] = None  # FLOAT
    commercial_district_average_sales_j_score: Optional[float] = None  # FLOAT
    commercial_district_usage_count_j_score: Optional[float] = None  # FLOAT
    commercial_district_sub_district_density_j_score: Optional[float] = None  # FLOAT
    commercial_district_average_payment_j_score: Optional[float] = None  # FLOAT
    commercial_district_average_sales_percent_mon: Optional[float] = None  # FLOAT
    commercial_district_average_sales_percent_tue: Optional[float] = None  # FLOAT
    commercial_district_average_sales_percent_wed: Optional[float] = None  # FLOAT
    commercial_district_average_sales_percent_thu: Optional[float] = None  # FLOAT
    commercial_district_average_sales_percent_fri: Optional[float] = None  # FLOAT
    commercial_district_average_sales_percent_sat: Optional[float] = None  # FLOAT
    commercial_district_average_sales_percent_sun: Optional[float] = None  # FLOAT
    commercial_district_average_sales_percent_06_09: Optional[float] = None  # FLOAT
    commercial_district_average_sales_percent_09_12: Optional[float] = None  # FLOAT
    commercial_district_average_sales_percent_12_15: Optional[float] = None  # FLOAT
    commercial_district_average_sales_percent_15_18: Optional[float] = None  # FLOAT
    commercial_district_average_sales_percent_18_21: Optional[float] = None  # FLOAT
    commercial_district_average_sales_percent_21_24: Optional[float] = None  # FLOAT
    # VARCHAR(100)
    commercial_district_detail_category_average_sales_top1_info: Optional[str] = None
    commercial_district_detail_category_average_sales_top2_info: Optional[str] = None
    commercial_district_detail_category_average_sales_top3_info: Optional[str] = None
    commercial_district_detail_category_average_sales_top4_info: Optional[str] = None
    commercial_district_detail_category_average_sales_top5_info: Optional[str] = None
    rising_business_national_rising_sales_top1_info: Optional[str] = None
    rising_business_national_rising_sales_top2_info: Optional[str] = None
    rising_business_national_rising_sales_top3_info: Optional[str] = None
    rising_business_national_rising_sales_top4_info: Optional[str] = None
    rising_business_national_rising_sales_top5_info: Optional[str] = None
    rising_business_sub_district_rising_sales_top1_info: Optional[str] = None
    rising_business_sub_district_rising_sales_top2_info: Optional[str] = None
    rising_business_sub_district_rising_sales_top3_info: Optional[str] = None
    # VARCHAR(100)
    loc_info_data_ref_date: Optional[date] = None  # DATE
    nice_biz_map_data_ref_date: Optional[date] = None  # DATE
    population_data_ref_date: Optional[date] = None  # DATE
    created_at: datetime  # DATETIME
    updated_at: datetime  # DATETIME

    class Config:
        from_attributes = True


class LocalStoreImage(BaseModel):
    local_store_image_id: int
    store_business_number: str
    local_store_image_url: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


##########################################################################################
# 리덕스로 관리할 정보들
class LocalStoreRedux(BaseModel):
    city_name: str
    district_name: str
    sub_district_name: str
    detail_category_name: str
    loc_info_data_ref_date: Optional[date] = None
    nice_biz_map_data_ref_date: Optional[date] = None
    population_data_ref_date: Optional[date] = None

    def __init__(self, **data):
        super().__init__(**data)
        if self.loc_info_data_ref_date is None:
            self.loc_info_data_ref_date = date(2024, 1, 1)

        if self.nice_biz_map_data_ref_date is None:
            self.nice_biz_map_data_ref_date = date(2024, 1, 1)

        if self.population_data_ref_date is None:
            self.population_data_ref_date = date(2024, 1, 1)

    class Config:
        from_attributes = True


# 매장 기본 정보
class LocalStoreBasicInfo(BaseModel):
    store_name: str
    road_name: Optional[str] = None
    building_name: Optional[str] = None
    floor_info: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None

    local_store_image_url: Optional[str] = None

    class Config:
        from_attributes = True

    def __init__(self, **data):
        super().__init__(**data)
        if self.latitude is None:
            self.latitude = "37.5543836"  # 남산 위도

        if self.longitude is None:
            self.longitude = "126.9814663"  # 남산 경도

        if self.local_store_image_url is None:
            self.local_store_image_url = (
                "/static/images/report/basic_store_img.png"  # 기본 이미지
            )


class WeatherInfo(BaseModel):
    icon: str
    temp: float

    class Config:
        from_attributes = True


class AqiInfo(BaseModel):
    aqi: int
    description: str

    class Config:
        from_attributes = True


class LocalStoreInfoWeaterInfoOutput(BaseModel):
    localStoreInfo: LocalStoreBasicInfo
    weatherInfo: WeatherInfo
    aqi_info: AqiInfo
    format_current_datetime: str

    class Config:
        from_attributes = True


#################################################################
# 매장별 top5 메뉴
class LocalStoreTop5Menu(BaseModel):
    city_name: str
    district_name: str
    sub_district_name: str
    detail_category_name: str
    detail_category_top1_ordered_menu: Optional[str] = None
    detail_category_top2_ordered_menu: Optional[str] = None
    detail_category_top3_ordered_menu: Optional[str] = None
    detail_category_top4_ordered_menu: Optional[str] = None
    detail_category_top5_ordered_menu: Optional[str] = None

    def __init__(self, **data):
        super().__init__(**data)

        def set_default_if_empty(value):
            return value if value and value != ",,," else "-"

        self.detail_category_top1_ordered_menu = set_default_if_empty(
            self.detail_category_top1_ordered_menu
        )
        self.detail_category_top2_ordered_menu = set_default_if_empty(
            self.detail_category_top2_ordered_menu
        )
        self.detail_category_top3_ordered_menu = set_default_if_empty(
            self.detail_category_top3_ordered_menu
        )
        self.detail_category_top4_ordered_menu = set_default_if_empty(
            self.detail_category_top4_ordered_menu
        )
        self.detail_category_top5_ordered_menu = set_default_if_empty(
            self.detail_category_top5_ordered_menu
        )

    class Config:
        from_attributes = True


class LocalStoreTop5MenuAdviceOutput(BaseModel):
    local_store_top5_orderd_menu: LocalStoreTop5Menu
    rising_menu_advice: Optional[str] = None

    class Config:
        from_attributes = True


#######################################################################
# 읍/면/동 소분류 업종 상권분석
class LocalStoreCommercialDistrict(BaseModel):

    class Config:
        from_attributes = True


#######################################################################
# 동별 인구 분포
class LocalStorePopulationDataOutPut(BaseModel):
    population_total: Optional[int] = None
    population_male_percent: Optional[float] = None
    population_female_percent: Optional[float] = None
    population_age_10_under: Optional[int] = None
    population_age_10s: Optional[int] = None
    population_age_20s: Optional[int] = None
    population_age_30s: Optional[int] = None
    population_age_40s: Optional[int] = None
    population_age_50s: Optional[int] = None
    population_age_60_over: Optional[int] = None

    loc_info_resident_k: Optional[float] = None
    loc_info_work_pop_k: Optional[float] = None
    loc_info_move_pop_k: Optional[float] = None
    loc_info_shop_k: Optional[float] = None
    loc_info_income_won: Optional[int] = None

    loc_info_resident_j_score: Optional[float] = None
    loc_info_work_pop_j_score: Optional[float] = None
    loc_info_move_pop_j_score: Optional[float] = None
    loc_info_shop_j_score: Optional[float] = None
    loc_info_income_j_score: Optional[float] = None

    class Config:
        from_attributes = True


#######################################################################


# 입지분석 읍/면/동 소분류 J_Score 가중치 평균 합
class LocalStoreLIJSWeightedAverage(BaseModel):
    loc_info_j_score_average: Optional[float] = None

    class Config:
        from_attributes = True


#######################################################################


# 매장별 입지정보 J_Score
class LocalStoreLocInfoJscoreData(BaseModel):
    city_name: str
    district_name: str
    sub_district_name: str
    detail_category_name: str
    store_name: str

    loc_info_resident_k: Optional[float] = None
    loc_info_move_pop_k: Optional[float] = None
    loc_info_shop_k: Optional[float] = None
    loc_info_income_won: Optional[int] = None
    loc_info_average_sales_k: Optional[float] = None
    loc_info_average_spend_k: Optional[float] = None
    loc_info_house_k: Optional[float] = None

    loc_info_resident_j_score: Optional[float] = None
    loc_info_move_pop_j_score: Optional[float] = None
    loc_info_shop_j_score: Optional[float] = None
    loc_info_income_j_score: Optional[float] = None
    loc_info_average_spend_j_score: Optional[float] = None
    loc_info_average_sales_j_score: Optional[float] = None
    loc_info_house_j_score: Optional[float] = None
    population_mz_population_j_score: Optional[float] = None

    population_total: Optional[int] = None
    population_male_percent: Optional[float] = None
    population_female_percent: Optional[float] = None
    population_age_10_under: Optional[int] = None
    population_age_10s: Optional[int] = None
    population_age_20s: Optional[int] = None
    population_age_30s: Optional[int] = None
    population_age_40s: Optional[int] = None
    population_age_50s: Optional[int] = None
    population_age_60_over: Optional[int] = None

    def __init__(self, **data):
        super().__init__(**data)
        if self.loc_info_resident_j_score is None:
            self.loc_info_resident_j_score = 0.0

        if self.population_mz_population_j_score is None:
            self.population_mz_population_j_score = 0.0

        if self.loc_info_move_pop_j_score is None:
            self.loc_info_move_pop_j_score = 0.0

        if self.loc_info_shop_j_score is None:
            self.loc_info_shop_j_score = 0.0

        if self.loc_info_income_j_score is None:
            self.loc_info_income_j_score = 0.0

        if self.loc_info_average_spend_j_score is None:
            self.loc_info_average_spend_j_score = 0.0

        if self.loc_info_average_sales_j_score is None:
            self.loc_info_average_sales_j_score = 0.0

        if self.loc_info_house_j_score is None:
            self.loc_info_house_j_score = 0.0

        if self.population_total is None:
            self.population_total = 0

        if self.population_male_percent is None:
            self.population_male_percent = 0.0

        if self.population_female_percent is None:
            self.population_female_percent = 0.0

        if self.population_age_10_under is None:
            self.population_age_10_under = 0

        if self.population_age_10s is None:
            self.population_age_10s = 0

        if self.population_age_20s is None:
            self.population_age_20s = 0

        if self.population_age_30s is None:
            self.population_age_30s = 0

        if self.population_age_40s is None:
            self.population_age_40s = 0

        if self.population_age_50s is None:
            self.population_age_50s = 0

        if self.population_age_60_over is None:
            self.population_age_60_over = 0

    class Config:
        from_attributes = True


class LocalStoreLocInfoJscoreDataOutput(BaseModel):
    local_store_loc_info_j_score_data: LocalStoreLocInfoJscoreData
    loc_info_advice: Optional[str] = None

    class Config:
        from_attributes = True


#######################################################################


# 읍/면/동 입지정보 주거인구/직장인구
class LocalStoreResidentWorkPopData(BaseModel):
    loc_info_resident: Optional[int] = None
    loc_info_work_pop: Optional[int] = None
    loc_info_resident_percent: Optional[float] = None
    loc_info_work_pop_percent: Optional[float] = None

    def __init__(self, **data):
        super().__init__(**data)
        if self.loc_info_resident is None:
            self.loc_info_resident = 0

        if self.loc_info_work_pop is None:
            self.loc_info_work_pop = 0

        if self.loc_info_resident_percent is None:
            self.loc_info_resident_percent = 0.0

        if self.loc_info_work_pop_percent is None:
            self.loc_info_work_pop_percent = 0.0

    class Config:
        from_attributes = True


#######################################################################


# 상권분석 읍/면/동 소분류 J_Score 가중치 평균 합
class LocalStoreCDJSWeightedAverage(BaseModel):
    commercial_district_j_score_average: Optional[float] = None

    def __init__(self, **data):
        super().__init__(**data)
        if self.commercial_district_j_score_average is None:
            self.commercial_district_j_score_average = 0

    class Config:
        from_attributes = True


#######################################################################


# 읍/면/동 입지정보 유동인구, 시/도 평균 유동인구
class LocalStoreMovePopData(BaseModel):
    loc_info_move_pop_j_score: Optional[float] = None
    loc_info_move_pop: Optional[int] = None
    loc_info_city_move_pop: Optional[int] = None

    def __init__(self, **data):
        super().__init__(**data)
        if self.loc_info_move_pop_j_score is None:
            self.loc_info_move_pop_j_score = 0.0

        if self.loc_info_move_pop is None:
            self.loc_info_move_pop = 0

        if self.loc_info_city_move_pop is None:
            self.loc_info_city_move_pop = 0

    class Config:
        from_attributes = True


#######################################################################


# 상권분석 읍/면/동 대분류 갯수
class LocalStoreMainCategoryCount(BaseModel):
    commercial_district_food_business_count: Optional[int] = None
    commercial_district_healthcare_business_count: Optional[int] = None
    commercial_district_education_business_count: Optional[int] = None
    commercial_district_entertainment_business_count: Optional[int] = None
    commercial_district_lifestyle_business_count: Optional[int] = None
    commercial_district_retail_business_count: Optional[int] = None

    def __init__(self, **data):
        super().__init__(**data)
        if self.commercial_district_food_business_count is None:
            self.commercial_district_food_business_count = 0

        if self.commercial_district_healthcare_business_count is None:
            self.commercial_district_healthcare_business_count = 0

        if self.commercial_district_education_business_count is None:
            self.commercial_district_education_business_count = 0

        if self.commercial_district_entertainment_business_count is None:
            self.commercial_district_entertainment_business_count = 0

        if self.commercial_district_lifestyle_business_count is None:
            self.commercial_district_lifestyle_business_count = 0

        if self.commercial_district_retail_business_count is None:
            self.commercial_district_retail_business_count = 0

    class Config:
        from_attributes = True


#######################################################################


# 상권분석 읍/면/동 소분류 J_Score 평균
class LocalStoreCommercialDistrictJscoreAverage(BaseModel):
    commercial_district_market_size_j_socre: Optional[float] = None
    commercial_district_average_sales_j_socre: Optional[float] = None
    commercial_district_usage_count_j_socre: Optional[float] = None
    commercial_district_sub_district_density_j_socre: Optional[float] = None
    commercial_district_sub_average_payment_j_socre: Optional[float] = None

    def __init__(self, **data):
        super().__init__(**data)
        if self.commercial_district_market_size_j_socre is None:
            self.commercial_district_market_size_j_socre = 0.0

        if self.commercial_district_average_sales_j_socre is None:
            self.commercial_district_average_sales_j_socre = 0.0

        if self.commercial_district_usage_count_j_socre is None:
            self.commercial_district_usage_count_j_socre = 0.0

        if self.commercial_district_sub_district_density_j_socre is None:
            self.commercial_district_sub_district_density_j_socre = 0.0

        if self.commercial_district_sub_average_payment_j_socre is None:
            self.commercial_district_sub_average_payment_j_socre = 0.0

    class Config:
        from_attributes = True


#######################################################################


# 매장 상권분석 동별 소분류별 요일 매출 비중
class LocalStoreCDWeekdayAverageSalesPercent(BaseModel):
    commercial_district_average_sales_percent_mon: Optional[float] = 0.0
    commercial_district_average_sales_percent_tue: Optional[float] = 0.0
    commercial_district_average_sales_percent_wed: Optional[float] = 0.0
    commercial_district_average_sales_percent_thu: Optional[float] = 0.0
    commercial_district_average_sales_percent_fri: Optional[float] = 0.0
    commercial_district_average_sales_percent_sat: Optional[float] = 0.0
    commercial_district_average_sales_percent_sun: Optional[float] = 0.0

    def __init__(self, **data):
        super().__init__(**data)
        if self.commercial_district_average_sales_percent_mon is None:
            self.commercial_district_average_sales_percent_mon = 0.0

        if self.commercial_district_average_sales_percent_tue is None:
            self.commercial_district_average_sales_percent_tue = 0.0

        if self.commercial_district_average_sales_percent_wed is None:
            self.commercial_district_average_sales_percent_wed = 0.0

        if self.commercial_district_average_sales_percent_thu is None:
            self.commercial_district_average_sales_percent_thu = 0.0

        if self.commercial_district_average_sales_percent_fri is None:
            self.commercial_district_average_sales_percent_fri = 0.0

        if self.commercial_district_average_sales_percent_fri is None:
            self.commercial_district_average_sales_percent_fri = 0.0

        if self.commercial_district_average_sales_percent_sun is None:
            self.commercial_district_average_sales_percent_sun = 0.0

    class Config:
        from_attributes = True


# 매장 상권분석 동별 소분류별 시간대 매출 비중
class LocalStoreCDTiemAverageSalesPercent(BaseModel):
    commercial_district_average_sales_percent_06_09: Optional[float] = 0.0
    commercial_district_average_sales_percent_09_12: Optional[float] = 0.0
    commercial_district_average_sales_percent_12_15: Optional[float] = 0.0
    commercial_district_average_sales_percent_15_18: Optional[float] = 0.0
    commercial_district_average_sales_percent_18_21: Optional[float] = 0.0
    commercial_district_average_sales_percent_21_24: Optional[float] = 0.0

    def __init__(self, **data):
        super().__init__(**data)
        if self.commercial_district_average_sales_percent_06_09 is None:
            self.commercial_district_average_sales_percent_06_09 = 0.0

        if self.commercial_district_average_sales_percent_09_12 is None:
            self.commercial_district_average_sales_percent_09_12 = 0.0

        if self.commercial_district_average_sales_percent_12_15 is None:
            self.commercial_district_average_sales_percent_12_15 = 0.0

        if self.commercial_district_average_sales_percent_15_18 is None:
            self.commercial_district_average_sales_percent_15_18 = 0.0

        if self.commercial_district_average_sales_percent_18_21 is None:
            self.commercial_district_average_sales_percent_18_21 = 0.0

        if self.commercial_district_average_sales_percent_21_24 is None:
            self.commercial_district_average_sales_percent_21_24 = 0.0

    class Config:
        from_attributes = True


#######################################################################
# 상권 분석 시/군/구에서 매핑된 소분류들 매출합 TOP5
class LocalStoreCDDistrictAverageSalesTop5(BaseModel):
    commercial_district_detail_category_average_sales_top1_info: Optional[str] = ","
    commercial_district_detail_category_average_sales_top2_info: Optional[str] = ","
    commercial_district_detail_category_average_sales_top3_info: Optional[str] = ","
    commercial_district_detail_category_average_sales_top4_info: Optional[str] = ","
    commercial_district_detail_category_average_sales_top5_info: Optional[str] = ","

    class Config:
        from_attributes = True


#######################################################################


# 상권 분석 시/군/구에서 매핑된 소분류들 매출합 TOP5
class LocalStoreRisingBusinessNTop5SDTop3(BaseModel):
    sub_district_name: str
    store_name: str
    nice_biz_map_data_ref_date: Optional[date] = None

    rising_business_national_rising_sales_top1_info: Optional[str] = None
    rising_business_national_rising_sales_top2_info: Optional[str] = None
    rising_business_national_rising_sales_top3_info: Optional[str] = None
    rising_business_national_rising_sales_top4_info: Optional[str] = None
    rising_business_national_rising_sales_top5_info: Optional[str] = None

    rising_business_sub_district_rising_sales_top1_info: Optional[str] = None
    rising_business_sub_district_rising_sales_top2_info: Optional[str] = None
    rising_business_sub_district_rising_sales_top3_info: Optional[str] = None

    def __init__(self, **data):
        super().__init__(**data)

        # 기본 값 설정 함수
        def set_default_if_empty(value):
            return value if value and value != ",,," else "-,-,-,0.0"

        # 필드 값 검사 및 기본 값 설정
        self.rising_business_national_rising_sales_top1_info = set_default_if_empty(
            self.rising_business_national_rising_sales_top1_info
        )
        self.rising_business_national_rising_sales_top2_info = set_default_if_empty(
            self.rising_business_national_rising_sales_top2_info
        )
        self.rising_business_national_rising_sales_top3_info = set_default_if_empty(
            self.rising_business_national_rising_sales_top3_info
        )
        self.rising_business_national_rising_sales_top4_info = set_default_if_empty(
            self.rising_business_national_rising_sales_top4_info
        )
        self.rising_business_national_rising_sales_top5_info = set_default_if_empty(
            self.rising_business_national_rising_sales_top5_info
        )

        self.rising_business_sub_district_rising_sales_top1_info = set_default_if_empty(
            self.rising_business_sub_district_rising_sales_top1_info
        )
        self.rising_business_sub_district_rising_sales_top2_info = set_default_if_empty(
            self.rising_business_sub_district_rising_sales_top2_info
        )
        self.rising_business_sub_district_rising_sales_top3_info = set_default_if_empty(
            self.rising_business_sub_district_rising_sales_top3_info
        )

    class Config:
        from_attributes = True

    class Config:
        from_attributes = True


#######################################################################


# 상권분석 읍/면/동 소분류 상권분석
class LocalStoreCDCommercialDistrict(BaseModel):
    commercial_district_national_density_average: Optional[float]
    commercial_district_sub_district_density_average: Optional[float]
    commercial_district_national_average_sales: Optional[int]
    commercial_district_sub_district_average_sales: Optional[int]
    commercial_district_national_average_payment: Optional[int]
    commercial_district_sub_district_average_payment: Optional[int]
    commercial_district_national_usage_count: Optional[int]
    commercial_district_sub_district_usage_count: Optional[int]

    commercial_district_average_sales_max_percent_weekday: Optional[str]
    commercial_district_average_sales_min_percent_weekday: Optional[str]
    commercial_district_average_sales_max_percent_time: Optional[str]
    commercial_district_average_sales_max_percent_client_top1: Optional[str]
    commercial_district_average_sales_max_percent_client_top2: Optional[str]

    def __init__(self, **data):
        super().__init__(**data)
        if self.commercial_district_national_density_average is None:
            self.commercial_district_national_density_average = 0.0

        if self.commercial_district_sub_district_density_average is None:
            self.commercial_district_sub_district_density_average = 0.0

        if self.commercial_district_national_average_sales is None:
            self.commercial_district_national_average_sales = 0.0

        if self.commercial_district_sub_district_average_sales is None:
            self.commercial_district_sub_district_average_sales = 0.0

        if self.commercial_district_national_average_payment is None:
            self.commercial_district_national_average_payment = 0.0

        if self.commercial_district_sub_district_average_payment is None:
            self.commercial_district_sub_district_average_payment = 0.0

        if self.commercial_district_national_usage_count is None:
            self.commercial_district_national_usage_count = 0.0

        if self.commercial_district_sub_district_usage_count is None:
            self.commercial_district_sub_district_usage_count = 0.0


#######################################################################
#######################################################################
#######################################################################
#######################################################################


class FilterRequest(BaseModel):
    city: Optional[int] = None  # 기본값 None을 설정
    district: Optional[int] = None
    subDistrict: Optional[int] = None
    storeName: Optional[str] = None
    matchType: Optional[str] = "="  # = 또는 LIKE 검색
    mainCategory: Optional[str] = None
    subCategory: Optional[str] = None
    detailCategory: Optional[str] = None
    page: Optional[int] = 1  # 페이지 번호 (기본값 1)
    page_size: Optional[int] = 20  # 페이지 크기 (기본값 20)


# 매장별 읍/면/동 id 조회
class LocalStorePopulationData(BaseModel):
    store_business_number: str
    population_total: int
    population_male_percent: float
    population_female_percent: float
    population_age_10_under: int
    population_age_10s: int
    population_age_20s: int
    population_age_30s: int
    population_age_40s: int
    population_age_50s: int
    population_age_60_over: int
    population_date_ref_date: date

    class Config:
        from_attributes = True


# 매장별 입지정보
class LocalStoreLocInfoData(BaseModel):
    store_business_number: str
    loc_info_resident_k: Optional[float] = 0.0
    loc_info_work_pop_k: Optional[float] = 0.0
    loc_info_move_pop_k: Optional[float] = 0.0
    loc_info_shop_k: Optional[float] = 0.0
    loc_info_income_won: Optional[int] = 0
    loc_info_data_ref_date: date

    class Config:
        from_attributes = True


# 매장 소분류 비즈맵 매핑 대표 id
class LocalStoreMappingSubDistrictDetailCategoryId(BaseModel):
    store_business_number: str
    sub_district_id: int
    detail_category_id: Optional[int] = 3  # 3: 비즈맵 소분류 없음 default 값

    class Config:
        from_attributes = True


#######################################################################
#######################################################################
#######################################################################
#######################################################################


# gpt 대답 생성용
class GPTAnswer(BaseModel):
    gpt_answer: str

    class Config:
        from_attributes = True
