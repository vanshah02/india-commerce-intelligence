# India Commerce Intelligence

**End-to-End E-Commerce Data Analytics & Business Intelligence Platform**

An end-to-end analytics project analysing Indian e-commerce activity from January 2023 to December 2025 using Python, PostgreSQL, SQL, Docker and Metabase.

## Project Overview

This project transforms raw e-commerce datasets into actionable business insights through data cleaning, exploratory data analysis, SQL analytics and interactive dashboards.

### Technology Stack

- Python, Pandas, NumPy
- PostgreSQL 16
- SQL
- Metabase
- Docker
- Git and GitHub

## Dataset Overview

Nine synthetic datasets containing **659,318 records**:

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

## Project Workflow

1. Extract raw CSV datasets.
2. Clean and transform data using Python.
3. Store processed datasets in PostgreSQL.
4. Perform exploratory data analysis.
5. Execute advanced SQL analysis.
6. Build interactive Metabase dashboards.
7. Generate business insights and recommendations.

## Advanced SQL Analysis

Seven SQL scripts covering:

1. Monthly Revenue Growth
2. Yearly Revenue Growth
3. Customer Retention
4. Repeat Customer Analysis
5. Product Profitability
6. State-wise Sales
7. Marketing Effectiveness

Techniques include CTEs, aggregate functions, window functions, date functions and conditional calculations.

## Key Business Findings

| Metric | Result |
|---|---:|
| Total Orders | 100,000 |
| Delivered Orders | 80,679 |
| Delivered Order Revenue | 2,084,309,803.30 |
| 2025 Revenue Growth | 68.16% |
| Repeat Customer Rate | 78.25% |
| Delivered Item Profit Margin | 7.99% |
| Average Delivery Time | 4.10 days |
| Delayed Shipment Rate | 41.76% |
| Marketing ROAS | 2.33 |

## Metabase Dashboards

Three dashboards:

1. **Executive Dashboard** — Sales KPIs, order status, geographical performance and category revenue.
2. **Customer & Product Analytics** — Customer segmentation, customer performance and product analytics.
3. **Operations, Payments, Returns & Marketing** — Fulfilment, payments, returns and campaign effectiveness.

## Repository Structure

```text
india-commerce-intelligence/
├── data/
│   ├── raw/
│   └── processed/
├── src/
├── sql/
│   ├── migrations/
│   └── analysis/
├── reports/
├── docs/
├── notebooks/
├── requirements.txt
├── .gitignore
└── README.md
```

## Getting Started

### Prerequisites

- Python
- Docker Desktop
- Git

### Installation

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd india-commerce-intelligence

python3 -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
```

Configure your local `.env` file with the required database settings.

### Run the Pipeline

```bash
python src/data_cleaning.py
python src/eda.py
python src/load_data.py
```

Run SQL scripts from `sql/analysis/` against the PostgreSQL database.

Access Metabase at:

`http://localhost:3000`

**Note:** Raw and processed CSV datasets are excluded from this repository. Obtain the datasets separately before running the complete pipeline.

## Documentation

See the `docs/` directory for:

- Data Warehouse Documentation
- Database Schema
- ETL Pipeline
- Project Architecture

Analytical reports are available in `reports/`.

## Future Enhancements

- Automated ETL scheduling
- Data quality monitoring
- Incremental data loading
- Sales forecasting
- Customer lifetime value analysis
- Predictive analytics

## Author

**Vansh Shah**  
Information Technology Engineering  
Dwarkadas J. Sanghvi College of Engineering

*Educational and portfolio project using synthetic e-commerce data.*