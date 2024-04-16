import streamlit as st
from pathlib import Path
import pandas as pd
path = Path(__file__).parent.parent
path_csv = path /'data/bank-full.csv'
path_additional = path /'data/bank-additional-full.csv'
bank = pd.read_csv(path_csv,sep=';')
bank_addition = pd.read_csv(path_additional,sep=';')

st.markdown('### Bank sample data', unsafe_allow_html=True)
st.write(bank.head())
st.markdown('### Bank sample additional data', unsafe_allow_html=True)
st.write(bank_addition.head())