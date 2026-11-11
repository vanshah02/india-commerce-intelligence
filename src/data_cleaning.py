
from pathlib import Path
import pandas as pd

# --------------------------------------------------
# 1. PROJECT PATHS
# --------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent
RAW_DIR = PROJECT_ROOT / "data" / "raw"
PROCESSED_DIR = PROJECT_ROOT / "data" / "processed"


# --------------------------------------------------
# 2. DATE COLUMNS
# --------------------------------------------------

DATE_COLUMNS = {
    "customers": [
        "customer_signup_date", "last_order_date"
    ],
    "orders": [
        "order_date"
    ],
    "products": [
        "product_launch_date"
    ],
    "payments": [
        "payment_date"
    ],
    "shipments": [
        "dispatch_date",
        "expected_delivery_date",
        "actual_delivery_date"
    ],
    "returns": [
        "return_date"
    ],
    "customer_reviews": [
        "review_date"
    ],
    "marketing_campaigns": [
        "campaign_start_date",
        "campaign_end_date"
    ]
}


# --------------------------------------------------
# 3. MISSING VALUE STRATEGY
# --------------------------------------------------

NUMERIC_FILL_COLUMNS = {
    "customers": ["age"],
    "products": ["rating_average"]
}

CATEGORY_FILL_COLUMNS = {
    "customers": ["preferred_device"],
    "customer_reviews": ["review_sentiment"]
}


# --------------------------------------------------
# 4. LOAD DATASETS
# --------------------------------------------------

def create_processed_directory():
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)


def load_dataset(filename):
    file_path = RAW_DIR / filename

    if not file_path.exists():
        raise FileNotFoundError(f"Dataset not found: {file_path}")

    return pd.read_csv(file_path)


def load_all_datasets():
    filenames = [
        "customers",
        "orders",
        "products",
        "order_items",
        "payments",
        "shipments",
        "returns",
        "customer_reviews",
        "marketing_campaigns"
    ]

    return {
        name: load_dataset(f"{name}.csv")
        for name in filenames
    }


# --------------------------------------------------
# 5. CONVERT DATE COLUMNS
# --------------------------------------------------

def convert_date_columns(datasets):
    print("\nDATE CONVERSION")

    for name, columns in DATE_COLUMNS.items():
        df = datasets[name]

        for column in columns:
            df[column] = pd.to_datetime(
                df[column],
                errors="coerce"
            )

    print("All identified date columns converted.")


# --------------------------------------------------
# 6. STANDARDIZE TEXT AND CATEGORIES
# --------------------------------------------------

def standardize_text_columns(datasets):
    print("\nTEXT STANDARDIZATION")

    for name, df in datasets.items():
        for column in df.columns:
            if pd.api.types.is_string_dtype(df[column]):
                df[column] = (
                    df[column]
                    .str.strip()
                    .str.replace(r"\s+", " ", regex=True)
                )

                # Convert empty strings into missing values
                df[column] = df[column].replace("", pd.NA)

    print("Text columns standardized.")


# --------------------------------------------------
# 7. HANDLE MISSING VALUES
# --------------------------------------------------

def handle_missing_values(datasets):
    print("\nMISSING VALUE HANDLING")

    # Fill selected numeric columns with their median
    for name, columns in NUMERIC_FILL_COLUMNS.items():
        df = datasets[name]

        for column in columns:
            median_value = df[column].median()
            df[column] = df[column].fillna(median_value)

            print(f"{name}.{column}: filled with median")

    # Fill selected categorical columns with Unknown
    for name, columns in CATEGORY_FILL_COLUMNS.items():
        df = datasets[name]

        for column in columns:
            df[column] = df[column].fillna("Unknown")

            print(f"{name}.{column}: filled with Unknown")

    print("Other missing values preserved.")


# --------------------------------------------------
# 8. VALIDATE CLEANED DATASETS
# --------------------------------------------------

def validate_datasets(datasets, original_shapes):
    print("\nDATA VALIDATION")

    for name, df in datasets.items():

        # Check row count
        assert len(df) == original_shapes[name][0], (
            f"Row count changed in {name}"
        )

        # Check duplicate rows
        assert not df.duplicated().any(), (
            f"Duplicate rows found in {name}"
        )

        # Check date column data types
        for column in DATE_COLUMNS.get(name, []):
            assert pd.api.types.is_datetime64_any_dtype(
                df[column]
            ), f"Date conversion failed: {name}.{column}"

        print(
            f"{name}: validation passed | "
            f"{len(df)} rows, {len(df.columns)} columns"
        )

    print("\nAll validation checks passed.")


# --------------------------------------------------
# 9. SAVE PROCESSED DATASETS
# --------------------------------------------------

def save_processed_datasets(datasets):
    print("\nSAVING PROCESSED DATASETS")

    for name, df in datasets.items():
        output_path = PROCESSED_DIR / f"{name}.csv"

        df.to_csv(output_path, index=False)

        print(f"Saved: {output_path.name}")

    print("\nAll nine processed datasets saved.")


# --------------------------------------------------
# 10. MAIN EXECUTION
# --------------------------------------------------

if __name__ == "__main__":

    create_processed_directory()

    datasets = load_all_datasets()

    original_shapes = {
        name: df.shape
        for name, df in datasets.items()
    }

    print("\nDATASET LOADING SUMMARY")

    for name, df in datasets.items():
        print(f"{name}: {df.shape[0]} rows, {df.shape[1]} columns")

    convert_date_columns(datasets)

    standardize_text_columns(datasets)

    handle_missing_values(datasets)

    validate_datasets(datasets, original_shapes)

    save_processed_datasets(datasets)

    print("\nPHASE 2 DATA CLEANING COMPLETED SUCCESSFULLY.")
