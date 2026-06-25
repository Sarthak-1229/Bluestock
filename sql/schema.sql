-- Dimension Table for Funds

CREATE TABLE dim_fund 
(
    amfi_code INTEGER PRIMARY KEY,
    fund_house TEXT,
    scheme_name TEXT,
    category TEXT,
    sub_category TEXT,
    plan TEXT,
    benchmark TEXT,
    fund_manager TEXT,
    risk_category TEXT
);


-- Dimension Table for Dates

CREATE TABLE dim_date 
(
    date_id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_date DATE UNIQUE,
    year INTEGER,
    month INTEGER,
    day INTEGER
);


-- Fact Table for NAV

CREATE TABLE fact_nav 
(
    nav_id INTEGER PRIMARY KEY AUTOINCREMENT,
    amfi_code INTEGER,
    date_id INTEGER,
    nav REAL,
    FOREIGN KEY (amfi_code) REFERENCES dim_fund(amfi_code),
    FOREIGN KEY (date_id) REFERENCES dim_date(date_id)
);



-- Fact Table for Transactions

CREATE TABLE fact_transactions 
(
    transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
    amfi_code INTEGER,
    transaction_date DATE,
    amount_inr REAL,
    transaction_type TEXT,
    state TEXT,
    city TEXT,
    payment_mode TEXT,
    kyc_status TEXT,

    FOREIGN KEY (amfi_code) REFERENCES dim_fund(amfi_code)
);


-- Fact Table for Performance

CREATE TABLE fact_performance 
(
    performance_id INTEGER PRIMARY KEY AUTOINCREMENT,
    amfi_code INTEGER,
    return_1yr_pct REAL,
    return_3yr_pct REAL,
    return_5yr_pct REAL,
    alpha REAL,
    beta REAL,
    sharpe_ratio REAL,
    expense_ratio_pct REAL,
    FOREIGN KEY (amfi_code) REFERENCES dim_fund(amfi_code)
);


-- Fact Table for AUM

CREATE TABLE fact_aum 
(
    aum_id INTEGER PRIMARY KEY AUTOINCREMENT,
    fund_house TEXT,
    date_id INTEGER,
    aum_crore REAL,
    num_schemes INTEGER,
    FOREIGN KEY (date_id) REFERENCES dim_date(date_id)
);