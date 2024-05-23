
import streamlit as st
from pathlib import Path
import pandas as pd

def load_data():
    path = Path(__file__).parent
    path_csv = path /'../data/sales_data_sample.csv'
    data = pd.read_csv(path_csv,encoding = "ISO-8859-1")
    data = tweak_data(data)
    return data

def set_sessions():
    if 'sales_data' not in st.session_state:
        st.session_state['sales_data'] = load_data()

def tweak_data(df):
    df.columns = [col.lower() for col in df.columns]
    return (df
            .assign(orderdate = lambda x : pd.to_datetime(x.orderdate))

            )