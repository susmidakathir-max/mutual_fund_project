from sqlalchemy import create_engine
import pandas as pd

engine = create_engine(
    "sqlite:///bluestock_mf.db"
)

files = {
    "fund_master":
    "data/processed/fund_master_clean.csv",

    "nav_history":
    "data/processed/nav_history_clean.csv",

    "investor_transactions":
    "data/processed/investor_transactions_clean.csv",

    "scheme_performance":
    "data/processed/scheme_performance_clean.csv",

    "aum_by_fund_house":
    "data/processed/aum_by_fund_house_clean.csv"
}

for table, file in files.items():

    df = pd.read_csv(file)

    df.to_sql(
        table,
        engine,
        if_exists="replace",
        index=False
    )

    print(
        f"{table}: {len(df)} rows loaded"
    )

print("Database created successfully")