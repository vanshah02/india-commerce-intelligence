-- Analysis: Monthly Revenue Growth
-- Metric: Delivered revenue and month-over-month growth
-- Source: orders

WITH monthly_revenue AS (
    SELECT
        DATE_TRUNC('month', order_date::date)::date AS revenue_month,
        SUM(final_amount) AS total_revenue
    FROM orders
    WHERE order_status = 'Delivered'
      AND order_date IS NOT NULL
      AND order_date <> ''
    GROUP BY 1
),

calendar_months AS (
    SELECT GENERATE_SERIES(
        (SELECT MIN(revenue_month) FROM monthly_revenue),
        (SELECT MAX(revenue_month) FROM monthly_revenue),
        INTERVAL '1 month'
    )::date AS revenue_month
),

complete_monthly_revenue AS (
    SELECT
        c.revenue_month,
        COALESCE(m.total_revenue, 0) AS total_revenue
    FROM calendar_months c
    LEFT JOIN monthly_revenue m
        ON c.revenue_month = m.revenue_month
),

revenue_with_previous_month AS (
    SELECT
        revenue_month,
        total_revenue,
        LAG(total_revenue) OVER (
            ORDER BY revenue_month
        ) AS previous_month_revenue
    FROM complete_monthly_revenue
)

SELECT
    revenue_month,
    ROUND(total_revenue::numeric, 2) AS total_revenue,
    ROUND(previous_month_revenue::numeric, 2) AS previous_month_revenue,
    ROUND(
        (
            (total_revenue - previous_month_revenue)
            / NULLIF(previous_month_revenue, 0)
            * 100
        )::numeric,
        2
    ) AS revenue_growth_percentage
FROM revenue_with_previous_month
ORDER BY revenue_month;
