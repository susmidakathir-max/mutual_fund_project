-- 1. Top 5 funds by AUM
SELECT * FROM aum_by_fund_house
ORDER BY total_aum_crore DESC
LIMIT 5;

-- 2. Average NAV
SELECT AVG(nav)
FROM nav_history;

-- 3. Monthly Average NAV
SELECT strftime('%Y-%m', date) AS month,
AVG(nav)
FROM nav_history
GROUP BY month;

-- 4. Transactions by State
SELECT state,
COUNT(*) AS txn_count
FROM investor_transactions
GROUP BY state
ORDER BY txn_count DESC;

-- 5. Funds with Expense Ratio < 1%
SELECT scheme_name,
expense_ratio_pct
FROM scheme_performance
WHERE expense_ratio_pct < 1;

-- 6. Total Investment by Transaction Type
SELECT transaction_type,
SUM(amount_inr)
FROM investor_transactions
GROUP BY transaction_type;

-- 7. Average Return by Category
SELECT category,
AVG(return_3yr_pct)
FROM scheme_performance
GROUP BY category;

-- 8. Top Performing Funds (5Y Return)
SELECT scheme_name,
return_5yr_pct
FROM scheme_performance
ORDER BY return_5yr_pct DESC
LIMIT 10;

-- 9. Investors by KYC Status
SELECT kyc_status,
COUNT(*)
FROM investor_transactions
GROUP BY kyc_status;

-- 10. NAV Records per Fund
SELECT amfi_code,
COUNT(*)
FROM nav_history
GROUP BY amfi_code;