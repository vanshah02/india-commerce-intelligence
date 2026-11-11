# India Commerce Intelligence
# Phase 1: Data Audit Findings

## 1. Project Overview

The project uses nine synthetic relational datasets representing an Indian e-commerce business.

The datasets cover business activities from January 2023 to December 2025.

The objective of the data audit was to assess data quality, identify inconsistencies, validate relationships, and understand the business data before performing data cleaning and transformation.

## 2. Dataset Overview

The project contains nine datasets:

1. Customers
2. Orders
3. Products
4. Order Items
5. Payments
6. Shipments
7. Returns
8. Customer Reviews
9. Marketing Campaigns

## 3. Data Quality Audit

The following checks were performed:

| Audit Check | Result |
|---|---|
| Dataset loading | All 9 datasets loaded successfully |
| Duplicate records | No duplicate rows identified |
| Duplicate primary IDs | No duplicate primary IDs identified |
| Referential integrity | 9 relationship checks completed |
| Financial consistency | 0 mismatches identified |
| Date validation | 7 date columns validated |
| Invalid dates | 0 invalid dates identified |

### 3.1 Referential Integrity

The following relationships were validated:

| Relationship | Invalid References |
|---|---:|
| Orders → Customers | 0 |
| Order Items → Orders | 0 |
| Order Items → Products | 0 |
| Payments → Orders | 0 |
| Shipments → Orders | 0 |
| Returns → Orders | 0 |
| Customer Reviews → Customers | 0 |
| Customer Reviews → Products | 0 |
| Orders → Marketing Campaigns | 0 |

All nine relationship checks passed.

## 4. Date Validation

All seven selected date columns were successfully validated.

| Dataset | Date Column | Earliest Date | Latest Date | Invalid Dates |
|---|---|---|---|---:|
| Customers | customer_signup_date | 2023-01-01 | 2025-12-31 | 0 |
| Orders | order_date | 2023-01-01 | 2025-12-31 | 0 |
| Products | product_launch_date | 2023-01-03 | 2025-12-27 | 0 |
| Shipments | dispatch_date | 2023-01-02 | 2025-12-31 | 0 |
| Returns | return_date | 2023-01-07 | 2025-12-31 | 0 |
| Customer Reviews | review_date | 2023-01-08 | 2025-12-31 | 0 |
| Marketing Campaigns | campaign_start_date | 2023-01-01 | 2025-12-08 | 0 |

No invalid or missing dates were identified in these selected columns.

## 5. Business Analysis Findings

### 5.1 Order Status Distribution

Total Orders: 100,000

| Order Status | Count | Percentage |
|---|---:|---:|
| Delivered | 80,679 | 80.68% |
| Cancelled | 8,073 | 8.07% |
| Returned | 6,681 | 6.68% |
| Failed | 2,880 | 2.88% |
| Processing | 1,687 | 1.69% |

Delivered orders represent the largest category.

### 5.2 Payment Status Distribution

Total Payment Records: 100,000

| Payment Status | Count | Percentage |
|---|---:|---:|
| Success | 82,137 | 82.14% |
| Refunded | 10,690 | 10.69% |
| Failed | 5,068 | 5.07% |
| Not Charged | 1,876 | 1.88% |
| Pending | 229 | 0.23% |

Successful payments represent the largest category.

### 5.3 Shipment Status Distribution

Total Shipment Records: 89,681

| Delivery Status | Count | Percentage |
|---|---:|---:|
| Delivered | 80,679 | 89.96% |
| Delivered then Returned | 6,681 | 7.45% |
| Cancelled in Transit | 2,321 | 2.59% |

Not every order has a shipment record.

### 5.4 Return Reason Analysis

Total Return Records: 12,075

| Return Reason | Count | Percentage |
|---|---:|---:|
| Size issue | 2,201 | 18.23% |
| Changed mind | 1,984 | 16.43% |
| Product damaged | 1,933 | 16.01% |
| Quality issue | 1,692 | 14.01% |
| Product not as expected | 1,442 | 11.94% |
| Wrong product | 1,394 | 11.54% |
| Late delivery | 960 | 7.95% |
| Other | 469 | 3.88% |

Size issues were the most frequently recorded return reason.

### 5.5 Customer Review Analysis

Total Customer Reviews: 77,530

Average Customer Rating: 3.69 out of 5

| Rating | Reviews | Percentage |
|---|---:|---:|
| 1 Star | 700 | 0.90% |
| 2 Stars | 6,311 | 8.14% |
| 3 Stars | 24,208 | 31.22% |
| 4 Stars | 31,265 | 40.33% |
| 5 Stars | 15,046 | 19.41% |

Four-star reviews represent the largest category.

### 5.6 Marketing Campaign Analysis

Total Marketing Campaigns: 151

Campaign types identified:

- Loyalty Program: 32
- New Product Launch: 26
- Seasonal Sale: 18
- Festival Special: 17
- Flash Sale: 17
- Retargeting: 15
- Clearance Sale: 14
- Brand Awareness: 12

Ten marketing channels were identified.

### 5.7 Marketing Financial Summary

| Metric | Value |
|---|---:|
| Total Campaign Cost | 187,120,911.26 |
| Total Revenue Generated | 436,296,290.91 |
| Total Conversions | 17,179 |
| Total Impressions | 9,217,314 |
| Total Clicks | 294,369 |

### 5.8 Marketing Performance KPIs

| KPI | Result |
|---|---:|
| Click-Through Rate (CTR) | 3.19% |
| Conversion Rate | 5.84% |
| Cost per Conversion | 10,892.42 |
| Average Campaign ROI | 2.406 |
| Median Campaign ROI | 1.935 |
| Minimum Campaign ROI | -0.600 |
| Maximum Campaign ROI | 7.639 |

These metrics provide a baseline for future marketing performance analysis.

## 6. Missing Value Findings

Missing values were identified during the initial audit.

Some missing values are expected because of business logic, such as:

- Customers who have never placed an order may not have a last order date.
- Orders may not have coupon or campaign information.
- Shipments cancelled in transit may not have actual delivery dates.
- Some products may not have ratings.
- Some customer records may have incomplete demographic information.

Other missing values will be investigated and handled according to the audit findings during Phase 2.

No original raw data will be overwritten.

## 7. Important Business Observations

The initial audit identified several areas for further analysis:

1. Delivered orders account for 80.68% of all orders.
2. Size issues are the leading recorded return reason.
3. Product damage and quality issues together account for 30.02% of returns.
4. The average customer review rating is 3.69 out of 5.
5. Marketing campaigns generated 436,296,290.91 in attributed revenue against 187,120,911.26 in campaign expenditure.
6. Marketing performance varies across campaigns and channels.

These observations are based on synthetic data and should be treated as analytical findings rather than actual business performance.

## 8. Audit Conclusion

The initial data audit has been completed successfully.

The nine datasets were examined for structural quality, duplicate records, primary key uniqueness, referential integrity, financial consistency, date validity, missing values, and business distributions.

The nine referential integrity checks returned zero invalid references.

The seven selected date columns contained zero invalid or missing dates.

The original CSV files will be preserved in the `data/raw/` directory.

## 9. Next Phase: Data Cleaning and Transformation

Phase 2 will focus on:

1. Creating `src/data_cleaning.py`.
2. Converting date columns into appropriate datetime formats.
3. Handling missing values based on the audit findings.
4. Standardizing categorical columns.
5. Correcting data types.
6. Performing post-cleaning validation.
7. Saving cleaned datasets in `data/processed/`.

**Final Objective:** Create clean, consistent, analysis-ready datasets while preserving all original raw CSV files.