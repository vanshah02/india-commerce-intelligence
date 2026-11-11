-- Analysis: State-wise Sales Performance
-- All financial metrics use Delivered orders only.
-- Source: orders

WITH state_sales AS (
    SELECT
        delivery_state,
        COUNT(DISTINCT order_id) AS delivered_orders,
        COUNT(DISTINCT customer_id) AS unique_customers,
        SUM(final_amount) AS total_revenue,
        AVG(final_amount) AS average_order_value
    FROM orders
    WHERE order_status = 'Delivered'
      AND delivery_state IS NOT NULL
      AND TRIM(delivery_state) <> ''
    GROUP BY delivery_state
),

sales_with_contribution AS (
    SELECT
        *,
        SUM(total_revenue) OVER () AS overall_revenue
    FROM state_sales
)

SELECT
    delivery_state,
    delivered_orders,
    unique_customers,
    ROUND(total_revenue::numeric, 2) AS total_revenue,
    ROUND(average_order_value::numeric, 2) AS average_order_value,
    ROUND(
        (100.0 * total_revenue / NULLIF(overall_revenue, 0))::numeric,
        2
    ) AS revenue_contribution_percentage
FROM sales_with_contribution
ORDER BY total_revenue DESC;


-- Top 10 states by delivered revenue
SELECT
    delivery_state,
    COUNT(DISTINCT order_id) AS delivered_orders,
    ROUND(SUM(final_amount)::numeric, 2) AS total_revenue
FROM orders
WHERE order_status = 'Delivered'
  AND delivery_state IS NOT NULL
  AND TRIM(delivery_state) <> ''
GROUP BY delivery_state
ORDER BY total_revenue DESC
LIMIT 10;
