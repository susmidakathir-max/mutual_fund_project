"""
Master Pipeline Script

Executes the complete ETL workflow.
"""

import os

print("Running data ingestion...")
os.system("python data_ingestion.py")

print("Running data cleaning...")
os.system("python data_cleaning.py")

print("Loading SQLite database...")
os.system("python load_sqlite.py")

print("Pipeline completed successfully.")
