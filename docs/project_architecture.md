# Project Architecture — India Commerce Intelligence

## 1. Architecture Overview

The project follows a data analytics architecture:

Raw CSV Files
    ↓
Python Data Extraction
    ↓
Data Cleaning and Transformation
    ↓
Processed CSV Files
    ↓
PostgreSQL Data Warehouse
    ↓
SQL Business Analysis
    ↓
Metabase Dashboards and Reports
    ↓
Business Insights and Recommendations

## 2. Architecture Components

### Data Source Layer
Nine synthetic e-commerce datasets covering customers, orders, products, order items, payments, shipments, returns, reviews and campaigns.

### Processing Layer
Python and Pandas perform data cleaning, transformation and validation.

### Storage Layer
PostgreSQL 16 stores the nine relational datasets in india_commerce_dw.

### Analytics Layer
SQL queries calculate business metrics and analyse sales, customers, products, geographical performance and marketing.

### Visualisation Layer
Metabase provides three interactive dashboards:
1. Executive Dashboard
2. Customer & Product Analytics
3. Operations, Payments, Returns & Marketing

### Reporting Layer
Python EDA reports, SQL findings and the Business Insights Report communicate analytical results.

## 3. Infrastructure
- Docker runs PostgreSQL and Metabase containers.
- PostgreSQL container: pfw_postgres.
- Metabase container: pfw_metabase.
- Metabase is accessed locally at http://localhost:3000.

## 4. Project Structure

india-commerce-intelligence/
├── data/
│   ├── raw/
│   └── processed/
├── src/
│   ├── data_cleaning.py
│   ├── eda.py
│   └── load_data.py
├── sql/
│   ├── migrations/
│   └── analysis/
├── reports/
│   ├── figures/
│   ├── data_audit_findings.md
│   ├── eda_report.md
│   └── business_insights_report.md
├── docs/
│   ├── data_warehouse_documentation.md
│   ├── database_schema.md
│   ├── etl_pipeline.md
│   └── project_architecture.md
└── README.md

Note: This is a simplified project structure. Additional scripts, configuration files and dependencies may exist.
