# India Commerce Intelligence
## Business Insights Report

**Project Period:** January 2023 – December 2025  
**Technology Stack:** Python, Pandas, NumPy, PostgreSQL, SQL, Metabase  
**Project Type:** E-commerce Data Analytics and Business Intelligence

---

# 1. Executive Summary

India Commerce Intelligence is an e-commerce analytics project designed to analyse sales performance, customer behaviour, product profitability, geographical performance, order fulfilment, payment activity, returns, and marketing effectiveness.

The project uses nine interconnected datasets containing **659,318 records** across customers, orders, products, order items, payments, shipments, returns, customer reviews, and marketing campaigns.

The objective is to transform raw e-commerce data into clean, analysis-ready datasets and generate actionable business insights using Python, SQL, PostgreSQL, and Metabase.

### 1.1 Key Business Metrics

| Metric | Result |
|---|---:|
| Total Customers | 25,000 |
| Total Orders | 100,000 |
| Total Products | 550 |
| Delivered Orders | 80,679 |
| Delivered Order Revenue | 2,084,309,803.30 |
| Customers with Delivered Orders | 21,849 |
| Repeat Customer Rate | 78.25% |
| Delivered Item Profit | 158,628,938.94 |
| Product Profit Margin | 7.99% |
| Average Delivery Time | 4.10 days |
| Marketing Campaigns | 151 |
| Marketing ROAS | 2.33 |

### 1.2 Major Findings

1. **Sales Performance:** Delivered revenue increased by 68.16% in 2025 compared with 2024.
2. **Customer Behaviour:** 78.25% of customers with delivered orders made repeat purchases.
3. **Product Profitability:** The overall delivered item profit margin was 7.99%, with significant differences across product categories.
4. **Geographical Performance:** Maharashtra generated the highest delivered revenue, contributing 13.96%.
5. **Operations:** 41.76% of shipments were flagged as delayed.
6. **Marketing Effectiveness:** Campaigns generated 436,296,290.91 in attributed revenue against campaign spending of 187,120,911.26, producing an overall ROAS of 2.33.

### 1.3 Project Objective

The primary objective is to identify business performance trends, customer retention opportunities, operational inefficiencies, product profitability issues, and opportunities to improve marketing effectiveness.

---

# 2. Sales Performance Insights

Sales performance was analysed using delivered orders from January 2023 to December 2025.

The analysis focused on yearly revenue, year-over-year growth, monthly revenue trends, delivered order volume, and average order value.

## 2.1 Yearly Revenue Performance

| Year | Delivered Revenue | Delivered Orders | Average Order Value | Revenue Growth |
|---|---:|---:|---:|---:|
| 2023 | 574,176,966.04 | 21,984 | 26,117.95 | Baseline |
| 2024 | 563,143,556.27 | 22,057 | 25,531.29 | -1.92% |
| 2025 | 946,989,280.99 | 36,638 | 25,847.19 | +68.16% |

## 2.2 Monthly Revenue Trends

Monthly delivered revenue was analysed using month-over-month growth.

Notable movements included:

- February 2023 recorded month-over-month revenue growth of 123.09%.
- February 2025 recorded a month-over-month decline of 21.54%.
- October 2025 recorded month-over-month growth of 66.04%.
- December 2025 recorded delivered revenue of 167,911,724.09.

## 2.3 Key Observations

1. **Strong growth in 2025:** Delivered revenue increased by 68.16% compared with 2024.
2. **2024 revenue decline:** Revenue decreased by 1.92% in 2024, despite a slight increase in delivered order volume.
3. **Order volume expansion:** Delivered orders increased from 22,057 in 2024 to 36,638 in 2025.
4. **Average order value stability:** Average order value remained relatively stable across all three years, ranging from 25,531.29 to 26,117.95.

## 2.4 Business Implications

- The strong growth in 2025 indicates a significant improvement in delivered sales performance.
- The increase in delivered order volume was a major contributor to revenue expansion.
- Stable average order value suggests that revenue growth was not driven solely by higher order values.
- Monthly fluctuations indicate the importance of monitoring seasonal patterns and planning inventory and marketing activities accordingly.

## 2.5 Recommendations

1. Investigate the factors behind the strong 2025 revenue growth and identify strategies that can be sustained.
2. Analyse the causes of the 2024 revenue decline.
3. Monitor monthly revenue growth to identify unusual declines early.
4. Focus on increasing average order value through product bundles, cross-selling, and relevant recommendations.
5. Use historical monthly sales trends to improve inventory and campaign planning.

---

# 3. Customer Behaviour and Retention Insights

Customer analysis focused on purchasing behaviour, repeat purchases, retention rates, customer segments, and customer status.

The analysis uses delivered orders to measure purchasing behaviour.

## 3.1 Customer Overview

| Metric | Result |
|---|---:|
| Total Registered Customers | 25,000 |
| Customers with Delivered Orders | 21,849 |
| One-Time Customers | 4,753 |
| Repeat Customers | 17,096 |
| Repeat Customer Percentage | 78.25% |
| Total Delivered Orders | 80,679 |
| Average Delivered Orders per Customer | 3.69 |

## 3.2 Customer Retention Analysis

A retained customer is defined as a customer with at least one delivered order in both the current year and the previous year.

| Year | Active Customers | New Customers | Retained Customers | Reactivated Customers | Retention Rate |
|---|---:|---:|---:|---:|---:|
| 2023 | 7,691 | 7,691 | 0 | 0 | Baseline |
| 2024 | 8,960 | 5,942 | 3,018 | 0 | 39.24% |
| 2025 | 11,932 | 8,216 | 3,487 | 229 | 38.92% |

**Note:** The 2023 figures represent the first year of observed delivered-order activity. Retention is calculated using the previous year's active customers as the denominator. The dataset does not provide delivered-order history before 2023.

## 3.3 Customer Segmentation

| Customer Segment | Number of Customers |
|---|---:|
| Regular | 11,002 |
| Budget | 7,713 |
| New | 3,294 |
| Premium | 2,991 |

Premium customers recorded an average spend of 286,622.67, making this segment particularly valuable from a customer-value perspective.

## 3.4 Customer Status Distribution

| Customer Status | Number of Customers |
|---|---:|
| Churned | 13,365 |
| Active | 7,234 |
| Never Purchased | 2,300 |
| At Risk | 2,101 |

## 3.5 Key Observations

1. **Strong repeat purchasing:** 78.25% of customers with delivered orders made more than one delivered purchase.
2. **Retention opportunity:** The annual retention rate decreased slightly from 39.24% in 2024 to 38.92% in 2025.
3. **Premium customer value:** Premium customers have substantially higher average spending than the overall customer base.
4. **Churn concern:** The customer dataset identifies 13,365 customers as churned.
5. **Reactivation opportunity:** 229 customers became active again in 2025 after not purchasing in 2024.

## 3.6 Business Implications

- Repeat customers represent an important source of business revenue.
- The retention rate indicates room to improve customer loyalty.
- Premium customers offer opportunities for targeted retention and loyalty initiatives.
- Churned and at-risk customers represent potential opportunities for re-engagement.
- Reactivated customers demonstrate that previously inactive customers can return.

## 3.7 Recommendations

1. Introduce targeted loyalty programmes for repeat customers.
2. Develop personalised campaigns for premium customers.
3. Create win-back campaigns for churned and at-risk customers.
4. Analyse why customers stop purchasing after their first order.
5. Monitor annual retention and reactivation rates.
6. Offer relevant product recommendations based on customer purchase history.

---

# 4. Product Performance and Profitability Insights

Product analysis focused on units sold, item-level revenue, product costs, profit margins, category performance, and individual product profitability.

The analysis includes items belonging to delivered orders only.

## 4.1 Overall Product Performance

| Metric | Result |
|---|---:|
| Total Products Sold | 550 |
| Total Units Sold | 472,749 |
| Delivered Item Revenue | 1,984,905,302.15 |
| Delivered Item Cost | 1,826,276,363.21 |
| Delivered Item Profit | 158,628,938.94 |
| Overall Profit Margin | 7.99% |

## 4.2 Category-wise Profitability

| Category | Total Profit | Profit Margin |
|---|---:|---:|
| Fashion | 37,461,222.13 | 33.19% |
| Home & Kitchen | 23,010,617.87 | 17.99% |
| Footwear | 19,553,630.12 | 29.44% |
| Bags | 12,977,026.11 | 28.62% |
| Appliances | 12,656,074.04 | 3.88% |
| Electronics | 6,006,174.82 | 0.60% |

## 4.3 Product-level Findings

- The most profitable product was **PROD10392 — Gandhi-Lanka Ultra Storage & Container**, in the Home & Kitchen category, generating 13,559,798.74 in profit.
- Chanda Deluxe Winter Wear recorded the highest unit sales among the top 10 most profitable products, with 14,178 units sold.
- Electronics generated substantial revenue of 994,296,183.05 but had a profit margin of only 0.60%.

## 4.4 Key Observations

1. **Low overall profitability:** The overall delivered item profit margin was 7.99%.
2. **Fashion leads profitability:** Fashion recorded the highest category profit and a margin of 33.19%.
3. **Strong footwear margins:** Footwear generated a profit margin of 29.44%.
4. **Electronics margin concern:** Despite generating the highest category revenue, Electronics had a very low profit margin of 0.60%.
5. **Appliances profitability:** Appliances also had a relatively low profit margin of 3.88%.

## 4.5 Business Implications

- High-revenue categories do not necessarily generate high profits.
- Electronics requires closer monitoring because its large revenue contribution is accompanied by a low profit margin.
- Fashion, Footwear, and Bags demonstrate stronger profitability and may offer opportunities for growth.
- Product-level profitability analysis can help identify products that generate revenue without contributing sufficiently to profit.

## 4.6 Recommendations

1. Review supplier costs and pricing strategies for Electronics.
2. Evaluate discounting practices in low-margin categories.
3. Focus on expanding profitable categories such as Fashion and Footwear.
4. Identify products with high sales volume but low profit margins.
5. Monitor product-level profit margins regularly rather than relying only on revenue.
6. Use profitability analysis when making inventory and promotional decisions.

**Measurement note:** Item-level revenue and profit are calculated from `order_items`. They are different from order-level `final_amount` revenue and should be interpreted separately.

---

# 5. State-wise Sales Insights

Geographical sales analysis was performed using delivered orders across 15 Indian states.

The analysis focused on delivered revenue, order volume, unique customers, average order value, and revenue contribution.

## 5.1 State-wise Revenue Performance

| State | Delivered Orders | Delivered Revenue | Revenue Contribution |
|---|---:|---:|---:|
| Maharashtra | 11,388 | 291,040,130.86 | 13.96% |
| Uttar Pradesh | 8,637 | 231,579,249.75 | 11.11% |
| Gujarat | 8,352 | 219,318,619.40 | 10.52% |
| Karnataka | 6,427 | 160,659,737.03 | 7.71% |
| Tamil Nadu | 6,197 | 157,331,652.14 | 7.55% |
| Telangana | 5,661 | 152,224,616.88 | 7.30% |
| Haryana | 4,996 | 129,931,442.22 | 6.23% |
| West Bengal | 4,810 | 119,716,221.13 | 5.74% |
| Kerala | 4,103 | 103,649,144.28 | 4.97% |
| Andhra Pradesh | 3,966 | 99,426,253.94 | 4.77% |
| Madhya Pradesh | 3,767 | 96,934,181.29 | 4.65% |
| Rajasthan | 3,765 | 95,936,545.38 | 4.60% |
| Delhi | 3,583 | 95,798,391.83 | 4.60% |
| Punjab | 3,620 | 93,172,084.98 | 4.47% |
| Bihar | 1,407 | 37,591,532.19 | 1.80% |

## 5.2 Key Observations

1. **Maharashtra leads sales:** Maharashtra recorded the highest delivered revenue of 291.04 million, contributing 13.96% of total delivered revenue.
2. **Strong performance in Uttar Pradesh and Gujarat:** These states contributed 11.11% and 10.52% of delivered revenue respectively.
3. **Top three states:** Maharashtra, Uttar Pradesh, and Gujarat together contributed approximately 35.59% of delivered revenue.
4. **Telangana's average order value:** Telangana recorded an average order value of 26,890.06, the highest among the top six states by delivered revenue.
5. **Bihar has the lowest revenue:** Bihar contributed 1.80% of delivered revenue, with 1,407 delivered orders.

## 5.3 Business Implications

- Sales are distributed across multiple states, but the top three states contribute a substantial share of revenue.
- Maharashtra represents an important geographical market.
- Differences in average order value and order volume indicate opportunities for state-specific marketing strategies.
- Lower-revenue states may require further investigation before additional investment.

## 5.4 Recommendations

1. Strengthen customer acquisition and retention strategies in Maharashtra, Uttar Pradesh, and Gujarat.
2. Analyse customer preferences and product demand separately for each state.
3. Investigate the factors contributing to Telangana's relatively high average order value.
4. Evaluate delivery coverage, marketing reach, and product availability in lower-revenue states.
5. Develop region-specific promotions instead of applying identical campaigns across all states.

---

# 6. Operations, Payments and Returns Insights

This section evaluates order fulfilment, delivery performance, payment outcomes, refunds, and product returns.

## 6.1 Delivery Performance

| Metric | Result |
|---|---:|
| Total Shipments | 89,681 |
| Average Delivery Time | 4.10 days |
| Delayed Shipments | 37,448 |
| Delayed Shipment Rate | 41.76% |

### Key Observations

1. Approximately 41.76% of shipments were flagged as delayed.
2. Average delivery time was 4.10 days.
3. Delivery delays may affect customer satisfaction and repeat purchasing behaviour.

### Business Implications

- Delivery reliability is an important area for operational improvement.
- Delayed shipments may contribute to negative customer experiences.
- Delivery performance should be monitored across states and shipping methods.

### Recommendations

1. Identify states and shipping methods with the highest delay rates.
2. Review logistics partner performance.
3. Monitor expected versus actual delivery dates.
4. Improve shipment tracking and proactively communicate delivery delays.
5. Establish operational targets for reducing delayed shipments.

## 6.2 Payment Performance

| Payment Status | Number of Payments |
|---|---:|
| Success | 82,137 |
| Refunded | 10,690 |
| Failed | 5,068 |
| Not Charged | 1,876 |
| Pending | 229 |
| **Total** | **100,000** |

**Total payment refunds:** 268,740,811.64

### Key Observations

1. Successful payments accounted for 82,137 of the 100,000 payment records.
2. There were 5,068 failed payment records.
3. The dataset also contains refunded, pending, and not-charged payment records.
4. Total refunds recorded in the payments dataset were 268,740,811.64.

### Business Implications

- Failed payments represent potential lost order opportunities.
- Refund activity requires monitoring to understand its effect on cash flow.
- Payment failures may create friction in the customer purchasing journey.

### Recommendations

1. Investigate common payment failure reasons.
2. Monitor payment success rates by payment method.
3. Improve payment retry and recovery mechanisms where appropriate.
4. Reconcile payment refunds with order and return records.
5. Monitor pending transactions to identify unresolved payments.

## 6.3 Product Returns Analysis

| Metric | Result |
|---|---:|
| Total Returns | 12,075 |
| Total Return Refund Amount | 105,898,381.80 |
| Size-related Return Issues | 18.23% |

### Key Observations

1. The dataset contains 12,075 return records.
2. Return refunds totalled 105,898,381.80.
3. Size-related issues accounted for 18.23% of recorded return reasons.

### Business Implications

- Returns create additional costs and operational workload.
- Size-related issues indicate an opportunity to improve product information and customer expectations.
- Return patterns can help identify products that require quality or description improvements.

### Recommendations

1. Improve size guides and product measurement information.
2. Analyse return reasons by product category and individual product.
3. Identify products with unusually high return rates.
4. Improve product descriptions and images to reduce expectation mismatches.
5. Monitor return and refund trends regularly.

## 6.4 Important Measurement Notes

- Shipment delay rate is based on the `delayed_flag` field.
- Payment refund totals and return refund totals come from separate datasets and should not be added together without checking for overlapping transactions.
- Payment records, shipment records, and return records represent different operational events and should not be treated as interchangeable counts.

---

# 7. Marketing Effectiveness Insights

Marketing analysis evaluated 151 campaigns across multiple channels and campaign types.

The analysis focused on campaign spending, attributed revenue, return on ad spend (ROAS), click-through rate, conversion rate, and cost per conversion.

## 7.1 Overall Marketing Performance

| Metric | Result |
|---|---:|
| Total Campaigns | 151 |
| Total Impressions | 9,217,314 |
| Total Clicks | 294,369 |
| Total Conversions | 17,179 |
| Total Campaign Spend | 187,120,911.26 |
| Campaign-Attributed Revenue | 436,296,290.91 |
| Overall ROAS | 2.33 |
| Click-Through Rate | 3.19% |
| Conversion Rate | 5.84% |
| Cost per Conversion | 10,892.42 |

## 7.2 Channel-wise Marketing Performance

| Channel | Campaigns | Revenue | ROAS |
|---|---:|---:|---:|
| Organic Search | 12 | 76,657,402.30 | 5.31 |
| Paid Search | 18 | 68,579,569.86 | 1.89 |
| Referral | 19 | 47,788,369.16 | 5.09 |
| Direct/App | 13 | 47,237,718.46 | 6.20 |
| Email Marketing | 17 | 45,183,437.39 | 2.11 |
| Social Media - Facebook | 14 | 40,903,884.87 | 1.08 |
| Social Media - Instagram | 15 | 37,169,639.95 | 2.09 |
| Influencer Marketing | 15 | 31,249,377.81 | 1.32 |
| Affiliate | 14 | 24,418,954.99 | 2.22 |
| SMS Marketing | 14 | 17,107,936.12 | 2.29 |

## 7.3 Campaign-type Performance

| Campaign Type | Campaigns | Revenue | ROAS |
|---|---:|---:|---:|
| Loyalty Program | 32 | 84,733,604.79 | 1.68 |
| New Product Launch | 26 | 66,370,639.84 | 1.60 |
| Retargeting | 15 | 63,105,271.28 | 4.19 |
| Festival Special | 17 | 50,404,130.00 | 2.69 |
| Flash Sale | 17 | 48,681,804.63 | 2.47 |
| Seasonal Sale | 18 | 48,150,975.12 | 2.43 |
| Clearance Sale | 14 | 45,689,490.20 | 3.51 |
| Brand Awareness | 12 | 29,160,375.05 | 3.27 |

## 7.4 Loss-Making Campaigns

The analysis identified 9 campaigns where campaign cost exceeded campaign-attributed revenue.

The largest revenue shortfalls included:

| Campaign | Channel | Revenue Minus Cost | ROAS |
|---|---|---:|---:|
| CAMP1145 | Email Marketing | -4,860,856.01 | 0.62 |
| CAMP1100 | Social Media - Facebook | -4,830,326.87 | 0.47 |
| CAMP1136 | Influencer Marketing | -3,978,241.75 | 0.40 |
| CAMP1039 | Social Media - Facebook | -3,435,517.89 | 0.40 |
| CAMP1045 | Paid Search | -2,997,985.81 | 0.59 |

## 7.5 Key Observations

1. **Strong Direct/App performance:** Direct/App recorded the highest channel ROAS of 6.20.
2. **Organic Search performance:** Organic Search generated the highest channel revenue of 76.66 million.
3. **Referral effectiveness:** Referral recorded a ROAS of 5.09.
4. **Retargeting effectiveness:** Retargeting achieved the highest campaign-type ROAS of 4.19.
5. **Facebook performance concern:** Facebook recorded a relatively low ROAS of 1.08.
6. **Campaign losses:** Nine campaigns generated less attributed revenue than their campaign costs.

## 7.6 Business Implications

- Marketing channels differ significantly in their ability to generate attributed revenue relative to spending.
- Direct/App, Organic Search, and Referral are strong-performing channels based on ROAS.
- Retargeting appears particularly effective among the campaign types analysed.
- Low-performing campaigns require investigation before further investment.
- High campaign revenue does not necessarily indicate high marketing efficiency.

## 7.7 Recommendations

1. Evaluate opportunities to increase investment in Direct/App, Organic Search, and Referral.
2. Investigate the effectiveness of Retargeting campaigns and identify repeatable strategies.
3. Review spending on low-ROAS Facebook and Influencer Marketing campaigns.
4. Investigate all nine loss-making campaigns individually.
5. Monitor ROAS, CTR, conversion rate, and cost per conversion together.
6. Conduct campaign-level performance reviews before renewing marketing budgets.

**Measurement note:** ROAS is calculated as total campaign-attributed revenue divided by total campaign cost. Campaign-attributed revenue is not necessarily equivalent to independently verified incremental revenue or accounting profit.

---

# 8. Consolidated Business Problems Identified

Based on the analysis, the following business challenges and improvement opportunities were identified.

| No. | Business Problem | Supporting Evidence | Potential Business Impact |
|---|---|---|---|
| 1 | Customer churn | 13,365 customers classified as churned | Reduced repeat revenue and customer lifetime value |
| 2 | Retention improvement needed | Retention declined from 39.24% to 38.92% | Difficulty maintaining existing customers |
| 3 | Low overall product margin | Overall item profit margin of 7.99% | Limited profitability relative to sales |
| 4 | Electronics profitability concern | Electronics margin of 0.60% | High revenue with relatively low profit contribution |
| 5 | Delivery delays | 41.76% of shipments flagged as delayed | Potential customer dissatisfaction |
| 6 | Payment failures | 5,068 failed payment records | Lost or interrupted transactions |
| 7 | Product returns | 12,075 return records | Additional logistics and refund costs |
| 8 | Marketing inefficiency | 9 campaigns had revenue below campaign cost | Inefficient allocation of marketing budgets |
| 9 | Channel performance variation | Direct/App ROAS of 6.20 versus Facebook ROAS of 1.08 | Uneven marketing returns |
| 10 | Geographical concentration | Top three states contributed approximately 35.59% of delivered revenue | Dependence on a limited number of major markets |

These findings identify areas that require further investigation and targeted business action.

---

# 9. Strategic Business Recommendations

The following recommendations consolidate the findings from sales, customer, product, geographical, operational, and marketing analysis.

## 9.1 Improve Customer Retention

- Introduce loyalty programmes for repeat customers.
- Develop targeted reactivation campaigns for churned customers.
- Provide personalised offers to premium customers.
- Monitor customer retention and repeat-purchase behaviour regularly.

## 9.2 Improve Product Profitability

- Review pricing and supplier costs in low-margin categories.
- Investigate the low profitability of Electronics and Appliances.
- Prioritise profitable product categories where demand supports expansion.
- Monitor product-level revenue, cost, and profit margins.

## 9.3 Improve Delivery Operations

- Identify the causes of delayed shipments.
- Evaluate logistics partners and shipping methods.
- Monitor delivery performance across different states.
- Improve shipment tracking and delivery communication.

## 9.4 Reduce Payment and Return Issues

- Investigate recurring payment failure patterns.
- Improve payment recovery mechanisms.
- Analyse return reasons by product and category.
- Improve product information to reduce avoidable returns.

## 9.5 Optimise Marketing Spending

- Evaluate scaling opportunities in high-ROAS channels.
- Review low-performing campaigns before allocating additional budgets.
- Investigate campaigns with ROAS below 1.
- Prioritise performance measurement using ROAS, CTR, conversion rate, and cost per conversion.

## 9.6 Strengthen Geographical Strategy

- Maintain strong performance in major revenue-generating states.
- Analyse demand and customer behaviour at the state level.
- Investigate growth opportunities in lower-revenue markets.
- Align marketing, inventory, and delivery strategies with regional demand.

## 9.7 Establish Continuous Business Monitoring

- Track sales and revenue growth monthly.
- Monitor retention and churn rates.
- Review product profitability regularly.
- Monitor shipment delays and return trends.
- Evaluate marketing campaign effectiveness through consistent KPIs.

---

# 10. Conclusion

India Commerce Intelligence demonstrates how raw e-commerce datasets can be transformed into meaningful business insights using data cleaning, exploratory data analysis, SQL, PostgreSQL, and business intelligence dashboards.

The project analysed 659,318 records across nine datasets and examined key business areas including sales, customers, products, geographical performance, operations, payments, returns, and marketing.

The analysis identified several important findings:

- Delivered revenue grew by 68.16% in 2025 compared with 2024.
- Repeat customers represented 78.25% of customers with delivered orders.
- The overall delivered item profit margin was 7.99%.
- Maharashtra was the highest revenue-generating state.
- 41.76% of shipments were flagged as delayed.
- Marketing campaigns achieved an overall ROAS of 2.33.
- Nine marketing campaigns generated less attributed revenue than their campaign costs.

These findings highlight opportunities to improve customer retention, product profitability, delivery reliability, payment performance, and marketing efficiency.

The project also demonstrates the practical application of a complete analytics workflow, from raw data processing and validation to SQL-based business analysis and interactive dashboard development.

**Overall, India Commerce Intelligence provides a structured analytical foundation for understanding e-commerce performance and supporting data-driven business decisions.**

---

# Appendix A: Technical Implementation

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Data processing and analysis |
| Pandas | Data cleaning and transformation |
| NumPy | Numerical operations |
| PostgreSQL | Relational data storage |
| SQL | Business analysis and reporting |
| Metabase | Interactive dashboards and visualisation |
| Docker | Containerised database and BI services |
| GitHub | Version control and project management |

## Dataset Overview

| Dataset | Records |
|---|---:|
| Customers | 25,000 |
| Orders | 100,000 |
| Products | 550 |
| Order Items | 254,331 |
| Payments | 100,000 |
| Shipments | 89,681 |
| Returns | 12,075 |
| Customer Reviews | 77,530 |
| Marketing Campaigns | 151 |
| **Total** | **659,318** |

## Advanced SQL Analysis Files

The project includes seven SQL analysis files:

1. `01_monthly_revenue_growth.sql`
2. `02_yearly_revenue_growth.sql`
3. `03_customer_retention.sql`
4. `04_repeat_customer_analysis.sql`
5. `05_product_profitability.sql`
6. `06_state_wise_sales.sql`
7. `07_marketing_effectiveness.sql`

## Business Intelligence Dashboards

Three Metabase dashboards were developed:

1. **India Commerce Intelligence – Executive Dashboard:** Sales KPIs, order status distribution, delivery state performance, and product category revenue.
2. **Customer & Product Analytics:** Customer KPIs, customer segmentation, revenue by customer segment, and product analytics.
3. **Operations, Payments, Returns & Marketing:** Fulfilment, payment performance, returns, and marketing effectiveness.

---

# Appendix B: Metric Definitions and Scope

| Metric | Definition |
|---|---|
| Delivered Revenue | Sum of `orders.final_amount` for Delivered orders |
| Average Order Value | Average `orders.final_amount` for Delivered orders |
| Revenue Growth | Percentage change in delivered revenue from the previous period |
| Retention Rate | Retained customers divided by previous-year active customers |
| Repeat Customer Rate | Customers with more than one delivered order divided by customers with delivered orders |
| Product Profit | Sum of `order_items.profit` for items belonging to Delivered orders |
| Product Profit Margin | Delivered item profit divided by delivered item revenue |
| Revenue Contribution | State delivered revenue divided by total delivered revenue |
| Delayed Shipment Rate | Delayed shipments divided by total shipments |
| ROAS | Total campaign-attributed revenue divided by total campaign cost |
| CTR | Total clicks divided by total impressions |
| Conversion Rate | Total conversions divided by total clicks |
| Cost per Conversion | Total campaign cost divided by total conversions |

**Data interpretation notes:**

- Financial amounts are reported in the source dataset's units. Currency has not been independently verified.
- Delivered order revenue and delivered item revenue are separate measures.
- Campaign-attributed revenue is not necessarily incremental revenue.
- Payment refunds and return refunds are separate measures and may overlap.
- Customer retention analysis uses delivered-order activity observed during 2023–2025.
- The customer status and segment classifications are taken from the customer dataset.
- Findings are based on the available dataset and do not establish causal relationships.

**End of Report**