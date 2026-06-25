-- 1. Top 5 fund houses by AUM

SELECT fund_house,SUM(aum_crore) AS total_aum
FROM fact_aum
GROUP BY fund_house
ORDER BY total_aum DESC
LIMIT 5;


-- 2. Average NAV per month

SELECT strftime ('%Y-%m', date) AS month,AVG(nav) AS average_nav
FROM fact_nav
GROUP BY month
ORDER BY month;


-- 3. Monthly SIP inflows with YoY growth

SELECT month,sip_inflow_crore,yoy_growth_pct
FROM monthly_sip_inflows
ORDER BY month;


-- 4. Number of transactions by state

SELECT state,COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY state
ORDER BY total_transactions DESC;


-- 5. Funds with expense ratio less than 1%

SELECT scheme_name,expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1
ORDER BY expense_ratio_pct;


-- 6. Top 5 funds by 5-year returns

SELECT scheme_name,return_5yr_pct
FROM fact_performance
ORDER BY return_5yr_pct DESC
LIMIT 5;


-- 7. Average 3-year return by category

SELECT category,AVG(return_3yr_pct) AS average_return
FROM fact_performance
GROUP BY category;


-- 8. Transactions by payment mode

SELECT payment_mode,COUNT(*) AS transaction_count
FROM fact_transactions
GROUP BY payment_mode
ORDER BY transaction_count DESC;


-- 9. Number of funds by risk category

SELECT risk_category,COUNT(*) AS fund_count
FROM dim_fund
GROUP BY risk_category
ORDER BY fund_count DESC;


-- 10. Top 10 cities by investment amount

SELECT city,SUM(amount_inr) AS total_investment
FROM fact_transactions
GROUP BY city
ORDER BY total_investment DESC
LIMIT 10;
