-- Analysis: Customer Retention
-- Activity definition: At least one Delivered order
-- Retained: Active in both the current and previous year
-- New: First observed delivered order in the current year
-- Reactivated: Active again after not ordering in the previous year

WITH customer_year_activity AS (
    SELECT DISTINCT
        customer_id,
        EXTRACT(YEAR FROM order_date::date)::integer AS activity_year
    FROM orders
    WHERE order_status = 'Delivered'
      AND customer_id IS NOT NULL
      AND order_date IS NOT NULL
      AND order_date <> ''
),

first_purchase AS (
    SELECT
        customer_id,
        MIN(activity_year) AS first_purchase_year
    FROM customer_year_activity
    GROUP BY customer_id
),

yearly_summary AS (
    SELECT
        current_year.activity_year AS analysis_year,
        COUNT(*) AS active_customers,

        COUNT(*) FILTER (
            WHERE first_purchase.first_purchase_year =
                  current_year.activity_year
        ) AS new_customers,

        COUNT(*) FILTER (
            WHERE previous_year.customer_id IS NOT NULL
        ) AS retained_customers,

        COUNT(*) FILTER (
            WHERE previous_year.customer_id IS NULL
              AND first_purchase.first_purchase_year <
                  current_year.activity_year
        ) AS reactivated_customers

    FROM customer_year_activity current_year

    LEFT JOIN customer_year_activity previous_year
        ON current_year.customer_id = previous_year.customer_id
       AND previous_year.activity_year =
           current_year.activity_year - 1

    JOIN first_purchase
        ON current_year.customer_id = first_purchase.customer_id

    GROUP BY current_year.activity_year
),

previous_year_totals AS (
    SELECT
        activity_year,
        COUNT(*) AS previous_year_active_customers
    FROM customer_year_activity
    GROUP BY activity_year
)

SELECT
    yearly_summary.analysis_year,
    yearly_summary.active_customers,
    yearly_summary.new_customers,
    yearly_summary.retained_customers,
    yearly_summary.reactivated_customers,
    previous_year_totals.previous_year_active_customers,

    ROUND(
        (
            100.0 * yearly_summary.retained_customers
            / NULLIF(
                previous_year_totals.previous_year_active_customers,
                0
            )
        )::numeric,
        2
    ) AS retention_rate_percentage

FROM yearly_summary

LEFT JOIN previous_year_totals
    ON previous_year_totals.activity_year =
       yearly_summary.analysis_year - 1

ORDER BY yearly_summary.analysis_year;
