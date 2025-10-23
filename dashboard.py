"""
E-Commerce Sales Analysis Dashboard with RFM Customer Segmentation
Interactive dashboard for data-driven decision making
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import numpy as np

# Page configuration
st.set_page_config(
    page_title="E-Commerce Sales Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        padding: 0rem 1rem;
    }
    .stMetric {
        background-color: #f0f2f6;
        padding: 15px;
        border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv('ecommerce_sales_data.csv')
    df['Order_Date'] = pd.to_datetime(df['Order_Date'])
    return df

# Calculate RFM scores
@st.cache_data
def calculate_rfm(df):
    """
    Calculate RFM (Recency, Frequency, Monetary) scores for customer segmentation
    """
    # Use the most recent date in the dataset as reference
    reference_date = df['Order_Date'].max() + pd.Timedelta(days=1)
    
    # Calculate RFM metrics
    rfm = df.groupby('Customer_ID').agg({
        'Order_Date': lambda x: (reference_date - x.max()).days,  # Recency
        'Order_ID': 'count',  # Frequency
        'Net_Sales': 'sum'  # Monetary
    })
    
    rfm.columns = ['Recency', 'Frequency', 'Monetary']
    
    # Calculate RFM scores (1-5 scale, 5 being the best)
    rfm['R_Score'] = pd.qcut(rfm['Recency'], 5, labels=[5, 4, 3, 2, 1], duplicates='drop')
    rfm['F_Score'] = pd.qcut(rfm['Frequency'].rank(method='first'), 5, labels=[1, 2, 3, 4, 5], duplicates='drop')
    rfm['M_Score'] = pd.qcut(rfm['Monetary'], 5, labels=[1, 2, 3, 4, 5], duplicates='drop')
    
    # Convert to int for calculations
    rfm['R_Score'] = rfm['R_Score'].astype(int)
    rfm['F_Score'] = rfm['F_Score'].astype(int)
    rfm['M_Score'] = rfm['M_Score'].astype(int)
    
    # Calculate RFM Score
    rfm['RFM_Score'] = rfm['R_Score'] + rfm['F_Score'] + rfm['M_Score']
    
    # Customer Segmentation based on RFM Score
    def assign_segment(score):
        if score >= 13:
            return 'Champions'
        elif score >= 10:
            return 'Loyal Customers'
        elif score >= 7:
            return 'Potential Loyalists'
        elif score >= 5:
            return 'At Risk'
        else:
            return 'Lost Customers'
    
    rfm['Customer_Segment'] = rfm['RFM_Score'].apply(assign_segment)
    
    return rfm

# Main app
def main():
    st.title("📊 E-Commerce Sales Analysis Dashboard")
    st.markdown("### Data-Driven Decision Making with RFM Customer Segmentation")
    
    # Load data
    df = load_data()
    rfm_df = calculate_rfm(df)
    
    # Merge RFM data with main dataframe
    df_with_rfm = df.merge(rfm_df[['Customer_Segment']], left_on='Customer_ID', right_index=True, how='left')
    
    # Sidebar filters
    st.sidebar.header("📌 Filters")
    
    # Year filter
    years = sorted(df['Year'].unique())
    selected_years = st.sidebar.multiselect(
        "Select Year(s)",
        options=years,
        default=years
    )
    
    # Month filter
    months = ['January', 'February', 'March', 'April', 'May', 'June', 
              'July', 'August', 'September', 'October', 'November', 'December']
    selected_months = st.sidebar.multiselect(
        "Select Month(s)",
        options=months,
        default=months
    )
    
    # Category filter
    categories = sorted(df['Category'].unique())
    selected_categories = st.sidebar.multiselect(
        "Select Category(ies)",
        options=categories,
        default=categories
    )
    
    # City filter
    cities = sorted(df['City'].unique())
    selected_cities = st.sidebar.multiselect(
        "Select City(ies)",
        options=cities,
        default=cities
    )
    
    # Apply filters
    filtered_df = df_with_rfm[
        (df_with_rfm['Year'].isin(selected_years)) &
        (df_with_rfm['Month'].isin(selected_months)) &
        (df_with_rfm['Category'].isin(selected_categories)) &
        (df_with_rfm['City'].isin(selected_cities))
    ]
    
    # Key Metrics
    st.markdown("### 📈 Key Performance Indicators")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        total_orders = filtered_df['Order_ID'].nunique()
        st.metric("Total Orders", f"{total_orders:,}")
    
    with col2:
        total_net_sales = filtered_df['Net_Sales'].sum()
        st.metric("Net Sales", f"${total_net_sales:,.2f}")
    
    with col3:
        total_profit = filtered_df['Profit'].sum()
        profit_margin = (total_profit / total_net_sales * 100) if total_net_sales > 0 else 0
        st.metric("Total Profit", f"${total_profit:,.2f}", f"{profit_margin:.1f}% margin")
    
    with col4:
        total_units = filtered_df['Units_Sold'].sum()
        st.metric("Units Sold", f"{total_units:,}")
    
    st.markdown("---")
    
    # Row 1: Sales trends and Payment methods
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 📅 Sales Trend Over Time")
        
        # Aggregate by month
        monthly_sales = filtered_df.groupby([filtered_df['Order_Date'].dt.to_period('M')])['Net_Sales'].sum().reset_index()
        monthly_sales['Order_Date'] = monthly_sales['Order_Date'].astype(str)
        
        fig = px.line(monthly_sales, x='Order_Date', y='Net_Sales',
                      title='Monthly Sales Trend',
                      labels={'Order_Date': 'Month', 'Net_Sales': 'Net Sales ($)'})
        fig.update_traces(line_color='#1f77b4', line_width=3)
        fig.update_layout(height=400)
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown("### 💳 Payment Methods Distribution")
        
        payment_dist = filtered_df.groupby('Payment_Method')['Net_Sales'].sum().reset_index()
        
        fig = px.pie(payment_dist, values='Net_Sales', names='Payment_Method',
                     title='Sales by Payment Method')
        fig.update_layout(height=400)
        st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("---")
    
    # Row 2: Category performance and Brand analysis
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🏷️ Sales by Category")
        
        category_sales = filtered_df.groupby('Category').agg({
            'Net_Sales': 'sum',
            'Profit': 'sum',
            'Units_Sold': 'sum'
        }).reset_index().sort_values('Net_Sales', ascending=False)
        
        fig = px.bar(category_sales, x='Category', y='Net_Sales',
                     title='Net Sales by Category',
                     labels={'Net_Sales': 'Net Sales ($)', 'Category': 'Product Category'},
                     color='Net_Sales',
                     color_continuous_scale='Blues')
        fig.update_layout(height=400, showlegend=False)
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown("### 🏭 Top Brands by Revenue")
        
        brand_sales = filtered_df.groupby('Brand')['Net_Sales'].sum().reset_index()
        brand_sales = brand_sales.sort_values('Net_Sales', ascending=True).tail(10)
        
        fig = px.bar(brand_sales, x='Net_Sales', y='Brand',
                     title='Top 10 Brands',
                     labels={'Net_Sales': 'Net Sales ($)', 'Brand': 'Brand'},
                     orientation='h',
                     color='Net_Sales',
                     color_continuous_scale='Greens')
        fig.update_layout(height=400, showlegend=False)
        st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("---")
    
    # Row 3: Seller and Product performance
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🏪 Seller Performance")
        
        seller_perf = filtered_df.groupby('Seller').agg({
            'Net_Sales': 'sum',
            'Profit': 'sum',
            'Order_ID': 'count'
        }).reset_index()
        seller_perf.columns = ['Seller', 'Net_Sales', 'Profit', 'Orders']
        seller_perf = seller_perf.sort_values('Net_Sales', ascending=False)
        
        fig = px.scatter(seller_perf, x='Net_Sales', y='Profit', 
                        size='Orders', color='Seller',
                        title='Seller Performance: Sales vs Profit',
                        labels={'Net_Sales': 'Net Sales ($)', 'Profit': 'Profit ($)'},
                        hover_data=['Orders'])
        fig.update_layout(height=400)
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown("### 🌆 Sales by City")
        
        city_sales = filtered_df.groupby('City')['Net_Sales'].sum().reset_index()
        city_sales = city_sales.sort_values('Net_Sales', ascending=False).head(10)
        
        fig = px.bar(city_sales, x='City', y='Net_Sales',
                     title='Top 10 Cities by Sales',
                     labels={'Net_Sales': 'Net Sales ($)', 'City': 'City'},
                     color='Net_Sales',
                     color_continuous_scale='Oranges')
        fig.update_layout(height=400, showlegend=False, xaxis_tickangle=-45)
        st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("---")
    
    # RFM Analysis Section
    st.markdown("### 👥 RFM Customer Segmentation Analysis")
    
    # Filter RFM data based on customers in filtered dataset
    filtered_customers = filtered_df['Customer_ID'].unique()
    filtered_rfm = rfm_df[rfm_df.index.isin(filtered_customers)]
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("#### Customer Segment Distribution")
        segment_dist = filtered_rfm['Customer_Segment'].value_counts().reset_index()
        segment_dist.columns = ['Segment', 'Count']
        
        # Define colors for segments
        colors = {
            'Champions': '#2ecc71',
            'Loyal Customers': '#3498db',
            'Potential Loyalists': '#f39c12',
            'At Risk': '#e74c3c',
            'Lost Customers': '#95a5a6'
        }
        segment_dist['Color'] = segment_dist['Segment'].map(colors)
        
        fig = px.bar(segment_dist, x='Segment', y='Count',
                     title='Number of Customers by Segment',
                     color='Segment',
                     color_discrete_map=colors)
        fig.update_layout(height=350, showlegend=False, xaxis_tickangle=-45)
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown("#### Average Monetary Value by Segment")
        segment_monetary = filtered_rfm.groupby('Customer_Segment')['Monetary'].mean().reset_index()
        segment_monetary = segment_monetary.sort_values('Monetary', ascending=False)
        
        fig = px.bar(segment_monetary, x='Customer_Segment', y='Monetary',
                     title='Avg Spend per Customer Segment',
                     labels={'Monetary': 'Average Spend ($)', 'Customer_Segment': 'Segment'},
                     color='Customer_Segment',
                     color_discrete_map=colors)
        fig.update_layout(height=350, showlegend=False, xaxis_tickangle=-45)
        st.plotly_chart(fig, use_container_width=True)
    
    with col3:
        st.markdown("#### Recency by Customer Segment")
        segment_recency = filtered_rfm.groupby('Customer_Segment')['Recency'].mean().reset_index()
        segment_recency = segment_recency.sort_values('Recency')
        
        fig = px.bar(segment_recency, x='Customer_Segment', y='Recency',
                     title='Avg Days Since Last Purchase',
                     labels={'Recency': 'Days Since Last Order', 'Customer_Segment': 'Segment'},
                     color='Customer_Segment',
                     color_discrete_map=colors)
        fig.update_layout(height=350, showlegend=False, xaxis_tickangle=-45)
        st.plotly_chart(fig, use_container_width=True)
    
    # RFM Scatter plot
    st.markdown("#### 📊 RFM Score Distribution")
    col1, col2 = st.columns([2, 1])
    
    with col1:
        fig = px.scatter(filtered_rfm, x='Frequency', y='Monetary', 
                        color='Customer_Segment', size='Recency',
                        title='Customer Segmentation: Frequency vs Monetary Value',
                        labels={'Frequency': 'Purchase Frequency', 'Monetary': 'Total Spend ($)'},
                        color_discrete_map=colors,
                        hover_data=['Recency', 'RFM_Score'])
        fig.update_layout(height=400)
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown("#### 📋 Segment Statistics")
        segment_stats = filtered_rfm.groupby('Customer_Segment').agg({
            'Recency': 'mean',
            'Frequency': 'mean',
            'Monetary': 'mean'
        }).round(2)
        segment_stats.columns = ['Avg Recency', 'Avg Frequency', 'Avg Monetary']
        st.dataframe(segment_stats, use_container_width=True)
    
    st.markdown("---")
    
    # Top Products Section
    st.markdown("### 🏆 Top Performing Products")
    
    top_products = filtered_df.groupby('Product').agg({
        'Net_Sales': 'sum',
        'Profit': 'sum',
        'Units_Sold': 'sum',
        'Order_ID': 'count'
    }).reset_index()
    top_products.columns = ['Product', 'Net Sales', 'Profit', 'Units Sold', 'Orders']
    top_products = top_products.sort_values('Net Sales', ascending=False).head(15)
    
    st.dataframe(
        top_products.style.format({
            'Net Sales': '${:,.2f}',
            'Profit': '${:,.2f}',
            'Units Sold': '{:,.0f}',
            'Orders': '{:,.0f}'
        }),
        use_container_width=True
    )
    
    # Footer
    st.markdown("---")
    st.markdown("""
        <div style='text-align: center; color: #888;'>
            <p>E-Commerce Sales Analysis Dashboard | Built with Streamlit & Plotly</p>
            <p>Data-Driven Decision Making with RFM Customer Segmentation</p>
        </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
