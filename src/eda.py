from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# Project paths
PROJECT_ROOT = Path(__file__).resolve().parent.parent
PROCESSED_DIR = PROJECT_ROOT / "data" / "processed"

# Load all cleaned datasets
def load_datasets():
    datasets = {}

    for file_path in PROCESSED_DIR.glob("*.csv"):
        name = file_path.stem
        datasets[name] = pd.read_csv(file_path)

    return datasets


# Display overall dataset information
def dataset_overview(datasets):
    print("\n" + "=" * 60)
    print("EXPLORATORY DATA ANALYSIS - DATASET OVERVIEW")
    print("=" * 60)

    total_rows = 0

    for name, df in datasets.items():
        rows, columns = df.shape
        total_rows += rows

        print(f"\nDataset: {name.upper()}")
        print(f"Rows: {rows:,}")
        print(f"Columns: {columns}")
        print(f"Duplicate rows: {df.duplicated().sum():,}")
        print(f"Missing values: {df.isnull().sum().sum():,}")

    print("\n" + "=" * 60)
    print(f"Total datasets: {len(datasets)}")
    print(f"Total records: {total_rows:,}")
    print("=" * 60)


# --------------------------------------------------
# SALES ANALYSIS
# --------------------------------------------------

def sales_analysis(datasets):

    orders = datasets["orders"].copy()
    order_items = datasets["order_items"].copy()

    orders["order_date"] = pd.to_datetime(
        orders["order_date"], errors="coerce"
    )

    print("\n" + "=" * 60)
    print("SALES PERFORMANCE ANALYSIS")
    print("=" * 60)

    # Overall sales KPIs
    total_orders = len(orders)
    total_revenue = orders["final_amount"].sum()
    average_order_value = orders["final_amount"].mean()

    delivered = orders[
        orders["order_status"].str.strip().str.lower() == "delivered"
    ]

    print(f"\nTotal Orders: {total_orders:,}")
    print(f"Total Order Value: {total_revenue:,.2f}")
    print(f"Average Order Value: {average_order_value:,.2f}")
    print(f"Delivered Orders: {len(delivered):,}")
    print(f"Delivered Revenue: {delivered['final_amount'].sum():,.2f}")

    # Order status distribution
    print("\nORDER STATUS DISTRIBUTION")

    status_summary = (
        orders["order_status"]
        .value_counts()
        .to_frame("Orders")
    )

    status_summary["Percentage"] = (
        status_summary["Orders"] / total_orders * 100
    )

    print(status_summary.round(2).to_string())

    # Monthly sales trends
    print("\nMONTHLY SALES TRENDS")

    orders["month"] = orders["order_date"].dt.to_period("M")

    monthly_sales = (
        orders.groupby("month")
        .agg(
            total_orders=("order_id", "count"),
            total_revenue=("final_amount", "sum")
        )
        .reset_index()
    )

    print(monthly_sales.to_string(index=False))

    # Order item revenue
    item_revenue = order_items["item_revenue"].sum()

    print("\nORDER ITEM ANALYSIS")
    print(f"Total Order Items: {len(order_items):,}")
    print(f"Total Item Revenue: {item_revenue:,.2f}")

    print("\n" + "=" * 60)


# --------------------------------------------------
# CUSTOMER ANALYSIS
# --------------------------------------------------

def customer_analysis(datasets):

    customers = datasets["customers"].copy()

    print("\n" + "=" * 60)
    print("CUSTOMER ANALYSIS")
    print("=" * 60)

    # Overall customer KPIs
    print("\nCUSTOMER OVERVIEW")
    print(f"Total Customers: {len(customers):,}")
    print(f"Total Customer Spend: {customers['total_spend'].sum():,.2f}")
    print(f"Average Customer Spend: {customers['total_spend'].mean():,.2f}")
    print(f"Average Orders per Customer: {customers['total_orders'].mean():.2f}")

    # Customer segment analysis
    print("\nCUSTOMER SEGMENT DISTRIBUTION")

    segment_summary = (
        customers.groupby("customer_segment")
        .agg(
            customers=("customer_id", "count"),
            average_spend=("total_spend", "mean"),
            total_spend=("total_spend", "sum")
        )
        .sort_values("total_spend", ascending=False)
    )

    print(segment_summary.round(2).to_string())

    # Customer status
    print("\nCUSTOMER STATUS DISTRIBUTION")
    print(customers["customer_status"].value_counts().to_string())

    # State-wise customer distribution
    print("\nTOP 10 STATES BY CUSTOMER COUNT")

    state_summary = (
        customers["state"]
        .value_counts()
        .head(10)
    )

    print(state_summary.to_string())

    # Loyalty tier analysis
    print("\nLOYALTY TIER DISTRIBUTION")

    loyalty_summary = (
        customers.groupby("loyalty_tier")
        .agg(
            customers=("customer_id", "count"),
            average_spend=("total_spend", "mean")
        )
        .sort_values("average_spend", ascending=False)
    )

    print(loyalty_summary.round(2).to_string())

    print("\n" + "=" * 60)



# --------------------------------------------------
# PRODUCT ANALYSIS
# --------------------------------------------------

def product_analysis(datasets):

    products = datasets["products"].copy()
    order_items = datasets["order_items"].copy()

    # Connect product information with sales
    product_sales = order_items.merge(
        products,
        on="product_id",
        how="left"
    )

    # Standardise brand names
    product_sales["brand"] = (
    product_sales["brand"]
    .astype("string")
    .str.strip()
    .str.rstrip(",")
    .str.strip()
)
    

    print("\n" + "=" * 60)
    print("PRODUCT PERFORMANCE ANALYSIS")
    print("=" * 60)

    # Overall product KPIs
    print(f"\nTotal Products: {len(products):,}")
    print(f"Total Product Categories: {products['category'].nunique()}")
    print(f"Total Brands: {products['brand'].nunique()}")

    # Top 10 products by revenue
    print("\nTOP 10 PRODUCTS BY REVENUE")

    top_revenue = (
        product_sales.groupby("product_name")
        .agg(
            total_revenue=("item_revenue", "sum"),
            quantity_sold=("quantity", "sum")
        )
        .sort_values("total_revenue", ascending=False)
        .head(10)
    )

    print(top_revenue.round(2).to_string())

    # Top 10 products by quantity
    print("\nTOP 10 PRODUCTS BY QUANTITY SOLD")

    top_quantity = (
        product_sales.groupby("product_name")
        .agg(quantity_sold=("quantity", "sum"))
        .sort_values("quantity_sold", ascending=False)
        .head(10)
    )

    print(top_quantity.to_string())

    # Category performance
    print("\nCATEGORY PERFORMANCE")

    category_summary = (
        product_sales.groupby("category")
        .agg(
            total_revenue=("item_revenue", "sum"),
            quantity_sold=("quantity", "sum"),
            products=("product_id", "nunique")
        )
        .sort_values("total_revenue", ascending=False)
    )

    print(category_summary.round(2).to_string())

    # Brand performance
    print("\nTOP 10 BRANDS BY REVENUE")

    brand_summary = (
        product_sales.groupby("brand")
        .agg(total_revenue=("item_revenue", "sum"))
        .sort_values("total_revenue", ascending=False)
        .head(10)
    )

    print(brand_summary.round(2).to_string())

    # Product ratings
    print("\nPRODUCT RATINGS")

    print(f"Average Product Rating: {products['rating_average'].mean():.2f}")
    print(f"Products with Rating Below 3: {(products['rating_average'] < 3).sum()}")

    # Inventory
    print("\nINVENTORY OVERVIEW")

    print(f"Total Stock Quantity: {products['stock_quantity'].sum():,}")
    print(f"Out of Stock Products: {(products['stock_quantity'] == 0).sum():,}")

    print("\n" + "=" * 60)


def operations_analysis(datasets):
    payments = datasets["payments"].copy()
    shipments = datasets["shipments"].copy()
    returns = datasets["returns"].copy()

    print("\n" + "=" * 60)
    print("PAYMENT, SHIPMENT & RETURNS ANALYSIS")
    print("=" * 60)

    # PAYMENT ANALYSIS
    print("\nPAYMENT ANALYSIS")
    print(f"Total Transactions: {len(payments):,}")
    print(f"Total Amount Paid: {payments['amount_paid'].sum():,.2f}")
    print(f"Total Transaction Fees: {payments['transaction_fee'].sum():,.2f}")
    print(f"Total Refund Amount: {payments['refund_amount'].sum():,.2f}")

    print("\nPAYMENT STATUS DISTRIBUTION")
    payment_summary = (
        payments.groupby("payment_status")
        .agg(
            transactions=("payment_id", "count"),
            amount_paid=("amount_paid", "sum")
        )
        .sort_values("transactions", ascending=False)
    )
    payment_summary["percentage"] = (
        payment_summary["transactions"] / len(payments) * 100
    )
    print(payment_summary.round(2).to_string())

    print("\nPAYMENT METHOD DISTRIBUTION")
    print(payments["payment_method"].value_counts().to_string())

    # SHIPMENT ANALYSIS
    print("\n" + "-" * 60)
    print("SHIPMENT ANALYSIS")
    print("-" * 60)

    print(f"Total Shipments: {len(shipments):,}")
    print(f"Average Delivery Days: {shipments['delivery_days'].mean():.2f}")
    print(f"Delayed Shipments: {shipments['delayed_flag'].astype(str).str.lower().isin(['true', '1', 'yes']).sum():,}")

    print("\nDELIVERY STATUS DISTRIBUTION")
    print(shipments["delivery_status"].value_counts().to_string())

    print("\nSHIPPING METHOD DISTRIBUTION")
    print(shipments["shipping_method"].value_counts().to_string())

    print("\nDELIVERY PERFORMANCE BY SHIPPING METHOD")
    delivery_summary = (
        shipments.groupby("shipping_method")
        .agg(
            shipments=("shipment_id", "count"),
            average_delivery_days=("delivery_days", "mean")
        )
        .sort_values("average_delivery_days")
    )
    print(delivery_summary.round(2).to_string())

    # RETURNS ANALYSIS
    print("\n" + "-" * 60)
    print("RETURNS ANALYSIS")
    print("-" * 60)

    print(f"Total Returns: {len(returns):,}")
    print(f"Total Refund Amount: {returns['refund_amount'].sum():,.2f}")
    print(f"Average Refund Amount: {returns['refund_amount'].mean():,.2f}")

    print("\nRETURN REASON DISTRIBUTION")
    reason_summary = (
        returns["return_reason"]
        .value_counts()
        .to_frame("return_count")
    )
    reason_summary["percentage"] = (
        reason_summary["return_count"] / len(returns) * 100
    )
    print(reason_summary.round(2).to_string())

    print("\nRETURN STATUS DISTRIBUTION")
    print(returns["return_status"].value_counts().to_string())

    print("\n" + "=" * 60)


def reviews_marketing_analysis(datasets):
    reviews = datasets["customer_reviews"].copy()
    campaigns = datasets["marketing_campaigns"].copy()

    print("\n" + "=" * 60)
    print("CUSTOMER REVIEWS & MARKETING ANALYSIS")
    print("=" * 60)

    # CUSTOMER REVIEWS ANALYSIS
    print("\nCUSTOMER REVIEWS ANALYSIS")
    print("-" * 60)

    print(f"Total Reviews: {len(reviews):,}")
    print(f"Average Rating: {reviews['rating'].mean():.2f}")
    print(f"Verified Purchases: {reviews['verified_purchase'].astype(str).str.lower().isin(['true', '1', 'yes']).sum():,}")

    print("\nRATING DISTRIBUTION")
    rating_summary = reviews["rating"].value_counts().sort_index().to_frame("reviews")
    rating_summary["percentage"] = (
        rating_summary["reviews"] / len(reviews) * 100
    )
    print(rating_summary.round(2).to_string())

    print("\nREVIEW SENTIMENT DISTRIBUTION")
    print(reviews["review_sentiment"].value_counts().to_string())

    print("\nRATING BY SENTIMENT")
    sentiment_summary = (
        reviews.groupby("review_sentiment")
        .agg(
            total_reviews=("review_id", "count"),
            average_rating=("rating", "mean")
        )
        .sort_values("average_rating", ascending=False)
    )
    print(sentiment_summary.round(2).to_string())

    # MARKETING CAMPAIGN ANALYSIS
    print("\n" + "=" * 60)
    print("MARKETING CAMPAIGN ANALYSIS")
    print("-" * 60)

    print(f"Total Campaigns: {len(campaigns):,}")
    print(f"Total Campaign Cost: {campaigns['campaign_cost'].sum():,.2f}")
    print(f"Total Revenue Generated: {campaigns['revenue_generated'].sum():,.2f}")
    print(f"Total Conversions: {campaigns['conversions'].sum():,}")
    print(f"Total Impressions: {campaigns['impressions'].sum():,}")
    print(f"Total Clicks: {campaigns['clicks'].sum():,}")

    total_impressions = campaigns["impressions"].sum()
    total_clicks = campaigns["clicks"].sum()
    total_conversions = campaigns["conversions"].sum()

    ctr = (
        total_clicks / total_impressions * 100
        if total_impressions else 0
    )
    conversion_rate = (
        total_conversions / total_clicks * 100
        if total_clicks else 0
    )

    print(f"Overall Click-Through Rate: {ctr:.2f}%")
    print(f"Overall Conversion Rate: {conversion_rate:.2f}%")

    print("\nCAMPAIGN CHANNEL PERFORMANCE")
    channel_summary = (
        campaigns.groupby("channel")
        .agg(
            campaigns=("campaign_id", "count"),
            revenue=("revenue_generated", "sum"),
            cost=("campaign_cost", "sum"),
            conversions=("conversions", "sum"),
            clicks=("clicks", "sum")
        )
        .sort_values("revenue", ascending=False)
    )
    print(channel_summary.round(2).to_string())

    print("\nCAMPAIGN TYPE PERFORMANCE")
    type_summary = (
        campaigns.groupby("campaign_type")
        .agg(
            campaigns=("campaign_id", "count"),
            revenue=("revenue_generated", "sum"),
            cost=("campaign_cost", "sum"),
            conversions=("conversions", "sum")
        )
        .sort_values("revenue", ascending=False)
    )
    print(type_summary.round(2).to_string())

    print("\nTOP 10 CAMPAIGNS BY REVENUE")
    top_campaigns = (
        campaigns.groupby("campaign_name")
        .agg(
            revenue=("revenue_generated", "sum"),
            cost=("campaign_cost", "sum"),
            conversions=("conversions", "sum"),
            roi=("roi", "mean")
        )
        .sort_values("revenue", ascending=False)
        .head(10)
    )
    print(top_campaigns.round(2).to_string())

    print("\nCAMPAIGN ROI OVERVIEW")
    print(f"Average ROI: {campaigns['roi'].mean():.2f}")
    print(f"Median ROI: {campaigns['roi'].median():.2f}")
    print(f"Highest ROI: {campaigns['roi'].max():.2f}")
    print(f"Lowest ROI: {campaigns['roi'].min():.2f}")

    print("\n" + "=" * 60)



def create_visualizations(datasets):
    output_dir = PROJECT_ROOT / "reports" / "figures"
    output_dir.mkdir(parents=True, exist_ok=True)

    def save_chart(filename):
        plt.tight_layout()
        plt.savefig(output_dir / filename, dpi=300, bbox_inches="tight")
        plt.close()
        print(f"Saved: {filename}")

    # 1. MONTHLY SALES TREND
    orders = datasets["orders"].copy()
    orders["order_date"] = pd.to_datetime(orders["order_date"])

    monthly_sales = (
        orders.set_index("order_date")
        .resample("ME")
        .agg(
            total_revenue=("final_amount", "sum"),
            total_orders=("order_id", "count")
        )
    )

    plt.figure(figsize=(12, 6))
    plt.plot(monthly_sales.index, monthly_sales["total_revenue"], marker="o")
    plt.title("Monthly Sales Revenue Trend")
    plt.xlabel("Month")
    plt.ylabel("Revenue")
    plt.xticks(rotation=45)
    plt.grid(True)
    save_chart("monthly_sales_trend.png")

    # 2. ORDER STATUS DISTRIBUTION
    plt.figure(figsize=(9, 6))
    orders["order_status"].value_counts().plot(kind="bar")
    plt.title("Order Status Distribution")
    plt.xlabel("Order Status")
    plt.ylabel("Number of Orders")
    plt.xticks(rotation=30)
    save_chart("order_status_distribution.png")

    # 3. CUSTOMER SEGMENT REVENUE
    customers = datasets["customers"]

    segment_revenue = (
        customers.groupby("customer_segment")["total_spend"]
        .sum()
        .sort_values(ascending=False)
    )

    plt.figure(figsize=(9, 6))
    segment_revenue.plot(kind="bar")
    plt.title("Revenue by Customer Segment")
    plt.xlabel("Customer Segment")
    plt.ylabel("Total Customer Spend")
    plt.xticks(rotation=30)
    save_chart("customer_segment_revenue.png")

    # 4. PRODUCT CATEGORY REVENUE
    product_sales = datasets["order_items"].merge(
        datasets["products"][["product_id", "category"]],
        on="product_id",
        how="left"
    )

    category_revenue = (
        product_sales.groupby("category")["item_revenue"]
        .sum()
        .sort_values()
    )

    plt.figure(figsize=(11, 8))
    category_revenue.plot(kind="barh")
    plt.title("Revenue by Product Category")
    plt.xlabel("Revenue")
    plt.ylabel("Category")
    save_chart("category_revenue.png")

    # 5. PAYMENT STATUS DISTRIBUTION
    payments = datasets["payments"]

    plt.figure(figsize=(9, 6))
    payments["payment_status"].value_counts().plot(kind="bar")
    plt.title("Payment Status Distribution")
    plt.xlabel("Payment Status")
    plt.ylabel("Number of Transactions")
    plt.xticks(rotation=30)
    save_chart("payment_status_distribution.png")

    # 6. DELIVERY TIME BY SHIPPING METHOD
    shipments = datasets["shipments"]

    shipping_days = (
        shipments.groupby("shipping_method")["delivery_days"]
        .mean()
        .sort_values()
    )

    plt.figure(figsize=(10, 6))
    shipping_days.plot(kind="bar")
    plt.title("Average Delivery Days by Shipping Method")
    plt.xlabel("Shipping Method")
    plt.ylabel("Average Delivery Days")
    plt.xticks(rotation=30)
    save_chart("shipping_method_performance.png")

    # 7. RETURN REASONS
    returns = datasets["returns"]

    return_reasons = returns["return_reason"].value_counts().sort_values()

    plt.figure(figsize=(10, 6))
    return_reasons.plot(kind="barh")
    plt.title("Customer Return Reasons")
    plt.xlabel("Number of Returns")
    plt.ylabel("Return Reason")
    save_chart("return_reason_distribution.png")

    # 8. CUSTOMER REVIEW RATINGS
    reviews = datasets["customer_reviews"]

    plt.figure(figsize=(9, 6))
    reviews["rating"].value_counts().sort_index().plot(kind="bar")
    plt.title("Customer Review Rating Distribution")
    plt.xlabel("Rating")
    plt.ylabel("Number of Reviews")
    save_chart("customer_review_ratings.png")

    # 9. MARKETING CHANNEL REVENUE
    campaigns = datasets["marketing_campaigns"]

    channel_revenue = (
        campaigns.groupby("channel")["revenue_generated"]
        .sum()
        .sort_values()
    )

    plt.figure(figsize=(10, 7))
    channel_revenue.plot(kind="barh")
    plt.title("Revenue by Marketing Channel")
    plt.xlabel("Revenue Generated")
    plt.ylabel("Marketing Channel")
    save_chart("marketing_channel_revenue.png")

    # 10. MARKETING CAMPAIGN TYPE REVENUE
    type_revenue = (
        campaigns.groupby("campaign_type")["revenue_generated"]
        .sum()
        .sort_values()
    )

    plt.figure(figsize=(10, 7))
    type_revenue.plot(kind="barh")
    plt.title("Revenue by Marketing Campaign Type")
    plt.xlabel("Revenue Generated")
    plt.ylabel("Campaign Type")
    save_chart("campaign_type_revenue.png")

    print("\n" + "=" * 60)
    print("VISUALISATIONS COMPLETED")
    print(f"Charts saved in: {output_dir}")
    print("=" * 60)


if __name__ == "__main__":
    datasets = load_datasets()

    dataset_overview(datasets)
    sales_analysis(datasets)
    customer_analysis(datasets)
    product_analysis(datasets)
    operations_analysis(datasets)
    reviews_marketing_analysis(datasets)
    create_visualizations(datasets)


