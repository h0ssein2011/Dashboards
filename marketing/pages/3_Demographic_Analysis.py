import streamlit as st
import pandas as pd
from streamlit_app import set_sessions
import plotly.graph_objects as go
import plotly.express as px


if 'bank_data' not in st.session_state:
    set_sessions()
    bank , bank_addition  = st.session_state['bank_data']
else:
    bank , bank_addition  = st.session_state['bank_data']

st.sidebar.multiselect("job",bank.job.unique(),default='technician')

fig = go.Figure()
for job in bank.job.unique():
    balance = bank.loc[bank.job == job,'balance'].values
    fig.add_trace(go.Box(y=balance, name=job) )

st.plotly_chart(fig)

