-- Analysis: Yearly Revenue Growth
-- Metrics: Revenue, delivered orders, average order value, YoY growth
-- Source: orders

WITH yearly_revenue AS (
    SELECT
        EXTRACT(YEAR FROM order_date::date)::integer AS revenue_year,
        SUM(final_amount) AS total_revenue,
        COUNT(DISTINCT order_id) AS total_orders,
        AVG(final_amount) AS average_order_value
    FROM orders
    WHERE order_status = 'Delivered'
      AND order_date IS NOT NULL
      AND order_date <> ''
    GROUP BY 1
),

revenue_with_previous_year AS (
    SELECT
        revenue_year,
        total_revenue,
        total_orders,
        average_order_value,
        LAG(total_revenue) OVER (
            ORDER BY revenue_year
        ) AS previous_year_revenue
    FROM yearly_revenue
)

SELECT
    revenue_year,
    ROUND(total_revenue::numeric, 2) AS total_revenue,
    total_orders,
    ROUND(average_order_value::numeric, 2) AS average_order_value,
    ROUND(
        (
            (total_revenue - previous_year_revenue)
            / NULLIF(previous_year_revenue, 0)
            * 100
        )::numeric,
        2
    ) AS revenue_growth_percentage
FROM revenue_with_previous_year
ORDER BY revenue_year;
