# India Commerce Intelligence — Data Warehouse Documentation

## 1. Project Overview
India Commerce Intelligence is an e-commerce analytics platform covering January 2023 to December 2025.

The project analyses 659,318 records across nine datasets to identify business insights related to sales, customers, products, operations, returns, payments and marketing.

## 2. Technology Stack
- Python
- Pandas and NumPy
- PostgreSQL 16
- SQL
- Metabase
- Docker
- Git and GitHub

## 3. Database Information
- Database: india_commerce_dw
- Database engine: PostgreSQL 16
- Tables: 9
- Total records: 659,318

## 4. Database Tables

| Table | Records | Purpose |
|---|---:|---|
| customers | 25,000 | Customer information |
| orders | 100,000 | Order transactions |
| products | 550 | Product catalogue |
| order_items | 254,331 | Individual order line items |
| payments | 100,000 | Payment transactions |
| shipments | 89,681 | Shipment and delivery details |
| returns | 12,075 | Product return records |
| customer_reviews | 77,530 | Customer feedback |
| marketing_campaigns | 151 | Marketing campaign performance |

## 5. Data Processing
Raw CSV files are preserved. Python scripts perform cleaning, transformation, validation and loading into PostgreSQL.

## 6. Analytics
Exploratory analysis is performed using Python. Advanced SQL analysis covers monthly and yearly revenue, retention, repeat purchases, profitability, state-wise sales and marketing effectiveness.

## 7. Business Intelligence
Three Metabase dashboards provide executive, customer/product, and operations/marketing insights.

## 8. Project Outcomes
The project provides an end-to-end analytics workflow from raw datasets to cleaned data, a relational database, SQL analysis and interactive dashboards.
