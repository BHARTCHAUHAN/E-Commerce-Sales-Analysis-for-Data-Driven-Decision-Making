"""
Demo Script for E-Commerce Sales Dashboard
Run this to see example insights from the dashboard
"""

import pandas as pd
from dashboard import load_data, calculate_rfm

def main():
    print("=" * 70)
    print("E-COMMERCE SALES ANALYSIS DASHBOARD - DEMO")
    print("=" * 70)
    print()
    
    # Load data
    print("📊 Loading sample e-commerce data...")
    df = load_data()
    print(f"✓ Loaded {len(df):,} transactions")
    print()
    
    # Basic statistics
    print("=" * 70)
    print("KEY METRICS")
    print("=" * 70)
    print(f"Total Orders:        {df['Order_ID'].nunique():,}")
    print(f"Net Sales:           ${df['Net_Sales'].sum():,.2f}")
    print(f"Total Profit:        ${df['Profit'].sum():,.2f}")
    print(f"Profit Margin:       {(df['Profit'].sum() / df['Net_Sales'].sum() * 100):.2f}%")
    print(f"Units Sold:          {df['Units_Sold'].sum():,}")
    print(f"Unique Customers:    {df['Customer_ID'].nunique():,}")
    print(f"Date Range:          {df['Order_Date'].min().date()} to {df['Order_Date'].max().date()}")
    print()
    
    # Category performance
    print("=" * 70)
    print("TOP PRODUCT CATEGORIES")
    print("=" * 70)
    category_sales = df.groupby('Category').agg({
        'Net_Sales': 'sum',
        'Profit': 'sum',
        'Order_ID': 'count'
    }).round(2)
    category_sales.columns = ['Net Sales', 'Profit', 'Orders']
    category_sales = category_sales.sort_values('Net Sales', ascending=False)
    print(category_sales.to_string())
    print()
    
    # Payment methods
    print("=" * 70)
    print("PAYMENT METHODS DISTRIBUTION")
    print("=" * 70)
    payment_dist = df.groupby('Payment_Method')['Net_Sales'].sum().sort_values(ascending=False)
    for method, sales in payment_dist.items():
        pct = (sales / payment_dist.sum() * 100)
        print(f"{method:20s} ${sales:>12,.2f}  ({pct:>5.2f}%)")
    print()
    
    # Top cities
    print("=" * 70)
    print("TOP 5 CITIES BY SALES")
    print("=" * 70)
    city_sales = df.groupby('City')['Net_Sales'].sum().sort_values(ascending=False).head(5)
    for city, sales in city_sales.items():
        print(f"{city:20s} ${sales:>12,.2f}")
    print()
    
    # RFM Analysis
    print("=" * 70)
    print("RFM CUSTOMER SEGMENTATION ANALYSIS")
    print("=" * 70)
    rfm_df = calculate_rfm(df)
    
    print("\nCustomer Segment Distribution:")
    print("-" * 70)
    segment_counts = rfm_df['Customer_Segment'].value_counts()
    for segment, count in segment_counts.items():
        pct = (count / len(rfm_df) * 100)
        print(f"{segment:25s} {count:>4} customers  ({pct:>5.2f}%)")
    
    print("\nSegment Characteristics:")
    print("-" * 70)
    segment_stats = rfm_df.groupby('Customer_Segment').agg({
        'Recency': 'mean',
        'Frequency': 'mean',
        'Monetary': 'mean'
    }).round(2)
    segment_stats.columns = ['Avg Recency (days)', 'Avg Frequency', 'Avg Monetary ($)']
    print(segment_stats.to_string())
    print()
    
    # Customer segment insights
    print("=" * 70)
    print("CUSTOMER SEGMENT INSIGHTS")
    print("=" * 70)
    
    # Calculate total revenue by segment
    df_with_rfm = df.merge(rfm_df[['Customer_Segment', 'Monetary']], 
                            left_on='Customer_ID', right_index=True, how='left')
    segment_revenue = df_with_rfm.groupby('Customer_Segment')['Net_Sales'].sum().sort_values(ascending=False)
    
    print("\nRevenue Contribution by Segment:")
    print("-" * 70)
    for segment, revenue in segment_revenue.items():
        pct = (revenue / segment_revenue.sum() * 100)
        print(f"{segment:25s} ${revenue:>12,.2f}  ({pct:>5.2f}%)")
    print()
    
    # Top products
    print("=" * 70)
    print("TOP 10 PRODUCTS BY REVENUE")
    print("=" * 70)
    top_products = df.groupby('Product').agg({
        'Net_Sales': 'sum',
        'Units_Sold': 'sum'
    }).sort_values('Net_Sales', ascending=False).head(10)
    top_products.columns = ['Net Sales', 'Units Sold']
    print(top_products.to_string())
    print()
    
    # Recommendations
    print("=" * 70)
    print("💡 BUSINESS RECOMMENDATIONS")
    print("=" * 70)
    print()
    print("1. CHAMPION CUSTOMERS (Highest Value):")
    champions = rfm_df[rfm_df['Customer_Segment'] == 'Champions']
    print(f"   - {len(champions)} customers generating significant revenue")
    print(f"   - Average spend: ${champions['Monetary'].mean():,.2f}")
    print(f"   - Strategy: VIP programs, exclusive offers, early access to new products")
    print()
    
    print("2. AT RISK CUSTOMERS (Require Attention):")
    at_risk = rfm_df[rfm_df['Customer_Segment'] == 'At Risk']
    print(f"   - {len(at_risk)} customers who haven't purchased recently")
    print(f"   - Average days since last purchase: {at_risk['Recency'].mean():.0f}")
    print(f"   - Strategy: Win-back campaigns, special discounts, personalized outreach")
    print()
    
    print("3. TOP PERFORMING CATEGORY:")
    top_category = category_sales.index[0]
    top_cat_sales = category_sales.loc[top_category, 'Net Sales']
    print(f"   - {top_category}: ${top_cat_sales:,.2f}")
    print(f"   - Strategy: Expand product range, increase inventory, targeted marketing")
    print()
    
    print("4. CUSTOMER ENGAGEMENT:")
    lost_customers = rfm_df[rfm_df['Customer_Segment'] == 'Lost Customers']
    print(f"   - {len(lost_customers)} lost customers need re-engagement")
    print(f"   - Strategy: Survey to understand why they left, special comeback offers")
    print()
    
    print("=" * 70)
    print("🚀 LAUNCH THE DASHBOARD")
    print("=" * 70)
    print()
    print("Run the following command to launch the interactive dashboard:")
    print()
    print("    streamlit run dashboard.py")
    print()
    print("Then open your browser to http://localhost:8501")
    print()
    print("=" * 70)

if __name__ == "__main__":
    main()
