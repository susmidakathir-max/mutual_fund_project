# Mutual Fund Analytics Platform

## Project Overview

The Mutual Fund Analytics Platform is an end-to-end data analytics project developed as part of the Bluestock Data Analytics Internship. The project focuses on collecting, processing, analyzing, and visualizing mutual fund data to generate meaningful insights for investors and fund managers.

The platform performs ETL operations, exploratory data analysis, performance analytics, advanced risk analytics, and dashboard reporting using Python, SQLite, Jupyter Notebook, and Power BI.

---

## Project Objectives

1. Build a complete ETL pipeline for mutual fund datasets.
2. Clean and validate financial data.
3. Store processed data in SQLite database.
4. Perform Exploratory Data Analysis (EDA).
5. Analyze mutual fund performance metrics.
6. Calculate advanced risk measures such as VaR, CVaR, and Sharpe Ratio.
7. Build an interactive Power BI dashboard.
8. Generate actionable investment insights.

---

## Technologies Used

### Programming Languages

* Python

### Libraries

* Pandas
* NumPy
* Matplotlib
* Seaborn
* Plotly
* SQLAlchemy
* SQLite3
* SciPy

### Tools

* Jupyter Notebook
* SQLite
* Power BI Desktop
* Git
* GitHub

---

## Project Structure

```text
mutual_fund_project/

│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   ├── EDA_Analysis.ipynb
│   ├── Performance_Analytics.ipynb
│   └── Advanced_Analytics.ipynb
│
├── reports/
│   ├── Final_Report.pdf
│   ├── rolling_sharpe_chart.png
│   ├── var_cvar_report.csv
│   └── other generated reports
│
├── dashboard/
│   └── bluestock_mf_dashboard.pbix
│
├── data_ingestion.py
├── data_cleaning.py
├── load_sqlite.py
├── run_pipeline.py
├── schema.sql
├── queries.sql
├── requirements.txt
├── README.md
└── bluestock_mf.db
```

---

## Data Sources

The project uses multiple mutual fund datasets:

### Raw Datasets

1. Fund Master
2. NAV History
3. AUM by Fund House
4. Monthly SIP Inflows
5. Category Inflows
6. Industry Folio Count
7. Scheme Performance
8. Investor Transactions
9. Portfolio Holdings
10. Benchmark Indices

---

## ETL Pipeline

### Extract

Data is collected from CSV files stored in the raw data directory.

### Transform

Data cleaning includes:

* Handling missing values
* Removing duplicates
* Standardizing column names
* Data type conversion
* Date formatting
* Validation checks

### Load

Processed datasets are loaded into SQLite database tables for analytics and reporting.

Database:

```text
bluestock_mf.db
```

---

## How to Run the Project

### Step 1: Clone Repository

```bash
git clone https://github.com/susmidakathir-max/mutual_fund_project.git
cd mutual_fund_project
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Run Complete Pipeline

```bash
python run_pipeline.py
```

This executes:

1. Data Ingestion
2. Data Cleaning
3. Database Loading

---

## Database

SQLite database stores all processed datasets.

Database File:

```text
bluestock_mf.db
```

Tables include:

* fund_master
* nav_history
* scheme_performance
* investor_transactions
* portfolio_holdings
* benchmark_indices

---

## Exploratory Data Analysis (Day 3)

EDA includes:

* Fund category distribution
* Gender distribution of investors
* Age group analysis
* SIP investment trends
* NAV movement analysis
* T30 vs B30 investor analysis

Notebook:

```text
EDA_Analysis.ipynb
```

---

## Performance Analytics (Day 4)

Performance metrics calculated:

### Risk Metrics

* Volatility
* Alpha
* Beta
* Tracking Error

### Return Metrics

* CAGR
* Annualized Return

### Fund Scorecard

Generated for all mutual fund schemes.

Notebook:

```text
Performance_Analytics.ipynb
```

---

## Advanced Analytics (Day 6)

### Historical VaR (95%)

Measures downside investment risk using return distributions.

### Conditional VaR (CVaR)

Measures expected loss beyond VaR threshold.

### Rolling Sharpe Ratio

90-day rolling Sharpe ratio calculated for selected funds.

### Investor Cohort Analysis

Investors grouped by first investment year.

### SIP Continuity Analysis

Identifies investors at risk of SIP discontinuation.

### Fund Recommendation Engine

Provides fund recommendations based on risk appetite:

* Low Risk
* Moderate Risk
* High Risk

### Sector Concentration Analysis

Herfindahl-Hirschman Index (HHI) used to evaluate portfolio concentration.

Notebook:

```text
Advanced_Analytics.ipynb
```

---

## Power BI Dashboard (Day 5)

Interactive dashboard includes:

### Dashboard Pages

1. Executive Overview
2. Fund Performance
3. Investor Analytics
4. SIP Analytics
5. Risk Analytics

### Dashboard Features

* KPI Cards
* Trend Analysis
* Category Filters
* Fund Comparisons
* Interactive Visualizations

Power BI File:

```text
bluestock_mf_dashboard.pbix
```

---

## Key Insights

### Fund Performance

* Top-performing schemes identified through Sharpe Ratio analysis.
* Risk-adjusted returns varied significantly across categories.

### Risk Analysis

* Certain schemes exhibited higher VaR and CVaR values.
* Concentrated portfolios showed elevated HHI scores.

### Investor Behavior

* Recent investor cohorts demonstrated higher SIP participation.
* Investors with SIP gaps greater than 35 days were classified as at-risk.

### Portfolio Analysis

* Diversified funds generally achieved lower concentration risk.
* Equity funds showed stronger long-term growth potential.

---

## Generated Reports

The project generates:

* var_cvar_report.csv
* alpha_beta.csv
* tracking_error.csv
* fund_scorecard.csv
* rolling_sharpe_chart.png
* benchmark_comparison.png
* nav_trend.png

---

## Deliverables

### Notebooks

* EDA_Analysis.ipynb
* Performance_Analytics.ipynb
* Advanced_Analytics.ipynb

### Reports

* Final_Report.pdf
* var_cvar_report.csv
* rolling_sharpe_chart.png

### Dashboard

* bluestock_mf_dashboard.pbix

### Presentation

* Bluestock_MF_Presentation.pptx

---

## Future Enhancements

* Live NAV API integration
* Automated daily data refresh
* Machine Learning fund recommendation system
* Web-based dashboard deployment
* Real-time investor monitoring

---

## Author

Susmida K

Bluestock Data Analytics Internship Project

Version: v1.0
