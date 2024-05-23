import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px


from utils.data_manger import set_sessions

if 'sales_data' not in st.session_state:
    set_sessions()
    data = st.session_state['sales_data']
else:
    data = st.session_state['sales_data']

st.write(data.head())

grouped = data.groupby(data.orderdate.dt.strftime('%Y-%m'))['quantityordered'].sum().reset_index()

fig = go.Figure()
fig = px.line(grouped,x='orderdate',y='quantityordered')
fig.update_layout(
    title="Number of orders per day",
    width=700,
    height=600,
    xaxis_title="date",
    yaxis_title="count orders"
)

st.plotly_chart(fig)