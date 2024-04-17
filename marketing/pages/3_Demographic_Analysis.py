import streamlit as st
import pandas as pd
from main import load_data

try:
    bank , bank_addition  = st.session_state['bank_data']
except:
    load_data()
    bank , bank_addition  = st.session_state['bank_data']


st.markdown('### Bank sample data', unsafe_allow_html=True)
st.write(bank.head())
st.markdown('### Bank sample additional data', unsafe_allow_html=True)
st.write(bank_addition.head())