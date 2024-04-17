import streamlit as st
import pandas as pd
from streamlit_app import set_sessions

if 'bank_data' not in st.session_state:
    set_sessions()
    bank , bank_addition  = st.session_state['bank_data']
else:
    bank , bank_addition  = st.session_state['bank_data']





st.markdown('### Bank sample data', unsafe_allow_html=True)
st.write(bank.head())
st.markdown('### Bank sample additional data', unsafe_allow_html=True)
st.write(bank_addition.head())