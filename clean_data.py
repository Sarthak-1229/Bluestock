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