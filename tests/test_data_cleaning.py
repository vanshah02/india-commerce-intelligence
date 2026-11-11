
import pandas as pd
import pytest

from src import data_cleaning as dc


def make_datasets():
    """Create small test datasets without using project CSV files."""
    return {
        "customers": pd.DataFrame({
            "customer_signup_date": ["2025-01-01"],
            "last_order_date": ["2025-02-01"],
            "age": [None,],
            "preferred_device": [None],
        }),
        "orders": pd.DataFrame({
            "order_date": ["2025-01-10"]
        }),
        "products": pd.DataFrame({
            "product_launch_date": ["2024-01-01"],
            "rating_average": [None],
        }),
        "order_items": pd.DataFrame({
            "quantity": [2]
        }),
        "payments": pd.DataFrame({
            "payment_date": ["2025-01-11"]
        }),
        "shipments": pd.DataFrame({
            "dispatch_date": ["2025-01-12"],
            "expected_delivery_date": ["2025-01-15"],
            "actual_delivery_date": ["2025-01-14"],
        }),
        "returns": pd.DataFrame({
            "return_date": ["2025-01-20"]
        }),
        "customer_reviews": pd.DataFrame({
            "review_date": ["2025-01-21"],
            "review_sentiment": [None],
        }),
        "marketing_campaigns": pd.DataFrame({
            "campaign_start_date": ["2025-01-01"],
            "campaign_end_date": ["2025-01-31"],
        }),
    }


def test_load_dataset_success(tmp_path, monkeypatch):
    raw_dir = tmp_path / "raw"
    raw_dir.mkdir()

    pd.DataFrame({"id": [1, 2]}).to_csv(
        raw_dir / "customers.csv", index=False
    )

    monkeypatch.setattr(dc, "RAW_DIR", raw_dir)

    result = dc.load_dataset("customers.csv")

    assert len(result) == 2
    assert list(result.columns) == ["id"]


def test_load_dataset_missing_file(tmp_path, monkeypatch):
    monkeypatch.setattr(dc, "RAW_DIR", tmp_path)

    with pytest.raises(FileNotFoundError):
        dc.load_dataset("missing.csv")


def test_convert_date_columns():
    datasets = make_datasets()

    dc.convert_date_columns(datasets)

    assert pd.api.types.is_datetime64_any_dtype(
        datasets["orders"]["order_date"]
    )

    assert pd.api.types.is_datetime64_any_dtype(
        datasets["shipments"]["actual_delivery_date"]
    )


def test_standardize_text_columns():
    datasets = {
        "customers": pd.DataFrame({
            "name": ["  Vansh   Shah  ", "  Rahul  "],
            "city": [" Mumbai ", ""],
        })
    }

    dc.standardize_text_columns(datasets)

    assert datasets["customers"]["name"].tolist() == [
        "Vansh Shah", "Rahul"
    ]

    assert pd.isna(datasets["customers"]["city"].iloc[1])


def test_handle_missing_values():
    datasets = make_datasets()

    datasets["customers"]["age"] = [20]
    datasets["products"]["rating_average"] = [4.0]

    dc.handle_missing_values(datasets)

    assert datasets["customers"]["age"].isna().sum() == 0
    assert datasets["products"]["rating_average"].isna().sum() == 0

    assert datasets["customers"]["preferred_device"].iloc[0] == "Unknown"
    assert datasets["customer_reviews"]["review_sentiment"].iloc[0] == "Unknown"


def test_validate_datasets_success():
    datasets = make_datasets()

    dc.convert_date_columns(datasets)

    original_shapes = {
        name: df.shape for name, df in datasets.items()
    }

    dc.validate_datasets(datasets, original_shapes)


def test_validate_datasets_detects_duplicate():
    datasets = {
        "customers": pd.DataFrame({
            "customer_id": [1, 1]
        })
    }

    original_shapes = {
        "customers": (2, 1)
    }

    with pytest.raises(AssertionError, match="Duplicate rows"):
        dc.validate_datasets(datasets, original_shapes)


def test_save_processed_datasets(tmp_path, monkeypatch):
    datasets = {
        "customers": pd.DataFrame({
            "customer_id": [1, 2]
        })
    }

    monkeypatch.setattr(dc, "PROCESSED_DIR", tmp_path)

    dc.save_processed_datasets(datasets)

    saved_file = tmp_path / "customers.csv"

    assert saved_file.exists()

    result = pd.read_csv(saved_file)

    assert len(result) == 2
    assert result["customer_id"].tolist() == [1, 2]

