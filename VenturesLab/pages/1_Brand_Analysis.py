import streamlit as st
import pandas as pd
from utils.data_manager import set_sessions
from utils.create_sidebar import filter_data
from utils.make_charts import Create_line_chart

import plotly.graph_objects as go
import plotly.express as px

st.set_page_config(layout="wide")

if 'player_data' not in st.session_state:
    set_sessions()
    data = st.session_state['player_data']
else:
    data = st.session_state['player_data']


data = filter_data(data)
st.write(data.columns)
grouped = data.groupby(['brand',data.date.dt.strftime('%Y-%m')]).agg({
                'deposit_amount':sum,
                'withdraw_amount':sum,
                'casino_bet_amount':sum,
                'casino_win_amount':sum,
                'sports_bet_amount':sum,
                'sports_win_amount':sum,
                }).reset_index()


col1,col2 = st.columns(2)
fig = Create_line_chart(data=grouped,x='date',y='deposit_amount',color='brand', title="Total deposit amount per month",x_title='month',y_title='deposit amount')
with col1:
    st.plotly_chart(fig)
fig = Create_line_chart(data=grouped,x='date',y='withdraw_amount',color='brand', title="Total withdraw amount per month",x_title='month',y_title='withdraw amount')
with col2:
    st.plotly_chart(fig)
with st.expander("💬 **it seems brand L has highest amount of deposit as well as withdrawals**" ):

    # Show comments

    st.write("")

col1,col2 = st.columns(2)
fig = Create_line_chart(data=grouped,x='date',y='deposit_amount',color='brand', title="Total deposit amount per month",x_title='month',y_title='deposit amount')
with col1:
    st.plotly_chart(fig)
fig = Create_line_chart(data=grouped,x='date',y='withdraw_amount',color='brand', title="Total withdraw amount per month",x_title='month',y_title='withdraw amount')
with col2:
    st.plotly_chart(fig)
with st.expander("💬 **it seems brand L has highest amount of deposit as well as withdrawals**" ):

    # Show comments

    st.write("")


col1,col2 = st.columns(2)
fig = Create_line_chart(data=grouped,x='date',y='casino_bet_amount',color='brand', title="Total Casino bet amount per month",x_title='month',y_title='Casino bet amount')
with col1:
    st.plotly_chart(fig)
fig = Create_line_chart(data=grouped,x='date',y='casino_win_amount',color='brand', title="Total Casino win amount per month",x_title='month',y_title='Casino win amount')
with col2:
    st.plotly_chart(fig)
with st.expander("💬 **it seems brand L has highest amount of deposit as well as withdrawals**" ):

    # Show comments

    st.write("")

col1,col2 = st.columns(2)
fig = Create_line_chart(data=grouped,x='date',y='sports_bet_amount',color='brand', title="Total Sports bet amount per month",x_title='month',y_title='Sports bet amount')
with col1:
    st.plotly_chart(fig)
fig = Create_line_chart(data=grouped,x='date',y='sports_bet_amount',color='brand', title="Total Sports win amount per month",x_title='month',y_title='Sports win amount')
with col2:
    st.plotly_chart(fig)
with st.expander("💬 **it seems brand L has highest amount of deposit as well as withdrawals**" ):
        st.write("")




