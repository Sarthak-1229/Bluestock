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


#-------------------------------------------------------------------------