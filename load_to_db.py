import pandas as pd

from sqlalchemy import create_engine

engine = create_engine("sqlite:///bluestock_mf.db")


tables = {
    "clean_fund_master.csv": "dim_fund",

    "clean_nav_history.csv": "fact_nav",

    "clean_investor_transactions.csv": "fact_transactions",

    "clean_scheme_performance.csv": "fact_performance",

    "clean_aum_by_fund_house.csv": "fact_aum",

    "clean_monthly_sip_inflows.csv": "monthly_sip_inflows",
    "clean_category_inflows.csv": "category_inflows",
    "clean_industry_folio_count.csv": "industry_folio_count",
    "clean_portfolio_holdings.csv": "portfolio_holdings",
    "clean_benchmark_indices.csv": "benchmark_indices"
}


for file_name, table_name in tables.items():

    df = pd.read_csv(f"data/processed/{file_name}")

    df.to_sql(table_name,engine,if_exists="replace",index=False)

    print(f"{table_name} loaded successfully. Rows: {len(df)}")



print("\nAll datasets loaded into SQLite successfully!")