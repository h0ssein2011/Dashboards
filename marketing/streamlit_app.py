import streamlit as st
from pathlib import Path
import pandas as pd

st.write('test app')

def load_data():
    path = Path(__file__).parent
    path_csv = path /'data/bank-full.csv'
    path_additional = path /'data/bank-additional-full.csv'
    bank = pd.read_csv(path_csv,sep=';')
    bank_addition = pd.read_csv(path_additional,sep=';')
    return bank , bank_addition

def set_sessions():
    if 'bank_data' not in st.session_state:
        st.session_state['bank_data'] = load_data()

if __name__ == "__main__":
    set_sessions()
