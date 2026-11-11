-- Analysis: Repeat Customer Analysis
-- Activity definition: Delivered orders only

WITH customer_orders AS (
    SELECT
        customer_id,
        COUNT(DISTINCT order_id) AS delivered_order_count,
        SUM(final_amount) AS total_delivered_spend
    FROM orders
    WHERE order_status = 'Delivered'
      AND customer_id IS NOT NULL
    GROUP BY customer_id
),

customer_summary AS (
    SELECT
        COUNT(*) AS total_customers,
        COUNT(*) FILTER (
            WHERE delivered_order_count = 1
        ) AS one_time_customers,
        COUNT(*) FILTER (
            WHERE delivered_order_count > 1
        ) AS repeat_customers,
        SUM(delivered_order_count) AS total_delivered_orders,
        AVG(delivered_order_count) AS average_orders_per_customer
    FROM customer_orders
)

SELECT
    total_customers,
    one_time_customers,
    repeat_customers,
    total_delivered_orders,
    ROUND(
        (
            100.0 * repeat_customers /
            NULLIF(total_customers, 0)
        )::numeric,
        2
    ) AS repeat_customer_percentage,
    ROUND(average_orders_per_customer::numeric, 2)
        AS average_orders_per_customer
FROM customer_summary;

-- Top 10 customers by delivered order count
SELECT
    customer_id,
    COUNT(DISTINCT order_id) AS delivered_order_count,
    ROUND(SUM(final_amount)::numeric, 2) AS total_delivered_spend
FROM orders
WHERE order_status = 'Delivered'
  AND customer_id IS NOT NULL
GROUP BY customer_id
ORDER BY delivered_order_count DESC, total_delivered_spend DESC
LIMIT 10;
