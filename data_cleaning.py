"""
Data Cleaning Module

Cleans raw mutual fund datasets and
stores processed files.
"""
import pandas as pd
import os

os.makedirs("data/processed", exist_ok=True)

# --------------------------------------------------
# NAV HISTORY
# --------------------------------------------------

nav = pd.read_csv("data/raw/02_nav_history.csv")

nav["date"] = pd.to_datetime(nav["date"])

nav = nav.sort_values(
    ["amfi_code", "date"]
)

nav["nav"] = nav.groupby(
    "amfi_code"
)["nav"].ffill()

nav = nav.drop_duplicates()

nav = nav[nav["nav"] > 0]

nav.to_csv(
    "data/processed/nav_history_clean.csv",
    index=False
)

print("✓ NAV History Cleaned")


# --------------------------------------------------
# INVESTOR TRANSACTIONS
# --------------------------------------------------

tx = pd.read_csv(
    "data/raw/08_investor_transactions.csv"
)

tx["transaction_date"] = pd.to_datetime(
    tx["transaction_date"]
)

tx["transaction_type"] = (
    tx["transaction_type"]
    .str.strip()
    .str.title()
)

valid_types = [
    "Sip",
    "Lumpsum",
    "Redemption"
]

tx = tx[
    tx["transaction_type"].isin(valid_types)
]

tx = tx[
    tx["amount_inr"] > 0
]

valid_kyc = [
    "Verified",
    "Pending",
    "Rejected"
]

print("\nInvalid KYC Rows:")
print(
    tx[
        ~tx["kyc_status"].isin(valid_kyc)
    ].shape[0]
)

tx.to_csv(
    "data/processed/investor_transactions_clean.csv",
    index=False
)

print("✓ Investor Transactions Cleaned")


# --------------------------------------------------
# SCHEME PERFORMANCE
# --------------------------------------------------

perf = pd.read_csv(
    "data/raw/07_scheme_performance.csv"
)

return_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct"
]

for col in return_cols:

    perf[col] = pd.to_numeric(
        perf[col],
        errors="coerce"
    )

expense_anomalies = perf[
    (perf["expense_ratio_pct"] < 0.1)
    |
    (perf["expense_ratio_pct"] > 2.5)
]

print(
    "\nExpense Ratio Anomalies:",
    len(expense_anomalies)
)

perf.to_csv(
    "data/processed/scheme_performance_clean.csv",
    index=False
)

print("✓ Scheme Performance Cleaned")
other_files = [
    ("01_fund_master.csv", "fund_master_clean.csv"),
    ("03_aum_by_fund_house.csv", "aum_by_fund_house_clean.csv"),
    ("04_monthly_sip_inflows.csv", "monthly_sip_inflows_clean.csv"),
    ("05_category_inflows.csv", "category_inflows_clean.csv"),
    ("06_industry_folio_count.csv", "industry_folio_count_clean.csv"),
    ("09_portfolio_holdings.csv", "portfolio_holdings_clean.csv"),
    ("10_benchmark_indices.csv", "benchmark_indices_clean.csv")
]

for source, target in other_files:
    df = pd.read_csv(f"data/raw/{source}")

    df = df.drop_duplicates()

    df.to_csv(
        f"data/processed/{target}",
        index=False
    )

    print(f"✓ {target} created")