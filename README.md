# E-Commerce Sales Analysis for Data-Driven Decision Making

This project provides an **interactive dashboard** for E-Commerce Sales Analysis using **RFM Customer Segmentation**. The dashboard enables data-driven decision making by visualizing key metrics such as customer distribution by segment, average spend, total sales, and average recency across different customer groups.

## 📊 Features

- **Key Performance Indicators (KPIs)**: Track total orders, net sales, profit, and units sold
- **Interactive Filters**: Filter data by product category, year, month, and city
- **Sales Analytics**:
  - Sales trends over time
  - Sales by category and brand
  - Payment method distribution
  - Seller and product performance analysis
  - Geographic sales distribution by city
- **RFM Customer Segmentation**:
  - **Recency**: Days since last purchase
  - **Frequency**: Number of purchases
  - **Monetary**: Total spending
  - Customer segments: Champions, Loyal Customers, Potential Loyalists, At Risk, Lost Customers
  - Segment-wise metrics and visualizations

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Installation

1. Clone the repository:
```bash
git clone https://github.com/BHARTCHAUHAN/E-Commerce-Sales-Analysis-for-Data-Driven-Decision-Making.git
cd E-Commerce-Sales-Analysis-for-Data-Driven-Decision-Making
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

### Running the Dashboard

1. Generate sample data (already included in the repository):
```bash
python generate_sample_data.py
```

2. Launch the Streamlit dashboard:
```bash
streamlit run dashboard.py
```

3. Open your web browser and navigate to:
```
http://localhost:8501
```

## 📁 Project Structure

```
├── dashboard.py                 # Main Streamlit dashboard application
├── generate_sample_data.py      # Script to generate sample e-commerce data
├── ecommerce_sales_data.csv     # Sample dataset (5000 transactions)
├── requirements.txt             # Python dependencies
└── README.md                    # Project documentation
```

## 📈 Dashboard Sections

### 1. Key Performance Indicators
- Total Orders
- Net Sales (Revenue)
- Total Profit with margin percentage
- Units Sold

### 2. Sales Analytics
- **Monthly Sales Trend**: Line chart showing sales over time
- **Payment Methods**: Pie chart of sales distribution by payment method
- **Category Performance**: Bar chart of sales by product category
- **Brand Analysis**: Top 10 brands by revenue
- **Seller Performance**: Scatter plot of sales vs profit with order volume
- **Geographic Analysis**: Top cities by sales

### 3. RFM Customer Segmentation
- **Customer Segments**:
  - **Champions** (RFM Score ≥ 13): Best customers who buy frequently and recently
  - **Loyal Customers** (RFM Score 10-12): Regular customers with good spending
  - **Potential Loyalists** (RFM Score 7-9): Recent customers with potential
  - **At Risk** (RFM Score 5-6): Customers who haven't purchased recently
  - **Lost Customers** (RFM Score < 5): Inactive customers who need re-engagement

- **Visualizations**:
  - Customer distribution by segment
  - Average monetary value by segment
  - Recency analysis by segment
  - Frequency vs Monetary scatter plot
  - Segment statistics table

### 4. Product Performance
- Top 15 products by sales, profit, and units sold

## 📊 Sample Data

The sample dataset includes:
- **5,000 transactions** from January 2022 to December 2024
- **500 unique customers**
- **7 product categories**: Electronics, Fashion, Home & Kitchen, Sports, Books, Beauty, Toys
- **8 brands** and **8 sellers**
- **10 cities** across the United States
- **5 payment methods**: Credit Card, Debit Card, PayPal, Cash on Delivery, UPI

## 🛠️ Technologies Used

- **Python 3.12**: Core programming language
- **Streamlit 1.29.0**: Web application framework
- **Pandas 2.1.4**: Data manipulation and analysis
- **Plotly 5.18.0**: Interactive visualizations
- **NumPy 1.26.2**: Numerical computations

## 📝 Usage

1. **Apply Filters**: Use the sidebar to filter data by year, month, category, and city
2. **View Metrics**: Monitor KPIs at the top of the dashboard
3. **Analyze Trends**: Explore sales trends and patterns across different dimensions
4. **Customer Insights**: Review RFM segmentation to understand customer behavior
5. **Product Analysis**: Identify top-performing products and categories

## 🔍 RFM Segmentation Methodology

The RFM model scores customers based on three dimensions:

1. **Recency (R)**: How recently did the customer make a purchase?
   - Score 5: Most recent purchasers
   - Score 1: Haven't purchased in a long time

2. **Frequency (F)**: How often does the customer purchase?
   - Score 5: Frequent buyers
   - Score 1: One-time buyers

3. **Monetary (M)**: How much does the customer spend?
   - Score 5: High spenders
   - Score 1: Low spenders

Each dimension is scored 1-5, and the combined RFM score (3-15) determines the customer segment.

## 💡 Business Insights

This dashboard helps answer key business questions:
- Which customer segments drive the most revenue?
- What are the trending products and categories?
- Which sellers and brands perform best?
- What payment methods do customers prefer?
- Which cities generate the most sales?
- Who are the at-risk customers that need retention efforts?
- What is the profit margin across different segments?

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is open source and available under the MIT License.

## 👨‍💻 Author

**Bhart Chauhan**

## 🙏 Acknowledgments

- Built with Streamlit for rapid dashboard development
- Plotly for beautiful interactive visualizations
- Sample data generated for demonstration purposes
