
from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT / "data" / "processed"
REPORT_DIR = PROJECT_ROOT / "reports"
FIGURE_DIR = REPORT_DIR / "figures"

def load_data():
    return {
        file.stem: pd.read_csv(file)
        for file in DATA_DIR.glob("*.csv")
    }


def generate_report(datasets):
    customers = datasets["customers"]
    orders = datasets["orders"]
    products = datasets["products"]
    items = datasets["order_items"]
    payments = datasets["payments"]
    shipments = datasets["shipments"]
    returns = datasets["returns"]
    reviews = datasets["customer_reviews"]
    campaigns = datasets["marketing_campaigns"]

    total_records = sum(len(df) for df in datasets.values())
    delivered = orders[orders["order_status"] == "Delivered"]

    category_sales = (
        items.merge(products, on="product_id", how="left")
        .groupby("category")["item_revenue"]
        .sum()
        .sort_values(ascending=False)
    )

    brand_sales = (
        items.merge(products, on="product_id", how="left")
    )
    brand_sales["brand"] = (
        brand_sales["brand"].astype("string").str.strip().str.rstrip(",").str.strip()
    )
    top_brands = (
        brand_sales.groupby("brand")["item_revenue"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    top_channel = (
        campaigns.groupby("channel")["revenue_generated"]
        .sum().sort_values(ascending=False)
    )

    top_campaign_type = (
        campaigns.groupby("campaign_type")["revenue_generated"]
        .sum().sort_values(ascending=False)
    )

    report = []

    def add(text=""):
        report.append(str(text))

    add("# India Commerce Intelligence")
    add("## Exploratory Data Analysis Report")
    add()
    add("**Project:** India Commerce Intelligence")
    add("**Analysis period:** 2023–2025")
    add("**Datasets analysed:** 9")
    add()
    add("---")
    add()
    add("## 1. Project Overview")
    add()
    add(
        "This project analyses e-commerce data to understand sales performance, "
        "customer behaviour, product performance, payment trends, delivery "
        "operations, returns, customer satisfaction and marketing effectiveness."
    )
    add()
    add("## 2. Dataset Overview")
    add()
    add(f"- Total datasets: {len(datasets)}")
    add(f"- Total records: {total_records:,}")
    add()
    add("| Dataset | Records | Columns | Missing Values |")
    add("|---|---:|---:|---:|")

    for name, df in datasets.items():
        add(
            f"| {name.replace('_', ' ').title()} "
            f"| {len(df):,} | {len(df.columns)} "
            f"| {df.isna().sum().sum():,} |"
        )

    add()
    add("## 3. Sales Performance Analysis")
    add()
    add(f"- Total orders: {len(orders):,}")
    add(f"- Total order value: {orders['final_amount'].sum():,.2f}")
    add(f"- Average order value: {orders['final_amount'].mean():,.2f}")
    add(f"- Delivered orders: {len(delivered):,}")
    add(f"- Delivered order value: {delivered['final_amount'].sum():,.2f}")
    add()
    add("### Order Status Distribution")
    add()
    add(orders["order_status"].value_counts().to_frame("Orders").to_markdown())
    add()
    add("### Monthly Sales Trend")
    add()
    add(
        "December 2025 recorded the highest monthly order value "
        "in the analysed period."
    )
    add()
    add("![Monthly Sales Trend](figures/monthly_sales_trend.png)")
    add()
    add("![Order Status Distribution](figures/order_status_distribution.png)")
    add()
    add("## 4. Customer Analysis")
    add()
    add(f"- Total customers: {len(customers):,}")
    add(f"- Average customer spend: {customers['total_spend'].mean():,.2f}")
    add(f"- Average orders per customer: {customers['total_orders'].mean():.2f}")
    add(
        f"- Churned customers: "
        f"{(customers['customer_status'] == 'Churned').sum():,}"
    )
    add()
    add("### Customer Segment Distribution")
    add()
    segment = customers.groupby("customer_segment").agg(
        customers=("customer_id", "count"),
        average_spend=("total_spend", "mean"),
        total_spend=("total_spend", "sum")
    )
    add(segment.round(2).to_markdown())
    add()
    add("![Customer Segment Revenue](figures/customer_segment_revenue.png)")
    add()
    add("## 5. Product Performance Analysis")
    add()
    add(f"- Total products: {len(products):,}")
    add(f"- Product categories: {products['category'].nunique()}")
    add(f"- Unique brands: {products['brand'].nunique()}")
    add(f"- Average product rating: {products['rating_average'].mean():.2f}")
    add()
    add("### Category Revenue")
    add()
    add(category_sales.round(2).to_frame("Revenue").to_markdown())
    add()
    add("### Top 10 Brands by Revenue")
    add()
    add(top_brands.round(2).to_frame("Revenue").to_markdown())
    add()
    add("![Category Revenue](figures/category_revenue.png)")
    add()
    add("## 6. Payment, Shipment and Returns Analysis")
    add()
    add("### Payments")
    add()
    add(f"- Total transactions: {len(payments):,}")
    add(f"- Total amount paid: {payments['amount_paid'].sum():,.2f}")
    add(f"- Transaction fees: {payments['transaction_fee'].sum():,.2f}")
    add(f"- Refund amount: {payments['refund_amount'].sum():,.2f}")
    add()
    add(payments["payment_status"].value_counts().to_frame("Transactions").to_markdown())
    add()
    add("![Payment Status](figures/payment_status_distribution.png)")
    add()
    add("### Shipments")
    add()
    add(f"- Total shipments: {len(shipments):,}")
    add(f"- Average delivery days: {shipments['delivery_days'].mean():.2f}")
    add()
    add(
        shipments.groupby("shipping_method")["delivery_days"]
        .mean().round(2).to_frame("Average Delivery Days").to_markdown()
    )
    add()
    add("![Shipping Performance](figures/shipping_method_performance.png)")
    add()
    add("### Returns")
    add()
    add(f"- Total returns: {len(returns):,}")
    add(f"- Total return refunds: {returns['refund_amount'].sum():,.2f}")
    add()
    add(returns["return_reason"].value_counts().to_frame("Returns").to_markdown())
    add()
    add("![Return Reasons](figures/return_reason_distribution.png)")
    add()
    add("## 7. Customer Reviews Analysis")
    add()
    add(f"- Total reviews: {len(reviews):,}")
    add(f"- Average rating: {reviews['rating'].mean():.2f} / 5")
    add()
    add(reviews["review_sentiment"].value_counts().to_frame("Reviews").to_markdown())
    add()
    add("![Customer Review Ratings](figures/customer_review_ratings.png)")
    add()
    add("## 8. Marketing Campaign Analysis")
    add()
    add(f"- Total campaigns: {len(campaigns):,}")
    add(f"- Campaign cost: {campaigns['campaign_cost'].sum():,.2f}")
    add(f"- Revenue generated: {campaigns['revenue_generated'].sum():,.2f}")
    add(f"- Total conversions: {campaigns['conversions'].sum():,}")
    add(f"- Total impressions: {campaigns['impressions'].sum():,}")
    add(f"- Total clicks: {campaigns['clicks'].sum():,}")
    add()
    add(
        f"- Overall CTR: "
        f"{campaigns['clicks'].sum() / campaigns['impressions'].sum() * 100:.2f}%"
    )
    add()
    add("### Marketing Channel Revenue")
    add()
    add(top_channel.round(2).to_frame("Revenue").to_markdown())
    add()
    add("![Marketing Channel Revenue](figures/marketing_channel_revenue.png)")
    add()
    add("### Campaign Type Revenue")
    add()
    add(top_campaign_type.round(2).to_frame("Revenue").to_markdown())
    add()
    add("![Campaign Type Revenue](figures/campaign_type_revenue.png)")
    add()
    add("## 9. Key Business Insights")
    add()
    add("1. December 2025 recorded the highest monthly order value.")
    add("2. Regular customers form the largest customer segment.")
    add("3. Electronics generates the highest category revenue.")
    add("4. Successful payments account for 82.14% of transactions.")
    add("5. Same-Day shipping has the shortest average delivery time.")
    add("6. Size issues are the most frequent return reason.")
    add("7. The average customer review rating is 3.69 out of 5.")
    add("8. Organic Search generates the highest marketing channel revenue.")
    add("9. Loyalty Programs generate the highest revenue among campaign types.")
    add()
    add("## 10. Recommendations")
    add()
    add("- Investigate customer churn and develop retention strategies.")
    add("- Review the performance and inventory of high-revenue products.")
    add("- Investigate the leading reasons for product returns.")
    add("- Monitor delivery delays across shipping methods.")
    add("- Improve customer experience to increase review ratings.")
    add("- Evaluate marketing campaigns using both revenue and campaign cost.")
    add()
    add("## 11. Conclusion")
    add()
    add(
        "The exploratory analysis provides an overview of e-commerce sales, "
        "customers, products, payments, logistics, returns, customer feedback "
        "and marketing performance. These findings establish a foundation "
        "for further business intelligence and dashboard development."
    )
    add()
    add("---")
    add("*Generated automatically using Python and Pandas.*")

    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    output_file = REPORT_DIR / "eda_report.md"
    output_file.write_text("\n".join(report), encoding="utf-8")

    print("\nEDA REPORT GENERATED SUCCESSFULLY")
    print(f"Report saved at: {output_file}")


if __name__ == "__main__":
    datasets = load_data()
    generate_report(datasets)
