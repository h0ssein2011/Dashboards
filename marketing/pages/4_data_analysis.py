import numpy as np
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

selected_jobs = st.sidebar.multiselect("job",bank.job.unique(),default=bank.job.unique())
selected_marital = st.sidebar.multiselect("marital status",bank.marital.unique(),default=bank.marital.unique())
selected_edu = st.sidebar.multiselect("education level",bank.education.unique(),default=bank.education.unique())

bank = bank.query('job.isin(@selected_jobs) and marital.isin(@selected_marital) and education.isin(@selected_edu) ')
bank_grouped = bank.groupby('job')['balance'].mean().reset_index()
bank_grouped.sort_values(by='balance',inplace=True,ascending=False)
# st.write(bank_grouped.head())

fig = go.Figure()
fig = px.bar(bank_grouped,x='job',y=['balance'], barmode="group")

fig.update_layout(
    title="Average Balance per job title",
    width=700,
    height=600,
    xaxis_title="Job",
    yaxis_title="Balance($)"
)

st.plotly_chart(fig)