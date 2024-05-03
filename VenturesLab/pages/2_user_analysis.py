import streamlit as st
import pandas as pd
from streamlit_app import set_sessions
from utils.create_sidebar import filter_data
from utils.make_charts import Create_line_chart


import plotly.graph_objects as go
import plotly.express as px
from pathlib import Path
import pandas as pd



st.set_page_config(layout="wide")



if 'player_data' not in st.session_state:
    set_sessions()
    data = st.session_state['player_data']
else:
    data = st.session_state['player_data']


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

path = Path(__file__).parent
local_css(path / '../utils/style.css')


data = filter_data(data)
# st.write(data.head())

count_users = data.user_id.nunique()
count_affliate_user = data.query('user_affiliate_id.isna()').user_id.nunique()
count_new_user = data.query('new_registration== 1 ').user_id.nunique()
count_ftd_user = data.query('first_time_deposit== 1 ').user_id.nunique()

kpi_html = """
<div class="kpi-container">
    <div class="kpi">
        <div class="number">{count_users}</div>
        <div class="label">Count Users</div>
    </div>
    <div class="kpi">
        <div class="number">{count_affliate_user}</div>
        <div class="label">Count Affliate User</div>
    </div>
    <div class="kpi">
        <div class="number">{count_new_user}</div>
        <div class="label">Count New User</div>
    </div>
    <div class="kpi">
        <div class="number">{count_ftd_user}</div>
        <div class="label">Count First Time Depositor</div>
    </div>

</div>
"""
st.markdown(kpi_html.format(count_users=count_users, count_affliate_user=count_affliate_user,
                             count_new_user=count_new_user,
                             count_ftd_user=count_ftd_user), unsafe_allow_html=True)

grouped = data.groupby(['brand',data.date.dt.strftime('%Y-%m')]).agg({
                'user_id':'nunique',
                }).reset_index().rename(columns={'user_id':'count_users'})
# st.write(grouped)
fig_total = Create_line_chart(data=grouped
                              ,x='date',y='count_users',color='brand'
                              , title="Active users per month"
                              ,x_title='month',y_title='Count users'
                              ,width=500
                              )


casino_players = data[data.casino_bet_amount > 0]
grouped = casino_players.groupby(['brand',casino_players.date.dt.strftime('%Y-%m')]).agg({
                'user_id':'nunique',
                }).reset_index().rename(columns={'user_id':'count_users'})
# st.write(grouped)
fig_casino = Create_line_chart(data=grouped,x='date'
                               ,y='count_users',color='brand'
                               , title="Active Casino player per month"
                               ,x_title='month',y_title='Count users'
                               ,width=500
                               )

sport_players = data[data.sports_bet_amount > 0]
grouped = sport_players.groupby(['brand',sport_players.date.dt.strftime('%Y-%m')]).agg({
                'user_id':'nunique',
                }).reset_index().rename(columns={'user_id':'count_users'})
# st.write(grouped)
fig_sports = Create_line_chart(data=grouped,x='date',y='count_users'
                               ,color='brand', title="Active Sports player per month"
                               ,x_title='month',y_title='Count users'
                               ,width=500
                               )

col1,col2,col3 = st.columns(3)

with col1:
    st.plotly_chart(fig_total)

with col2:
    st.plotly_chart(fig_casino)

with col3:
    st.plotly_chart(fig_sports)