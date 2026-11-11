# Database Schema — India Commerce Intelligence

## Database
- Name: india_commerce_dw
- Engine: PostgreSQL 16
- Total tables: 9

## Tables

### 1. customers
Customer master data, signup information, customer segments and customer status.

### 2. orders
Order transactions, customer references, dates, order status, delivery location, discounts and final order amounts.

### 3. products
Product catalogue containing product names, categories, brands, prices, costs, ratings and stock quantities.

### 4. order_items
Order line items containing product references, quantities, unit prices, discounts, item revenue, item cost and profit.

### 5. payments
Payment transaction details, payment methods, payment status and refund information.

### 6. shipments
Shipment records containing dispatch dates, expected and actual delivery dates, delivery duration and delayed flags.

### 7. returns
Return records containing order, customer and product references, return dates, reasons and refund amounts.

### 8. customer_reviews
Customer feedback and ratings associated with orders and products.

### 9. marketing_campaigns
Campaign information containing channels, campaign types, impressions, clicks, conversions, spending and generated revenue.

## Main Relationships

- customers.customer_id → orders.customer_id
- orders.order_id → order_items.order_id
- products.product_id → order_items.product_id
- orders.order_id → payments.order_id
- orders.order_id → shipments.order_id
- orders.order_id → returns.order_id
- customers.customer_id → returns.customer_id
- products.product_id → returns.product_id

Additional relationships should be verified against the actual table schemas before implementing database constraints.

## Important Measures
- Order revenue: orders.final_amount
- Item revenue: order_items.item_revenue
- Item cost: order_items.item_cost
- Item profit: order_items.profit
- Campaign revenue: marketing_campaigns.revenue_generated
- Campaign spending: marketing_campaigns.campaign_cost
