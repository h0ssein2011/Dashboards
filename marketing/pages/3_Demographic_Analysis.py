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
selected_marital = st.sidebar.multiselect("job",bank.marital.unique(),default=bank.marital.unique())
selected_edu = st.sidebar.multiselect("job",bank.education.unique(),default=bank.education.unique())

bank = bank.query('job.isin(@selected_jobs) and marital.isin(@selected_marital) and education.isin(@selected_edu) ')


job_counts = bank.job.value_counts()
colors = [[211, 199, 5], [98, 90, 5], [210, 179, 112],
          [220, 143, 165], [32, 134, 50], [167, 93, 127], [154, 27, 66]
          , [251, 70, 171], [140, 96, 85], [234, 120, 153],
          [248, 252, 186], [220, 17, 144]]

fig = go.Figure(data=[go.Pie(labels=job_counts.index, values=job_counts.values )])
fig.update_traces(hoverinfo='label+percent', textinfo='label+percent', textfont_size=14,
                  marker=dict(colors=colors, line=dict(color='#000000', width=2)))
fig.update_layout(title='Customers job distribution')


st.plotly_chart(fig)



marital_cnt =bank.marital.value_counts()
colors = [[211, 199, 5], [98, 90, 5], [210, 179, 112]]

fig = go.Figure(data=[go.Pie(labels=marital_cnt.index, values=marital_cnt.values )])
fig.update_traces(hoverinfo='label+percent', textinfo='label+percent', textfont_size=14,
                marker=dict(colors=colors, line=dict(color='#000000', width=2)))
fig.update_layout(title='Customer marital distribution')
st.plotly_chart(fig)

education_cnt =bank.education.value_counts()
colors = [[211, 199, 5], [98, 90, 5], [210, 179, 112],[220, 143, 165]]
fig = go.Figure(data=[go.Pie(labels=education_cnt.index, values=education_cnt.values )])
fig.update_traces(hoverinfo='label+percent', textinfo='label+percent', textfont_size=14,
                marker=dict(colors=colors, line=dict(color='#000000', width=2)))
fig.update_layout(title='Customer education distribution')
st.plotly_chart(fig)


# fig = go.Figure()
# for job in bank.job.unique():
#     balance = bank.loc[bank.job == job,'balance'].values
#     fig.add_trace(go.Box(y=balance, name=job) )
