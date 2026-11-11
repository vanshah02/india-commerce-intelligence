-- Analysis: Marketing Effectiveness
-- Metrics: Spend, revenue, ROAS, CTR, conversion rate and cost per conversion
-- Source: marketing_campaigns

-- 1. Overall marketing performance

SELECT
    COUNT(*) AS total_campaigns,
    SUM(impressions) AS total_impressions,
    SUM(clicks) AS total_clicks,
    SUM(conversions) AS total_conversions,
    ROUND(SUM(campaign_cost)::numeric, 2) AS total_campaign_spend,
    ROUND(SUM(revenue_generated)::numeric, 2) AS total_campaign_revenue,

    ROUND(
        (
            SUM(revenue_generated) /
            NULLIF(SUM(campaign_cost), 0)
        )::numeric,
        2
    ) AS overall_roas,

    ROUND(
        (
            100.0 * SUM(clicks) /
            NULLIF(SUM(impressions), 0)
        )::numeric,
        2
    ) AS ctr_percentage,

    ROUND(
        (
            100.0 * SUM(conversions) /
            NULLIF(SUM(clicks), 0)
        )::numeric,
        2
    ) AS conversion_rate_percentage,

    ROUND(
        (
            SUM(campaign_cost) /
            NULLIF(SUM(conversions), 0)
        )::numeric,
        2
    ) AS cost_per_conversion

FROM marketing_campaigns;


-- 2. Marketing performance by channel

SELECT
    channel,
    COUNT(*) AS total_campaigns,
    SUM(impressions) AS total_impressions,
    SUM(clicks) AS total_clicks,
    SUM(conversions) AS total_conversions,
    ROUND(SUM(campaign_cost)::numeric, 2) AS total_spend,
    ROUND(SUM(revenue_generated)::numeric, 2) AS total_revenue,

    ROUND(
        (
            SUM(revenue_generated) /
            NULLIF(SUM(campaign_cost), 0)
        )::numeric,
        2
    ) AS roas,

    ROUND(
        (
            100.0 * SUM(clicks) /
            NULLIF(SUM(impressions), 0)
        )::numeric,
        2
    ) AS ctr_percentage,

    ROUND(
        (
            100.0 * SUM(conversions) /
            NULLIF(SUM(clicks), 0)
        )::numeric,
        2
    ) AS conversion_rate_percentage,

    ROUND(
        (
            SUM(campaign_cost) /
            NULLIF(SUM(conversions), 0)
        )::numeric,
        2
    ) AS cost_per_conversion

FROM marketing_campaigns
GROUP BY channel
ORDER BY total_revenue DESC;


-- 3. Marketing performance by campaign type

SELECT
    campaign_type,
    COUNT(*) AS total_campaigns,
    SUM(conversions) AS total_conversions,
    ROUND(SUM(campaign_cost)::numeric, 2) AS total_spend,
    ROUND(SUM(revenue_generated)::numeric, 2) AS total_revenue,

    ROUND(
        (
            SUM(revenue_generated) /
            NULLIF(SUM(campaign_cost), 0)
        )::numeric,
        2
    ) AS roas

FROM marketing_campaigns
GROUP BY campaign_type
ORDER BY total_revenue DESC;


-- 4. Top 10 campaigns by revenue

SELECT
    campaign_id,
    campaign_name,
    channel,
    campaign_type,
    conversions,
    ROUND(campaign_cost::numeric, 2) AS campaign_cost,
    ROUND(revenue_generated::numeric, 2) AS revenue_generated,
    ROUND(
        (
            revenue_generated /
            NULLIF(campaign_cost, 0)
        )::numeric,
        2
    ) AS roas

FROM marketing_campaigns
ORDER BY revenue_generated DESC
LIMIT 10;


-- 5. Loss-making campaigns
-- Campaigns where generated revenue is lower than campaign cost.

SELECT
    campaign_id,
    campaign_name,
    channel,
    campaign_type,
    ROUND(campaign_cost::numeric, 2) AS campaign_cost,
    ROUND(revenue_generated::numeric, 2) AS revenue_generated,
    ROUND(
        (revenue_generated - campaign_cost)::numeric,
        2
    ) AS revenue_minus_cost,
    ROUND(
        (
            revenue_generated /
            NULLIF(campaign_cost, 0)
        )::numeric,
        2
    ) AS roas

FROM marketing_campaigns
WHERE revenue_generated < campaign_cost
ORDER BY revenue_minus_cost ASC;
