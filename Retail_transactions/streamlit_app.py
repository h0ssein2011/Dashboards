import streamlit as st
from pathlib import Path
import pandas as pd
from utils.funcs import load_css
import plotly.graph_objects as go
import plotly.express as px


def main():
    st.set_page_config(layout="wide")
    markdown_content = """

        """
    st.markdown(markdown_content , unsafe_allow_html=True)

def load_data():
    path = Path(__file__).parent
    path_csv = path /'data/Retail_Transaction_Dataset.csv'
    df = pd.read_csv(path_csv)
    return df

def set_sessions():
    if  'data_loaded' not in  st.session_state:

        df = load_data()
    st.session_state['data_loaded'] = True
    return df


if __name__ == "__main__":
    main()
    df = set_sessions()
    df['TransactionDate'] = pd.to_datetime(df['TransactionDate'])
    # st.write(df.columns)

    path = Path(__file__).parent
    path_css = path / 'utils/styles.css'
    load_css(path_css)

    count_users = df.CustomerID.nunique()
    count_products = df.ProductID.nunique()
    count_days = df.TransactionDate.dt.date.nunique()


    # Define the KPI section
    st.markdown(f"""
    <div class="kpi-container">
        <div class="kpi-box">
            <h2>{count_users}</h2>
            <p>Count Customers</p>
        </div>
        <div class="kpi-box">
            <h2>{count_products}</h2>
            <p>Count Products </p>
        </div>
        <div class="kpi-box">
            <h2>{count_days}</h2>
            <p>Count Days</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    df['TransactionDate_'] = df['TransactionDate'].dt.date

    grouped = df.groupby('TransactionDate_')['Quantity'].sum().reset_index()

    fig = go.Figure()
    fig = px.line(grouped,x='TransactionDate_',y='Quantity')
    fig.update_layout(
        title="Number of orders per day",
        width=700,
        height=600,
        xaxis_title="day",
        yaxis_title="count orders"
    )
    st.plotly_chart(fig)

