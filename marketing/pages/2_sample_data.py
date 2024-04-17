import streamlit as st
import pandas as pd
from main import set_sessions

try:
    bank , bank_addition  = st.session_state['bank_data']
except:
    st.write('data did not loaded')
    set_sessions()



st.markdown('### Bank sample data', unsafe_allow_html=True)
st.write(bank.head())
st.markdown('### Bank sample additional data', unsafe_allow_html=True)
st.write(bank_addition.head())