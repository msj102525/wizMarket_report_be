DROP TABLE IF EXISTS `LOCAL_STORE_IMAGE`;

DROP TABLE IF EXISTS `REPORT`;

DROP TABLE IF EXISTS `SERVICE_DETAIL_CATEGORY_MAPPING`;

DROP TABLE IF EXISTS `BIZ_DETAIL_CATEGORY_CONTENT`;

DROP TABLE IF EXISTS `BIZ_DETAIL_CATEGORY_CONTENT_IMAGE`;

DROP TABLE IF EXISTS `LOCAL_STORE_CONTENT`;

DROP TABLE IF EXISTS `LOCAL_STORE_CONTENT_IMAGE`;

DROP TABLE IF EXISTS `ADS`;

DROP TABLE IF EXISTS `ADS_IMAGE`;

CREATE TABLE
    `REPORT` (
        `STORE_BUSINESS_NUMBER` VARCHAR(100) NOT NULL COMMENT 'PK_RID',
        `CITY_NAME` VARCHAR(50) NULL COMMENT '시/도 명',
        `DISTRICT_NAME` VARCHAR(50) NULL COMMENT '시/군/구 명',
        `SUB_DISTRICT_NAME` VARCHAR(50) NULL COMMENT '읍/면/동 명',
        `DETAIL_CATEGORY_NAME` VARCHAR(100) NULL COMMENT '상권업종소분류명',
        `STORE_NAME` VARCHAR(255) NULL COMMENT '상호명',
        `ROAD_NAME` VARCHAR(255) NULL COMMENT '도로명',
        `BUILDING_NAME` VARCHAR(255) NULL COMMENT '건물명',
        `FLOOR_INFO` VARCHAR(10) NULL COMMENT '층정보',
        `LATITUDE` DOUBLE NULL COMMENT '위도',
        `LONGITUDE` DOUBLE NULL COMMENT '경도',
        `BUSINESS_AREA_CATEGORY_ID` INT NULL COMMENT '상권정보분류ID',
        `BIZ_DETAIL_CATEGORY_REP_NAME` VARCHAR(50) NULL COMMENT '비즈맵 대표값 소분류 명',
        `BIZ_MAIN_CATEGORY_ID` INT NULL COMMENT '비즈맵 대분류 ID',
        `BIZ_SUB_CATEGORY_ID` INT NULL COMMENT '비즈맵 중분류 ID',
        `DETAIL_CATEGORY_TOP1_ORDERED_MENU` VARCHAR(50) NULL COMMENT '소분류 주문 많은 TOP1 메뉴',
        `DETAIL_CATEGORY_TOP2_ORDERED_MENU` VARCHAR(50) NULL COMMENT '소분류 주문 많은 TOP2 메뉴',
        `DETAIL_CATEGORY_TOP3_ORDERED_MENU` VARCHAR(50) NULL COMMENT '소분류 주문 많은 TOP3 메뉴',
        `DETAIL_CATEGORY_TOP4_ORDERED_MENU` VARCHAR(50) NULL COMMENT '소분류 주문 많은 TOP4 메뉴',
        `DETAIL_CATEGORY_TOP5_ORDERED_MENU` VARCHAR(50) NULL COMMENT '소분류 주문 많은 TOP5 메뉴',
        `LOC_INFO_J_SCORE_AVERAGE` FLOAT NULL COMMENT '입지분석 J_SCORE 가중치 평균(MZ인구, 업소수, 유동인구, 주거인구, 세대수, 소득, 소비,매출,직장인구)',
        `POPULATION_TOTAL` INT NULL COMMENT '총 인구 수',
        `POPULATION_MALE_PERCENT` FLOAT NULL COMMENT '인구 분포 남성 비율',
        `POPULATION_FEMALE_PERCENT` FLOAT NULL COMMENT '인구 분포 여성 비율',
        `POPULATION_AGE_10_UNDER` INT NULL COMMENT '인구 분포 10대 미만',
        `POPULATION_AGE_10S` INT NULL COMMENT '인구 분포 10대',
        `POPULATION_AGE_20S` INT NULL COMMENT '인구 분포 20대',
        `POPULATION_AGE_30S` INT NULL COMMENT '인구 분포 30대',
        `POPULATION_AGE_40S` INT NULL COMMENT '인구 분포 40대',
        `POPULATION_AGE_50S` INT NULL COMMENT '인구 분포 50대',
        `POPULATION_AGE_60_OVER` INT NULL COMMENT '인구 분포 60대 이상',
        `LOC_INFO_RESIDENT_K` FLOAT NULL COMMENT '입지 분석 주거인구 수 (K)',
        `LOC_INFO_WORK_POP_K` FLOAT NULL COMMENT '입지 분석 직장인구 수 (K)',
        `LOC_INFO_MOVE_POP_K` FLOAT NULL COMMENT '입지 분석 유동인구 수 (K)',
        `LOC_INFO_SHOP_K` FLOAT NULL COMMENT '입지 분석 업소수 (K)',
        `LOC_INFO_AVERAGE_SALES_K` FLOAT NULL COMMENT '입지 분석 평균 매출 (K)',
        `LOC_INFO_AVERAGE_SPEND_K` FLOAT NULL COMMENT '입지 분석 평균 소비 (K)',
        `LOC_INFO_HOUSE_K` FLOAT NULL COMMENT '입지 분석 세대수 (K)',
        `LOC_INFO_INCOME_WON` INT NULL COMMENT '입지 분석 소득 (만원)',
        `LOC_INFO_RESIDENT_J_SCORE` FLOAT NULL COMMENT '입지 분석 주거인구 J_SCORE',
        `LOC_INFO_WORK_POP_J_SCORE` FLOAT NULL COMMENT '입지 분석 직장인구 J_SCORE',
        `LOC_INFO_MOVE_POP_J_SCORE` FLOAT NULL COMMENT '입지 분석 유동인구 J_SCORE',
        `LOC_INFO_SHOP_J_SCORE` FLOAT NULL COMMENT '입지 분석 업소수 J_SCORE',
        `LOC_INFO_INCOME_J_SCORE` FLOAT NULL COMMENT '입지 분석 소득 J_SCORE',
        `LOC_INFO_MZ_POPULATION_J_SCORE` FLOAT NULL COMMENT '입지분석 MZ인구 J_SCORE',
        `LOC_INFO_AVERAGE_SPEND_J_SCORE` FLOAT NULL COMMENT '입지분석 평균 소비 J_SCORE',
        `LOC_INFO_AVERAGE_SALES_J_SCORE` FLOAT NULL COMMENT '입지분석 매장평균매출 J_SCORE',
        `LOC_INFO_HOUSE_J_SCORE` FLOAT NULL COMMENT '입지분석 세대수 J_SCORE',
        `LOC_INFO_RESIDENT` INT NULL COMMENT '읍/면/동 주거인구 수',
        `LOC_INFO_WORK_POP` INT NULL COMMENT '읍/면/동 직장인구 수',
        `LOC_INFO_RESIDENT_PERCENT` FLOAT NULL COMMENT '읍/면/동 주거인구 비율',
        `LOC_INFO_WORK_POP_PERCENT` FLOAT NULL COMMENT '읍/면/동 직장인구 비율',
        `LOC_INFO_MOVE_POP` INT NULL COMMENT '읍/면/동 유동인구 수',
        `LOC_INFO_CITY_MOVE_POP` INT NULL COMMENT '시/군/구 기준 유동인구 J_SCORE',
        `COMMERCIAL_DISTRICT_J_SCORE_AVERAGE` FLOAT NULL COMMENT '상권분석 J_SCORE 가중치 평균(시장규모,매출,결제건수,밀집도,결제금액)',
        `COMMERCIAL_DISTRICT_FOOD_BUSINESS_COUNT` INT NULL COMMENT '상권분석 대분류 읍/면/동 음식 업종 수',
        `COMMERCIAL_DISTRICT_HEALTHCARE_BUSINESS_COUNT` INT NULL COMMENT '상권분석 대분류 읍/면/동 의료/건강 업종 수',
        `COMMERCIAL_DISTRICT_EDUCATION_BUSINESS_COUNT` INT NULL COMMENT '상권분석 대분류 읍/면/동 학문/교육 업종 수',
        `COMMERCIAL_DISTRICT_ENTERTAINMENT_BUSINESS_COUNT` INT NULL COMMENT '상권분석 대분류 읍/면/동 여가/오락 업종 수',
        `COMMERCIAL_DISTRICT_LIFESTYLE_BUSINESS_COUNT` INT NULL COMMENT '상권분석 대분류 읍/면/동 생활서비스 업종 수',
        `COMMERCIAL_DISTRICT_RETAIL_BUSINESS_COUNT` INT NULL COMMENT '상권분석 대분류 읍/면/동 소매/유통 업종 수',
        `COMMERCIAL_DISTRICT_NATIONAL_MARKET_SIZE` BIGINT NULL COMMENT '상권분석 소분류 전국 평균 시장크기',
        `COMMERCIAL_DISTRICT_SUB_DISTRICT_MARKET_SIZE` BIGINT NULL COMMENT '상권분석 소분류 읍/면/동 시장크기',
        `COMMERCIAL_DISTRICT_NATIONAL_DENSITY_AVERAGE` FLOAT NULL COMMENT '상권분석 소분류 전국 평균 밀집도',
        `COMMERCIAL_DISTRICT_SUB_DISTRICT_DENSITY_AVERAGE` FLOAT NULL COMMENT '상권분석 소분류 읍/면/동 밀집도',
        `COMMERCIAL_DISTRICT_NATIONAL_AVERAGE_SALES` BIGINT NULL COMMENT '상권분석 소분류 전국 평균 매출',
        `COMMERCIAL_DISTRICT_SUB_DISTRICT_AVERAGE_SALES` BIGINT NULL COMMENT '상권분석 소분류 읍/면/동 매출',
        `COMMERCIAL_DISTRICT_NATIONAL_AVERAGE_PAYMENT` INT NULL COMMENT '상권분석 소분류 전국 평균 결제단가',
        `COMMERCIAL_DISTRICT_SUB_DISTRICT_AVERAGE_PAYMENT` INT NULL COMMENT '상권분석 소분류 읍/면/동 결제단가',
        `COMMERCIAL_DISTRICT_NATIONAL_USAGE_COUNT` INT NULL COMMENT '상권분석 소분류 전국 평균 이용건수',
        `COMMERCIAL_DISTRICT_SUB_DISTRICT_USAGE_COUNT` INT NULL COMMENT '상권분석 소분류 읍/면/동 이용건수',
        `COMMERCIAL_DISTRICT_MARKET_SIZE_J_SCORE` FLOAT NULL COMMENT '상권분석 읍/면/동 소분류 시장규모 J_SCORE',
        `COMMERCIAL_DISTRICT_AVERAGE_SALES_J_SCORE` FLOAT NULL COMMENT '상권분석 읍/면/동 소분류 평균매출 J_SCORE',
        `COMMERCIAL_DISTRICT_USAGE_COUNT_J_SCORE` FLOAT NULL COMMENT '상권분석 읍/면/동 소분류 결제건수 J_SCORE',
        `COMMERCIAL_DISTRICT_SUB_DISTRICT_DENSITY_J_SCORE` FLOAT NULL COMMENT '상권분석 읍/면/동 소분류 밀집도 J_SCORE',
        `COMMERCIAL_DISTRICT_AVERAGE_PAYMENT_J_SCORE` FLOAT NULL COMMENT '상권분석 읍/면/동 소분류 결제금액 J_SCORE',
        `COMMERCIAL_DISTRICT_AVERAGE_SALES_PERCENT_MON` FLOAT NULL COMMENT '상권분석 요일별 평균 매출 비중 월요일',
        `COMMERCIAL_DISTRICT_AVERAGE_SALES_PERCENT_TUE` FLOAT NULL COMMENT '상권분석 요일별 평균 매출 비중 화요일',
        `COMMERCIAL_DISTRICT_AVERAGE_SALES_PERCENT_WED` FLOAT NULL COMMENT '상권분석 요일별 평균 매출 비중 수요일',
        `COMMERCIAL_DISTRICT_AVERAGE_SALES_PERCENT_THU` FLOAT NULL COMMENT '상권분석 요일별 평균 매출 비중 목요일',
        `COMMERCIAL_DISTRICT_AVERAGE_SALES_PERCENT_FRI` FLOAT NULL COMMENT '상권분석 요일별 평균 매출 비중 금요일',
        `COMMERCIAL_DISTRICT_AVERAGE_SALES_PERCENT_SAT` FLOAT NULL COMMENT '상권분석 요일별 평균 매출 비중 토요일',
        `COMMERCIAL_DISTRICT_AVERAGE_SALES_PERCENT_SUN` FLOAT NULL COMMENT '상권분석 요일별 평균 매출 비중 일요일',
        `COMMERCIAL_DISTRICT_AVERAGE_SALES_PERCENT_06_09` FLOAT NULL COMMENT '상권분석 시간대별 평균 매출 비중 06_09',
        `COMMERCIAL_DISTRICT_AVERAGE_SALES_PERCENT_09_12` FLOAT NULL COMMENT '상권분석 시간대별 평균 매출 비중 09_12',
        `COMMERCIAL_DISTRICT_AVERAGE_SALES_PERCENT_12_15` FLOAT NULL COMMENT '상권분석 시간대별 평균 매출 비중 12_15',
        `COMMERCIAL_DISTRICT_AVERAGE_SALES_PERCENT_15_18` FLOAT NULL COMMENT '상권분석 시간대별 평균 매출 비중 15_18',
        `COMMERCIAL_DISTRICT_AVERAGE_SALES_PERCENT_18_21` FLOAT NULL COMMENT '상권분석 시간대별 평균 매출 비중 18_21',
        `COMMERCIAL_DISTRICT_AVERAGE_SALES_PERCENT_21_24` FLOAT NULL COMMENT '상권분석 시간대별 평균 매출 비중 21_24',
        `COMMERCIAL_DISTRICT_AVG_CLIENT_PER_M_20S` FLOAT NULL COMMENT '상권분석 남자 20 비율',
        `COMMERCIAL_DISTRICT_AVG_CLIENT_PER_M_30S` FLOAT NULL COMMENT '상권분석 남자 30 비율',
        `COMMERCIAL_DISTRICT_AVG_CLIENT_PER_M_40S` FLOAT NULL COMMENT '상권분석 남자 40 비율',
        `COMMERCIAL_DISTRICT_AVG_CLIENT_PER_M_50S` FLOAT NULL COMMENT '상권분석 남자 50 비율',
        `COMMERCIAL_DISTRICT_AVG_CLIENT_PER_M_60_OVER` FLOAT NULL COMMENT '상권분석 남자 60 이상 비율',
        `COMMERCIAL_DISTRICT_AVG_CLIENT_PER_F_20S` FLOAT NULL COMMENT '상권분석 여자 20 비율',
        `COMMERCIAL_DISTRICT_AVG_CLIENT_PER_F_30S` FLOAT NULL COMMENT '상권분석 여자 30 비율',
        `COMMERCIAL_DISTRICT_AVG_CLIENT_PER_F_40S` FLOAT NULL COMMENT '상권분석 여자 40 비율',
        `COMMERCIAL_DISTRICT_AVG_CLIENT_PER_F_50S` FLOAT NULL COMMENT '상권분석 여자 50 비율',
        `COMMERCIAL_DISTRICT_AVG_CLIENT_PER_F_60_OVER` FLOAT NULL COMMENT '상권분석 여자 60 이상 비율',
        `COMMERCIAL_DISTRICT_DETAIL_CATEGORY_AVERAGE_SALES_TOP1_INFO` VARCHAR(100) NULL COMMENT '상권분석 소분류 시/군/구 기준 매출  TOP1 읍/면/동(읍/면/동, 매출(억), 증감율)',
        `COMMERCIAL_DISTRICT_DETAIL_CATEGORY_AVERAGE_SALES_TOP2_INFO` VARCHAR(100) NULL COMMENT '상권분석 소분류 시/군/구 기준 매출  TOP2 읍/면/동(읍/면/동, 매출(억), 증감율)',
        `COMMERCIAL_DISTRICT_DETAIL_CATEGORY_AVERAGE_SALES_TOP3_INFO` VARCHAR(100) NULL COMMENT '상권분석 소분류 시/군/구 기준 매출  TOP3 읍/면/동(읍/면/동, 매출(억), 증감율)',
        `COMMERCIAL_DISTRICT_DETAIL_CATEGORY_AVERAGE_SALES_TOP4_INFO` VARCHAR(100) NULL COMMENT '상권분석 소분류 시/군/구 기준 매출  TOP4 읍/면/동(읍/면/동, 매출(억), 증감율)',
        `COMMERCIAL_DISTRICT_DETAIL_CATEGORY_AVERAGE_SALES_TOP5_INFO` VARCHAR(100) NULL COMMENT '상권분석 소분류 시/군/구 기준 매출  TOP5 읍/면/동(읍/면/동, 매출(억), 증감율)',
        `RISING_BUSINESS_NATIONAL_RISING_SALES_TOP1_INFO` VARCHAR(100) NULL COMMENT '뜨는업종 전국 매출증가 업종 TOP5  1등 (시/군/구,읍/면/동,소분류명,증가율)',
        `RISING_BUSINESS_NATIONAL_RISING_SALES_TOP2_INFO` VARCHAR(100) NULL COMMENT '뜨는업종 전국 매출증가 업종 TOP5  2등 (시/군/구,읍/면/동,소분류명,증가율)',
        `RISING_BUSINESS_NATIONAL_RISING_SALES_TOP3_INFO` VARCHAR(100) NULL COMMENT '뜨는업종 전국 매출증가 업종 TOP5  3등 (시/군/구,읍/면/동,소분류명,증가율)',
        `RISING_BUSINESS_NATIONAL_RISING_SALES_TOP4_INFO` VARCHAR(100) NULL COMMENT '뜨는업종 전국 매출증가 업종 TOP5  4등 (시/군/구,읍/면/동,소분류명,증가율)',
        `RISING_BUSINESS_NATIONAL_RISING_SALES_TOP5_INFO` VARCHAR(100) NULL COMMENT '뜨는업종 전국 매출증가 업종 TOP5  5등 (시/군/구,읍/면/동,소분류명,증가율)',
        `RISING_BUSINESS_SUB_DISTRICT_RISING_SALES_TOP1_INFO` VARCHAR(100) NULL COMMENT '뜨는업종 읍/면/동 매출증가 업종 TOP3 1등 (대분류명, 소분류명, 증가율)',
        `RISING_BUSINESS_SUB_DISTRICT_RISING_SALES_TOP2_INFO` VARCHAR(100) NULL COMMENT '뜨는업종 읍/면/동 매출증가 업종 TOP3 2등 (대분류명, 소분류명, 증가율)',
        `RISING_BUSINESS_SUB_DISTRICT_RISING_SALES_TOP3_INFO` VARCHAR(100) NULL COMMENT '뜨는업종 읍/면/동 매출증가 업종 TOP3 3등 (대분류명, 소분류명, 증가율)',
        `LOC_INFO_DATA_REF_DATE` DATE NULL COMMENT '입지 정보 데이터 기준년월',
        `NICE_BIZ_MAP_DATA_REF_DATE` DATE NULL COMMENT '상권분석 뜨는업종 비즈맵 데이터 기준년월',
        `POPULATION_DATA_REF_DATE` DATE NULL COMMENT '인구 데이터 기준년월',
        `CREATED_AT` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '생성일시',
        `UPDATED_AT` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '수정일시',
        PRIMARY KEY (`STORE_BUSINESS_NUMBER`)
    );

CREATE TABLE
    `LOCAL_STORE_IMAGE` (
        `LOCAL_STORE_IMAGE_ID` INT NOT NULL AUTO_INCREMENT COMMENT 'PK_LSIID',
        `STORE_BUSINESS_NUMBER` VARCHAR(100) NOT NULL COMMENT 'FK_RID',
        `LOCAL_STORE_IMAGE_URL` VARCHAR(255) NOT NULL COMMENT '매장 이미지 URL',
        `STATUS` CHAR(1) NOT NULL DEFAULT 'Y' COMMENT '상태 (Y: 활성, N: 비활성, D: 삭제)',
        `CREATED_AT` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '생성일시',
        `UPDATED_AT` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '수정일시',
        PRIMARY KEY (`LOCAL_STORE_IMAGE_ID`),
        FOREIGN KEY (`STORE_BUSINESS_NUMBER`) REFERENCES `REPORT` (`STORE_BUSINESS_NUMBER`) ON DELETE CASCADE
    );

CREATE TABLE
    `SERVICE_DETAIL_CATEGORY_MAPPING` (
        `DETAIL_CATEGORY_MAPPING_ID` INT AUTO_INCREMENT PRIMARY KEY COMMENT 'PK_DCMID',
        `REP_ID` INT NULL COMMENT '소분류 대표값 ID',
        `BUSINESS_AREA_CATEGORY_ID` INT NOT NULL COMMENT '매핑될 ID',
        `DETAIL_CATEGORY_ID` INT NOT NULL COMMENT '비즈맵소분류ID'
    );


CREATE TABLE
    `BIZ_DETAIL_CATEGORY_CONTENT` (
        `BIZ_DETAIL_CATEGORY_CONTENT_ID` INT AUTO_INCREMENT PRIMARY KEY COMMENT 'PK_BDCCID',
        `DETAIL_CATEGORY_ID` INT NOT NULL COMMENT '비즈맵 소분류 ID',
        `TITLE` VARCHAR(255) NOT NULL COMMENT '제목',
        `CONTENT` TEXT NOT NULL COMMENT '내용',
        `STATUS` CHAR(1) NOT NULL COMMENT '게시 여부',
        `CREATED_AT` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '생성일시',
        `UPDATED_AT` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '수정일시'
    );

CREATE TABLE
    `BIZ_DETAIL_CATEGORY_CONTENT_IMAGE` (
        `BIZ_DETAIL_CATEGORY_CONTENT_IMAGE_ID` INT AUTO_INCREMENT PRIMARY KEY COMMENT 'PK_BDCCID',
        `BIZ_DETAIL_CATEGORY_CONTENT_ID` INT NOT NULL COMMENT 'FK_BDDCCID',
        `BIZ_DETAIL_CATEGORY_CONTENT_IMAGE_URL` VARCHAR(255) NOT NULL COMMENT '이미지 URL',
        `CREATED_AT` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '생성일시',
        `UPDATED_AT` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '수정일시',
        FOREIGN KEY (`BIZ_DETAIL_CATEGORY_CONTENT_ID`) REFERENCES `BIZ_DETAIL_CATEGORY_CONTENT` (`BIZ_DETAIL_CATEGORY_CONTENT_ID`) ON DELETE CASCADE
    );

CREATE TABLE
    `LOCAL_STORE_CONTENT` (
        `LOCAL_STORE_CONTENT_ID` INT AUTO_INCREMENT PRIMARY KEY COMMENT 'PK_LSCID',
        `STORE_BUSINESS_NUMBER` VARCHAR(100) NOT NULL COMMENT 'FK_RID',
        `DETAIL_CATEGORY_ID` INT NOT NULL COMMENT '비즈맵 소분류 ID',
        `TITLE` VARCHAR(255) NOT NULL COMMENT '제목',
        `CONTENT` TEXT NOT NULL COMMENT '내용',
        `STATUS` CHAR(1) NOT NULL COMMENT '게시 여부',
        `CREATED_AT` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '생성일시',
        `UPDATED_AT` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '수정일시'
    );

CREATE TABLE
    `LOCAL_STORE_CONTENT_IMAGE` (
        `LOCAL_STORE_CONTENT_IMAGE_ID` INT AUTO_INCREMENT PRIMARY KEY COMMENT 'PK_LSCIID',
        `LOCAL_STORE_CONTENT_ID` INT NOT NULL COMMENT 'FK_LSCID',
        `LOCAL_STORE_CONTENT_IMAGE_URL` VARCHAR(255) NOT NULL COMMENT '이미지 URL',
        `CREATED_AT` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '생성일시',
        `UPDATED_AT` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '수정일시',
        FOREIGN KEY (`LOCAL_STORE_CONTENT_ID`) REFERENCES `LOCAL_STORE_CONTENT` (`LOCAL_STORE_CONTENT_ID`) ON DELETE CASCADE
    );

CREATE TABLE
    `ADS` (
        `ADS_ID` INT AUTO_INCREMENT PRIMARY KEY COMMENT 'PK_AID',
        `STORE_BUSINESS_NUMBER` VARCHAR(100) NOT NULL COMMENT 'FK_RID',
        `DETAIL_CATEGORY_ID` INT NOT NULL COMMENT '비즈맵 소분류 ID',
        `USE_OPTION` VARCHAR(30) NOT NULL COMMENT '광고 채널',
        `TITLE` VARCHAR(255) NOT NULL COMMENT '주제',
        `DETAIL_TITLE` VARCHAR(255) NOT NULL COMMENT '세부 주제',
        `CONTENT` TEXT NOT NULL COMMENT '문구',
        `STATUS` CHAR(1) NOT NULL COMMENT '게시 여부',
        `CREATED_AT` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '생성일시',
        `UPDATED_AT` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '수정일시'
    );

CREATE TABLE
    `ADS_IMAGE` (
        `ADS_IMAGE_ID` INT AUTO_INCREMENT PRIMARY KEY COMMENT 'PK_AIID',
        `ADS_ID` INT NOT NULL COMMENT 'FK_AID',
        `ADS_IMAGE_URL` VARCHAR(255) NOT NULL COMMENT '이미지 URL',
        `CREATED_AT` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '생성일시',
        `UPDATED_AT` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '수정일시',
        FOREIGN KEY (`ADS_ID`) REFERENCES `ADS` (`ADS_ID`) ON DELETE CASCADE
    );