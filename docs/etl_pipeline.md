# ETL Pipeline Documentation

## 1. Overview
The ETL pipeline processes raw e-commerce CSV datasets and loads clean, analysis-ready records into PostgreSQL.

## 2. Extraction
- Source: Nine CSV datasets.
- Raw files are maintained separately.
- Python and Pandas are used to read the datasets.

## 3. Transformation
Implemented in src/data_cleaning.py.

Cleaning operations include:
- Date conversion into standard date formats.
- Whitespace trimming.
- Empty string conversion to missing values.
- Missing age values filled using the median.
- Missing product ratings filled using the median.
- Missing preferred device values set to Unknown.
- Missing review sentiment values set to Unknown.
- Data type standardisation and validation.

## 4. Processed Data
Cleaned datasets are stored in data/processed/.

The nine processed datasets contain 659,318 records in total.

## 5. Loading
Implemented in src/load_data.py.

Cleaned CSV datasets are loaded into PostgreSQL database india_commerce_dw.

## 6. Validation
- Verify that all nine tables exist.
- Compare database record counts with processed CSV record counts.
- Check date conversion and missing values.
- Validate important columns and relationships.

## 7. Exploratory Data Analysis
Implemented in src/eda.py.

EDA generates statistical summaries, business metrics and visualisations stored in reports/.

## 8. Advanced SQL Analysis
Seven SQL scripts are maintained in sql/analysis/:

1. Monthly revenue growth
2. Yearly revenue growth
3. Customer retention
4. Repeat customer analysis
5. Product profitability
6. State-wise sales
7. Marketing effectiveness

## 9. Output
The final outputs include:
- Cleaned CSV datasets
- PostgreSQL warehouse tables
- EDA reports and figures
- SQL analysis results
- Metabase dashboards
- Business insights report
