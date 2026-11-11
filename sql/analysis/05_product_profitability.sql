-- Analysis: Product Profitability
-- Revenue and profit are calculated at item level.
-- Only items belonging to Delivered orders are included.

-- 1. Overall product profitability
SELECT
    COUNT(DISTINCT oi.product_id) AS total_products_sold,
    SUM(oi.quantity) AS total_units_sold,
    ROUND(SUM(oi.item_revenue)::numeric, 2) AS total_revenue,
    ROUND(SUM(oi.item_cost)::numeric, 2) AS total_cost,
    ROUND(SUM(oi.profit)::numeric, 2) AS total_profit,
    ROUND(
        (
            100.0 * SUM(oi.profit)
            / NULLIF(SUM(oi.item_revenue), 0)
        )::numeric,
        2
    ) AS profit_margin_percentage
FROM order_items oi
JOIN orders o
    ON oi.order_id = o.order_id
WHERE o.order_status = 'Delivered';


-- 2. Revenue and profitability by product category
SELECT
    p.category,
    COUNT(DISTINCT oi.product_id) AS products_sold,
    SUM(oi.quantity) AS units_sold,
    ROUND(SUM(oi.item_revenue)::numeric, 2) AS total_revenue,
    ROUND(SUM(oi.profit)::numeric, 2) AS total_profit,
    ROUND(
        (
            100.0 * SUM(oi.profit)
            / NULLIF(SUM(oi.item_revenue), 0)
        )::numeric,
        2
    ) AS profit_margin_percentage
FROM order_items oi
JOIN orders o
    ON oi.order_id = o.order_id
JOIN products p
    ON oi.product_id = p.product_id
WHERE o.order_status = 'Delivered'
GROUP BY p.category
ORDER BY total_profit DESC;


-- 3. Top 10 most profitable products
SELECT
    p.product_id,
    p.product_name,
    p.category,
    SUM(oi.quantity) AS units_sold,
    ROUND(SUM(oi.item_revenue)::numeric, 2) AS total_revenue,
    ROUND(SUM(oi.profit)::numeric, 2) AS total_profit,
    ROUND(
        (
            100.0 * SUM(oi.profit)
            / NULLIF(SUM(oi.item_revenue), 0)
        )::numeric,
        2
    ) AS profit_margin_percentage
FROM order_items oi
JOIN orders o
    ON oi.order_id = o.order_id
JOIN products p
    ON oi.product_id = p.product_id
WHERE o.order_status = 'Delivered'
GROUP BY
    p.product_id,
    p.product_name,
    p.category
ORDER BY total_profit DESC
LIMIT 10;
