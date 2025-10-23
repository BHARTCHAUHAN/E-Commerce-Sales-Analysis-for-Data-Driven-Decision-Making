# Quick Start Guide

## 🚀 Get Started in 3 Steps

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: (Optional) Generate Fresh Sample Data
```bash
python generate_sample_data.py
```
*Note: Sample data is already included in the repository*

### Step 3: Launch the Dashboard
```bash
streamlit run dashboard.py
```

Then open your browser to: **http://localhost:8501**

---

## 📊 View Demo Report

To see a comprehensive analysis report in your terminal:
```bash
python demo.py
```

This will display:
- Key performance metrics
- Category and brand analysis
- RFM customer segmentation insights
- Business recommendations

---

## 🎯 Dashboard Features

### Interactive Filters (Sidebar)
- **Year**: Filter by 2022, 2023, or 2024
- **Month**: Select specific months
- **Category**: Filter by product categories
- **City**: Focus on specific cities

### Key Metrics Displayed
1. **Total Orders**: Number of transactions
2. **Net Sales**: Total revenue
3. **Total Profit**: Profit amount and margin percentage
4. **Units Sold**: Total items sold

### Visualizations Available
- Monthly sales trends (line chart)
- Payment method distribution (pie chart)
- Sales by category (bar chart)
- Top brands by revenue (horizontal bar)
- Seller performance (scatter plot)
- Sales by city (bar chart)
- RFM customer segmentation (multiple charts)
- Top performing products (data table)

---

## 🎨 RFM Customer Segments Explained

### Champions (Best Customers)
- **RFM Score**: 13-15
- **Characteristics**: Recent, frequent, high-value purchases
- **Action**: Reward with VIP programs, exclusive offers

### Loyal Customers
- **RFM Score**: 10-12
- **Characteristics**: Regular purchases, good spending
- **Action**: Keep engaged with loyalty programs

### Potential Loyalists
- **RFM Score**: 7-9
- **Characteristics**: Recent customers with growth potential
- **Action**: Nurture with targeted offers

### At Risk
- **RFM Score**: 5-6
- **Characteristics**: Haven't purchased recently
- **Action**: Win-back campaigns, special discounts

### Lost Customers
- **RFM Score**: 1-4
- **Characteristics**: Inactive for a long time
- **Action**: Re-engagement surveys, comeback offers

---

## 💡 Tips for Best Experience

1. **Start Broad**: Begin with all filters selected to see the full picture
2. **Drill Down**: Use filters to analyze specific segments
3. **Compare Periods**: Use year/month filters to compare time periods
4. **Hover for Details**: Hover over charts for detailed information
5. **Full Screen**: Click the full-screen icon on any chart for detailed view

---

## 🔧 Customization

### Modify Sample Data
Edit `generate_sample_data.py` to change:
- Number of records
- Date ranges
- Product categories
- Cities
- Brands and sellers

Then regenerate:
```bash
python generate_sample_data.py
```

### Customize Dashboard
Edit `dashboard.py` to:
- Add new visualizations
- Change color schemes
- Modify RFM scoring logic
- Add new filters or metrics

---

## 📈 Sample Data Overview

- **Records**: 5,000 transactions
- **Period**: January 2022 - December 2024
- **Customers**: 500 unique customers
- **Categories**: 7 (Electronics, Fashion, Home & Kitchen, Sports, Books, Beauty, Toys)
- **Brands**: 8 brands
- **Cities**: 10 US cities
- **Payment Methods**: 5 methods
- **Total Revenue**: ~$5.9M
- **Total Profit**: ~$2.1M

---

## 🐛 Troubleshooting

### Dashboard won't start
```bash
# Check if all dependencies are installed
pip install -r requirements.txt

# Verify data file exists
ls -l ecommerce_sales_data.csv
```

### Port already in use
```bash
# Use a different port
streamlit run dashboard.py --server.port 8502
```

### Performance issues
- Reduce the number of records in `generate_sample_data.py`
- Close other browser tabs
- Restart the Streamlit server

---

## 📚 Learn More

- **Streamlit Documentation**: https://docs.streamlit.io
- **Plotly Documentation**: https://plotly.com/python/
- **RFM Analysis**: Learn about customer segmentation techniques

---

## 🤝 Support

For issues or questions:
1. Check the README.md for detailed documentation
2. Review the demo.py output for data insights
3. Examine the sample data in ecommerce_sales_data.csv

---

**Happy Analyzing! 📊**
