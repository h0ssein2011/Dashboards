import streamlit as st
import pandas as pd
from pathlib import Path
import plotly.graph_objects as go
import plotly.express as px

from utils.data_manager import set_sessions
from utils.create_sidebar import filter_data
from utils.make_charts import Create_line_chart


if 'player_data' not in st.session_state:
    set_sessions()
    data = st.session_state['player_data']
else:
    data = st.session_state['player_data']

data,timeframe = filter_data(data)

def calc_kpis(data):
    count_users = data.user_id.nunique()
    count_affliate_user = data.query('user_affiliate_id!=0').user_id.nunique()
    count_new_user = data.query('new_registration== 1 ').user_id.nunique()
    count_ftd_user = data.query('first_time_deposit== 1 ').user_id.nunique()
    count_deposit_user = data.query('deposit_amount > 0 ').user_id.nunique()
    kpi_dict =  {'count_users':count_users,
            'count_affliate_user':count_affliate_user,
            'count_new_user':count_new_user,
            'count_ftd_user':count_ftd_user,
            'count_deposit_user':count_deposit_user
            }
    for i, (col, (kpi_name, kpi_value)) in enumerate(zip(st.columns(5), zip(kpi_dict.keys(), kpi_dict.values()))):
        col.metric(label=kpi_name, value=kpi_value)
calc_kpis(data)
st.markdown("""<hr style="height:2px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)

if timeframe == 'Daily':
    grouped = data.groupby(['brand',data.date.dt.strftime('%Y-%m-%d')]).agg(
            {'deposit_amount':'sum',
                'withdraw_amount':'sum',
                'casino_bet_amount':'sum',
                'casino_win_amount':'sum',
                'sports_bet_amount':'sum',
                'sports_win_amount':'sum'}).reset_index()
    x_title = 'date'
if timeframe == 'Weekly':
    grouped = data.groupby(['brand',data.date.dt.strftime('%Y-%W')]).agg(
            {'deposit_amount':'sum',
                'withdraw_amount':'sum',
                'casino_bet_amount':'sum',
                'casino_win_amount':'sum',
                'sports_bet_amount':'sum',
                'sports_win_amount':'sum'}).reset_index()
    x_title =  'week'

if timeframe == 'Monthly':
    grouped = data.groupby(['brand',data.date.dt.strftime('%Y-%m')]).agg(
       {'deposit_amount':'sum',
                'withdraw_amount':'sum',
                'casino_bet_amount':'sum',
                'casino_win_amount':'sum',
                'sports_bet_amount':'sum',
                'sports_win_amount':'sum'}).reset_index()
    x_title =  'month'


col1,col2 = st.columns(2)
fig = Create_line_chart(data=grouped
                        ,x='date',y='deposit_amount'
                        ,color='brand'
                        ,title='Total deposit amount'
                        ,x_title=x_title
                        ,y_title='deposit amount')
with col1:
    st.plotly_chart(fig)
fig = Create_line_chart(data=grouped
                        ,x='date',y='withdraw_amount'
                        ,color='brand'
                        ,title='Total Withdraw amount'
                        ,x_title=x_title
                        ,y_title='withdraw amount')
with col2:
    st.plotly_chart(fig)
with st.expander("💬 **Brand L has highest amount of deposit as well as withdrawals**" ):
    st.write("")


col1,col2 = st.columns(2)
fig = Create_line_chart(data=grouped,x='date',y='casino_bet_amount',color='brand', title="Total Casino bet amount per month",x_title='month',y_title='Casino bet amount')
with col1:
    st.plotly_chart(fig)
fig = Create_line_chart(data=grouped,x='date',y='casino_win_amount',color='brand', title="Total Casino win amount per month",x_title='month',y_title='Casino win amount')
with col2:
    st.plotly_chart(fig)
with st.expander("💬 **Brand L has highest amount of Casino bet amount as well as win amount**" ):

    # Show comments

    st.write("")

col1,col2 = st.columns(2)
fig = Create_line_chart(data=grouped,x='date',y='sports_bet_amount',color='brand', title="Total Sports bet amount per month",x_title='month',y_title='Sports bet amount')
with col1:
    st.plotly_chart(fig)
fig = Create_line_chart(data=grouped,x='date',y='sports_bet_amount',color='brand', title="Total Sports win amount per month",x_title='month',y_title='Sports win amount')
with col2:
    st.plotly_chart(fig)
with st.expander("💬 **Brand L has highest amount of Sports bet amount as well as win amount**" ):
        st.write("")




