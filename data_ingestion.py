import pandas as pd
import os
path = "data\\raw"
csv=[f for f in os.listdir(path)
     if f.endswith(".csv")]
print(csv)

for file in csv:
    file_path = os.path.join(path, file)

    print("\n" + "="*60)
    print(f"Dataset: {file}")

    df = pd.read_csv(file_path)

    print("\nShape:")
    print(df.shape)

    print("\nData Types:")
    print(df.dtypes)

    print("\nFirst 5 Rows:")
    print(df.head())

    fund_master = pd.read_csv("data/raw/01_fund_master.csv")

print("\nUnique Fund Houses:")
print(fund_master["fund_house"].unique())

print("\nUnique Categories:")
print(fund_master["category"].unique())

print("\nUnique Sub-Categories:")
print(fund_master["sub_category"].unique())

print("\nUnique Risk Categories:")
print(fund_master["risk_category"].unique())



# Load the datasets
fund_master = pd.read_csv("data/raw/01_fund_master.csv")
nav_history = pd.read_csv("data/raw/02_nav_history.csv")

# Get unique AMFI codes from both datasets
fund_codes = fund_master["amfi_code"].unique()
nav_codes = nav_history["amfi_code"].unique()

# Check if every code in fund_master exists in nav_history
missing_codes = []

for code in fund_codes:
    if code not in nav_codes:
        missing_codes.append(code)

# Display results
print("\nTotal Fund Master Codes:", len(fund_codes))
print("Total NAV History Codes:", len(nav_codes))

if len(missing_codes) == 0:
    print("\nAll AMFI codes from fund_master are present in nav_history.")
else:
    print("\nMissing AMFI Codes:")
    print(missing_codes)

