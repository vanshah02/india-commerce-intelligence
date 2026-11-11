
from pathlib import Path

import pandas as pd
from sqlalchemy import text

from db_connection import get_engine


PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT / "data" / "processed"

EXPECTED_FILES = [
    "customers.csv",
    "orders.csv",
    "products.csv",
    "order_items.csv",
    "payments.csv",
    "shipments.csv",
    "returns.csv",
    "customer_reviews.csv",
    "marketing_campaigns.csv",
]


def load_data():
    engine = get_engine()

    print("\nStarting CSV to PostgreSQL loading...\n")

    for filename in EXPECTED_FILES:
        file_path = DATA_DIR / filename

        if not file_path.exists():
            raise FileNotFoundError(f"Missing file: {file_path}")

        table_name = file_path.stem

        print(f"Loading {filename}...")

        df = pd.read_csv(file_path)

        df.to_sql(
            name=table_name,
            con=engine,
            schema="public",
            if_exists="replace",
            index=False,
            chunksize=1000,
        )

        print(f"Loaded {len(df):,} rows into {table_name}")

    print("\nVerifying database tables...\n")

    with engine.connect() as connection:
        for table_name in [Path(f).stem for f in EXPECTED_FILES]:
            result = connection.execute(
                text(f'SELECT COUNT(*) FROM public."{table_name}"')
            )
            count = result.scalar()

            print(f"{table_name}: {count:,} rows")

    print("\nAll nine datasets loaded successfully!")

    engine.dispose()


if __name__ == "__main__":
    load_data()
