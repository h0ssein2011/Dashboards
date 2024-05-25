import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px


from utils.data_manger import set_sessions
from utils.create_sidebar import filter_data
from utils.make_charts import create_chart

if 'sales_data' not in st.session_state:
    set_sessions()
    data = st.session_state['sales_data']
else:
    data = st.session_state['sales_data']

st.write(data.head())
# st.write(data.columns)
data = filter_data(data)

grouped = data.groupby([data.orderdate.dt.strftime('%Y-%m'),'dealsize'])['quantityordered'].sum().reset_index()
fig = create_chart(grouped,x='orderdate',y='quantityordered',title="Number of orders per day",x_title='date',y_title='count orders',chart_type='line',color='dealsize')
st.plotly_chart(fig)


grouped = data.groupby(['country','dealsize'])['quantityordered'].sum().reset_index().sort_values(by='quantityordered',ascending=False)
fig = create_chart(grouped,x='country',y='quantityordered',title="Number of orders per country",x_title='Country',y_title='count orders',chart_type='bar',color='dealsize')
st.plotly_chart(fig)

grouped = data.groupby('dealsize')['sales'].mean().reset_index()
fig = create_chart(grouped,x='dealsize',y='sales',title="Average sales per deal size",x_title='deal size',y_title='sales amount',chart_type='bar')
st.plotly_chart(fig)


grouped = data.groupby('status')['ordernumber'].size().reset_index()
fig = create_chart(grouped,x='status',y='ordernumber',title="Count status",x_title='status',y_title='count order',chart_type='bar')
st.plotly_chart(fig)

grouped = data.groupby('productline')['ordernumber'].size().reset_index().sort_values(by='ordernumber',ascending=False)
fig = create_chart(grouped,x='productline',y='ordernumber',title="Count orders per productline",x_title='productline',y_title='count order',chart_type='bar')
st.plotly_chart(fig)