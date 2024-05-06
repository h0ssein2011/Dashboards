import streamlit as st
import pandas as pd

import plotly.graph_objects as go
import plotly.express as px
from pathlib import Path

from streamlit_app import set_sessions
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
    kpi_dict =  {'count users':count_users,
            'count affliate user':count_affliate_user,
            'count new user':count_new_user,
            'count first time deposit user':count_ftd_user,
            'count deposit user':count_deposit_user
            }
    for i, (col, (kpi_name, kpi_value)) in enumerate(zip(st.columns(5), zip(kpi_dict.keys(), kpi_dict.values()))):
        col.metric(label=kpi_name, value=kpi_value)
calc_kpis(data)

st.markdown("""<hr style="height:2px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)
df_deposit = data[data.deposit_amount > 0]
df_withdraw = data[data.withdraw_amount > 0]
title_deposit = '# User with deposit transaction'
title_withdraw = '# User with withdraw transaction'


if timeframe == 'Daily':
    grouped = data.groupby(['brand',data.date.dt.strftime('%Y-%m-%d')]).agg({'user_id':'nunique',}).reset_index().rename(columns={'user_id':'count_users'})
    title,x_title = '# Active users per day', 'date'
    grouped_deposit = df_deposit.groupby(['brand',df_deposit.date.dt.strftime('%Y-%m-%d')]).agg({'user_id':'nunique',}).reset_index().rename(columns={'user_id':'count_users'})
    grouped_withdraw  = df_withdraw.groupby(['brand',df_withdraw.date.dt.strftime('%Y-%m-%d')]).agg({'user_id':'nunique',}).reset_index().rename(columns={'user_id':'count_users'})

if timeframe == 'Weekly':
    grouped = data.groupby(['brand',data.date.dt.strftime('%Y-%W')]).agg({'user_id':'nunique',}).reset_index().rename(columns={'user_id':'count_users'})
    title,x_title = '# Active users per Week', 'week'
    grouped_deposit = df_deposit.groupby(['brand',df_deposit.date.dt.strftime('%Y-%W')]).agg({'user_id':'nunique',}).reset_index().rename(columns={'user_id':'count_users'})
    grouped_withdraw  = df_withdraw.groupby(['brand',df_withdraw.date.dt.strftime('%Y-%W')]).agg({'user_id':'nunique',}).reset_index().rename(columns={'user_id':'count_users'})

if timeframe == 'Monthly':
    grouped = data.groupby(['brand',data.date.dt.strftime('%Y-%m')]).agg({'user_id':'nunique',}).reset_index().rename(columns={'user_id':'count_users'})
    title,x_title = '# Active users per Month', 'month'
    grouped_deposit = df_deposit.groupby(['brand',df_deposit.date.dt.strftime('%Y-%m')]).agg({'user_id':'nunique',}).reset_index().rename(columns={'user_id':'count_users'})
    grouped_withdraw  = df_withdraw.groupby(['brand',df_withdraw.date.dt.strftime('%Y-%m')]).agg({'user_id':'nunique',}).reset_index().rename(columns={'user_id':'count_users'})

fig = Create_line_chart(grouped
                              ,x='date',y='count_users',color='brand'
                              , title=title
                              ,x_title=x_title,y_title='Count users'
                              ,width=1200
                              )

st.plotly_chart(fig)

fig = Create_line_chart(grouped_deposit
                              ,x='date',y='count_users',color='brand'
                              , title=title_deposit
                              ,x_title=x_title,y_title='Count users'
                              ,width=1200
                              )

st.plotly_chart(fig)

fig = Create_line_chart(grouped_withdraw
                              ,x='date',y='count_users',color='brand'
                              , title=title_withdraw
                              ,x_title=x_title,y_title='Count users'
                              ,width=1200
                              )

st.plotly_chart(fig)
