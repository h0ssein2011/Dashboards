import streamlit as st
from pathlib import Path
import pandas as pd
path = Path()
path_csv = path /'data/bank-full.csv'
bank = pd.read_csv(path_csv,sep=';')
st.write(bank.head())