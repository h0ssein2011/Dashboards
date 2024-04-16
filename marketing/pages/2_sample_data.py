import streamlit as st
import pandas as pd
bank = pd.read_csv('data/bank-full.csv')
st.write(bank.head())