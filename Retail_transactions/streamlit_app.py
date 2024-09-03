import streamlit as st
from pathlib import Path
import pandas as pd
from utils.funcs import load_css
import plotly.express as px

def main():
    st.set_page_config(layout="wide")

    path = Path(__file__).parent
    path_css = path / 'utils/styles.css'
    load_css(path_css)


    count_users = df.CustomerID.nunique()
    count_products = df.ProductID.nunique()
    count_days = df.TransactionDate.dt.date.nunique()
    total_revenue = df['TotalAmount'].sum()
    avg_discount = df['DiscountAppliedPct'].mean()

    # Define the KPI section
    st.markdown(f"""
    <body>
    <div class="kpi-container">
        <div class="kpi-box">
            <h2>{count_users}</h2>
            <p>Unique Customers</p>
        </div>
        <div class="kpi-box">
            <h2>{count_products}</h2>
            <p>Unique Products</p>
        </div>
        <div class="kpi-box">
            <h2>{count_days}</h2>
            <p>Active Days</p>
        </div>
        <div class="kpi-box">
            <h2>${total_revenue:,.2f}</h2>
            <p>Total Revenue</p>
        </div>
        <div class="kpi-box">
            <h2>{avg_discount:.2f}%</h2>
            <p>Average Discount</p>
        </div>
    </div>
</body>

    """, unsafe_allow_html=True)

    df['TransactionDate_'] = df['TransactionDate'].dt.date
    c1,c2 = st.columns(2)

    # Line chart: Number of orders per day
    grouped = df.groupby('TransactionDate_')['Quantity'].sum().reset_index()
    fig = px.line(grouped, x='TransactionDate_', y='Quantity',
                  title="📈 Daily Orders Trend",
                  labels={"TransactionDate_": "Transaction Date", "Quantity": "Number of Orders"},
                  color_discrete_sequence=["#3498db"])
    fig.update_layout(
        title_font=dict(size=24, family='Arial, sans-serif'),
        width=800,
        height=500,
        paper_bgcolor='#f0f2f6',
        plot_bgcolor='#ffffff',
    )
    with c1:
        st.plotly_chart(fig)

    # Time series chart: Revenue Over Time
    revenue_over_time = df.groupby('TransactionDate_')['TotalAmount'].sum().reset_index()
    fig = px.line(revenue_over_time, x='TransactionDate_', y='TotalAmount',
                  title="📅 Revenue Over Time",
                  labels={"TransactionDate_": "Date", "TotalAmount": "Revenue"},
                  color_discrete_sequence=["#04cf77"])
    fig.update_layout(
        title_font=dict(size=24, family='Arial, sans-serif'),
        width=800,
        height=500,
        paper_bgcolor='#f0f2f6',
        plot_bgcolor='#ffffff',
    )
    with c2:
        st.plotly_chart(fig)

    c1,c2 = st.columns(2)

    revenue_by_category = df.groupby('ProductCategory')['TotalAmount'].sum().reset_index()
    fig = px.pie(revenue_by_category, names='ProductCategory', values='TotalAmount',
                 title="💰 Revenue by Product Category",
                 color_discrete_sequence=px.colors.sequential.Greens)
    fig.update_traces(textinfo='percent+label', pull=[0.05, 0.05, 0.05])
    fig.update_layout(
        title_font=dict(size=24, family='Arial, sans-serif'),
        width=800,
        height=500,
        paper_bgcolor='#f0f2f6',
    )
    with c1:

        st.plotly_chart(fig)

    # Pie chart: Payment Method Distribution
    payment_distribution = df['PaymentMethod'].value_counts().reset_index()
    payment_distribution.columns = ['PaymentMethod', 'Count']
    fig = px.pie(payment_distribution, names='PaymentMethod', values='Count',
                 title="💳 Payment Method Distribution",
                 color_discrete_sequence=px.colors.sequential.Plasma)
    fig.update_traces(textinfo='percent+label', pull=[0.05, 0.05, 0.05])
    fig.update_layout(
        title_font=dict(size=24, family='Arial, sans-serif'),
        width=800,
        height=500,
        paper_bgcolor='#f0f2f6',
    )
    with c2:
        st.plotly_chart(fig)

    c1,c2 = st.columns(2)

    # Scatter plot: Price vs. Quantity
    fig = px.scatter(df, x='Price', y='Quantity', size='TotalAmount', color='ProductCategory', hover_data=['CustomerID'],
                     title="💼 Price vs. Quantity (Bubble size: Total Amount)",
                     labels={"Price": "Price", "Quantity": "Quantity"},
                     color_discrete_sequence=px.colors.cyclical.IceFire)
    fig.update_layout(
        title_font=dict(size=24, family='Arial, sans-serif'),
        width=800,
        height=500,
        paper_bgcolor='#f0f2f6',
        plot_bgcolor='#ffffff',
    )
    with c1:
        st.plotly_chart(fig)

    # Histogram: Distribution of Discounts Applied
    fig = px.histogram(df, x='DiscountAppliedPct', nbins=20,
                       title="🎁 Distribution of Discounts Applied",
                       labels={"DiscountAppliedPct": "Discount Applied (%)"},
                       color_discrete_sequence=["#2ecc71"])
    fig.update_layout(
        title_font=dict(size=24, family='Arial, sans-serif'),
        width=800,
        height=500,
        paper_bgcolor='#f0f2f6',
        plot_bgcolor='#ffffff',
    )
    with c2:
        st.plotly_chart(fig)
    markdown_content = """
    <div class="footer">
     * <p> dataset : Kaggle   <h4> (https://www.kaggle.com/datasets/fahadrehman07/retail-transaction-dataset)  </h4> </p>
    """
    st.markdown(markdown_content, unsafe_allow_html=True)

def load_data():
    path = Path(__file__).parent
    path_csv = path / 'data/Retail_Transaction_Dataset.csv'
    df = pd.read_csv(path_csv)
    return df

def set_sessions():
    if 'data_loaded' not in st.session_state:
        df = load_data()
        st.session_state['data_loaded'] = True
        df['TransactionDate'] = pd.to_datetime(df['TransactionDate'])
        df = df[df.TransactionDate.dt.date >  pd.Timestamp('2023-04-29').date()] # exclude low values
    return df

if __name__ == "__main__":
    df = set_sessions()
    main()

