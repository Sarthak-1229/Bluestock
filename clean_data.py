import pandas as pd

nav = pd.read_csv("data/raw/02_nav_history.csv")
print("Original Shape:", nav.shape)

# Converting the date column dtype to datetime
nav["date"] = pd.to_datetime(nav["date"])

# Sorting the nav by amfi code and date
nav = nav.sort_values(by=["amfi_code", "date"])

# Removing duplicate values
before = len(nav)
nav = nav.drop_duplicates()
after = len(nav)

print("Duplicates removed:", before - after)

# Checking missing NAV values
print("Missing NAV values:", nav["nav"].isnull().sum())

# Forward filling the missing nav  values
nav["nav"] = nav.groupby("amfi_code")["nav"].ffill()

# Check missing NAV values again to make sure ff is done
print("Missing NAV values:", nav["nav"].isnull().sum())

# Validating NAV > 0
invalid_nav = nav[nav["nav"] <= 0]

print("Invalid NAV values:", len(invalid_nav))

# New cleaned file
nav.to_csv(
    "data/processed/clean_nav_history.csv",
    index=False
)

print("\n")


#---------------------------------------------------------------------------

#Cleaning investor transaction.csv


transactions = pd.read_csv("data/raw/08_investor_transactions.csv")

print("\nInvestor Transactions Shape:",transactions.shape)

# Convertin date dtyp to datetime 

transactions["transaction_date"] = pd.to_datetime(transactions["transaction_date"])

# Standardizing the transaction types


transactions["transaction_type"] = (transactions["transaction_type"].str.strip().str.title())

print("\nUnique Transaction Types:")


print(
    transactions["transaction_type"].unique()
)

# validating amount<=0

invalid_amount = transactions[transactions["amount_inr"] <= 0   ]

print("\nInvalid Amount Records:",len(invalid_amount))

# Checking the kyc status values

print("\nKYC Status Values:")

print(
    transactions["kyc_status"].unique()
)

# saved cleaned inestor_transaction.csv

transactions.to_csv(
    "data/processed/clean_investor_transactions.csv",
    index=False
)

print("\n")

#--------------------------------------------------------------------------------

#Clwaning 07_scheme_performance.csv

performance = pd.read_csv("data/raw/07_scheme_performance.csv")

print("\nScheme Performance Shape:",performance.shape)


return_columns = ["return_1yr_pct","return_3yr_pct","return_5yr_pct","benchmark_3yr_pct" ]


for column in return_columns:
    performance[column] = pd.to_numeric(performance[column],errors="coerce")

# Check for missing values created after coonversion

print("\nMissing values in return columns:")

print(
    performance[return_columns].isnull().sum()
)

#anomaly tracking
anomalies = performance[ (performance["return_1yr_pct"] > 100) |(performance["return_1yr_pct"] < -100)]

print("\nAnomalous Return Records:",len(anomalies))

#validating  expense ratio
invalid_expense = performance[(performance["expense_ratio_pct"] < 0.1) |(performance["expense_ratio_pct"] > 2.5)]

print("\nInvalid Expense Ratio Records:",len(invalid_expense))

# Save cleaned dataset

performance.to_csv("data/processed/clean_scheme_performance.csv",index=False)

print("\n")
#---------------------------------------

# Cleaning fund_master.csv

fund_master = pd.read_csv("data/raw/01_fund_master.csv")

print("\nFund Master Shape:",fund_master.shape)

# Convertng launch date to datetime

fund_master["launch_date"] = pd.to_datetime(fund_master["launch_date"])

# Removeing duplicates

before = len(fund_master)

fund_master = fund_master.drop_duplicates()

after = len(fund_master)

print("Duplicates removed:",before - after)

# Validate expense ratio

invalid_expense = fund_master[(fund_master["expense_ratio_pct"] < 0) |(fund_master["expense_ratio_pct"] > 5) ]

print("Invalid Expense Ratios:",len(invalid_expense))

# Saved cleaned file

fund_master.to_csv("data/processed/clean_fund_master.csv",index=False)

print("Cleaned Fund Master saved!")

#----------------------------------

# Cleaning aum_by_fund_house.csv

aum = pd.read_csv("data/raw/03_aum_by_fund_house.csv")

aum["date"] = pd.to_datetime(aum["date"])

aum = aum.drop_duplicates()

aum.to_csv("data/processed/clean_aum_by_fund_house.csv",index=False)

print("\nCleaned AUM dataset saved!")

#-------------------------------------

# cleaning monthly_sip_flow.csv

sip = pd.read_csv("data/raw/04_monthly_sip_inflows.csv")

print("\nMissing values:")

print(sip.isnull().sum())

# Fill missing YoY values with 0

sip["yoy_growth_pct"] = (sip["yoy_growth_pct"].fillna(0))

sip.to_csv("data/processed/clean_monthly_sip_inflows.csv",index=False)

print("Cleaned SIP dataset saved!")

#--------------------------

# Cleaning category inflows csv

category_inflows = pd.read_csv("data/raw/05_category_inflows.csv")

category_inflows["month"] = pd.to_datetime(category_inflows["month"])

print("\nCategory Inflows Shape:", category_inflows.shape)

before = len(category_inflows)

category_inflows = category_inflows.drop_duplicates()

after = len(category_inflows)

print("Duplicates removed:", before - after)

category_inflows.to_csv("data/processed/clean_category_inflows.csv", index=False)


#--------------------------------------
# Cleaning industry folio count csv

industry_folios = pd.read_csv("data/raw/06_industry_folio_count.csv")

industry_folios["month"] = pd.to_datetime(industry_folios["month"])

print("\nIndustry Folio Dataset Shape:", industry_folios.shape)

before = len(industry_folios)

industry_folios = industry_folios.drop_duplicates()

after = len(industry_folios)

print("Duplicates removed:", before - after)

industry_folios.to_csv("data/processed/clean_industry_folio_count.csv", index=False)

#----------------------------------

# Cleaning portfolio holdings csb

portfolio = pd.read_csv("data/raw/09_portfolio_holdings.csv")

portfolio["portfolio_date"] = pd.to_datetime(portfolio["portfolio_date"])

print("\nPortfolio Holdings Shape:", portfolio.shape)

before = len(portfolio)

portfolio = portfolio.drop_duplicates()

after = len(portfolio)

print("Duplicates removed:", before - after)

portfolio.to_csv("data/processed/clean_portfolio_holdings.csv", index=False)

#-----------------------------------------

# Cleaning benchmark indices csv

benchmark = pd.read_csv("data/raw/10_benchmark_indices.csv")

benchmark["date"] = pd.to_datetime(benchmark["date"])

print("\nBenchmark Dataset Shape:", benchmark.shape)

before = len(benchmark)

benchmark = benchmark.drop_duplicates()

after = len(benchmark)

print("Duplicates removed:", before - after)

benchmark.to_csv("data/processed/clean_benchmark_indices.csv", index=False)

