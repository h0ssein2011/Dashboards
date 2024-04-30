import streamlit as st
import pandas as pd
from streamlit_app import set_sessions

if 'player_data' not in st.session_state:
    set_sessions()
    data = st.session_state['player_data']
else:
    data = st.session_state['player_data']





st.markdown('### sample data', unsafe_allow_html=True)
st.write(data.head())
st.write(data.brand.unique())
