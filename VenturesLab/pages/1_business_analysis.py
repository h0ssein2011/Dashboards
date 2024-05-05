import streamlit as st
import pandas as pd
from streamlit_app import set_sessions
from utils.create_sidebar import filter_data
from utils.make_charts import Create_line_chart
from utils.data_manager import format_number


import plotly.graph_objects as go
import plotly.express as px
from pathlib import Path



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


data,timeframe = filter_data(data)
# st.write(data.head())


def calc_kpis(data):
    GGR_total = round(data.casino_GGR.sum() + data.sports_GGR.sum(),0)
    GGR_casino = round(data.casino_GGR.sum(),0)
    GGR_sports = round(data.sports_GGR.sum(),0)
    Total_Deposits = round(data.deposit_amount.sum(),0)
    Total_Withdrawals = round(data.withdraw_amount.sum(),0)
    Total_Net_Deposits = Total_Deposits - Total_Withdrawals
    Total_casino_bet = round(data.casino_bet_amount.sum(),0)
    Total_casino_win = round(data.casino_win_amount.sum(),0)
    Total_sports_bet = round(data.sports_bet_amount.sum(),0)
    Total_sports_win = round(data.sports_win_amount.sum(),0)

    kpi_dict =  {'GGR_total':format_number(GGR_total),
            'GGR_casino':format_number(GGR_casino),
            'GGR_sports':format_number(GGR_sports),
            'Total_Deposits':format_number(Total_Deposits),
            'Total_Withdrawals':format_number(Total_Withdrawals),
            'Total_Net_Deposits':format_number(Total_Net_Deposits),
            'Total_casino_bet':format_number(Total_casino_bet),
            'Total_casino_win':format_number(Total_casino_win),
            'Total_sports_bet':format_number(Total_sports_bet),
            'Total_sports_win':format_number(Total_sports_win),
            }
    for i, (col, (kpi_name, kpi_value)) in enumerate(zip(st.columns(10), zip(kpi_dict.keys(), kpi_dict.values()))):
        col.metric(label=kpi_name, value=kpi_value)
calc_kpis(data)

st.markdown("""<hr style="height:2px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)


grouped = data.groupby('product_status').agg({'total_GGR':'sum','user_id':'nunique'}).reset_index().rename(columns={'user_id':'count_users'})
grouped = grouped[grouped.product_status !='Unknown']

colors = [[211, 199, 5], [98, 90, 5], [210, 179, 112],[220, 143, 165], ]
fig_ggr = go.Figure(data=[go.Pie(labels=grouped.product_status, values=grouped.total_GGR )])
fig_ggr.update_traces(hoverinfo='label+percent', textinfo='label+percent', textfont_size=14,
                  marker=dict(colors=colors, line=dict(color='#000000', width=2)))
fig_ggr.update_layout(title='GGR by product')

fig_usr = go.Figure(data=[go.Pie(labels=grouped.product_status, values=grouped.count_users )])
fig_usr.update_traces(hoverinfo='label+percent', textinfo='label+percent+value', textfont_size=14,
                  marker=dict(colors=colors, line=dict(color='#000000', width=2)))
fig_usr.update_layout(title='Active user by product')

col1,col2 = st.columns(2)
with col1:
    st.plotly_chart(fig_ggr)
with col2:
    st.plotly_chart(fig_usr)


if timeframe == 'Daily':
    grouped = data.groupby(['product_status',data.date.dt.strftime('%Y-%m-%d')]).agg({'total_GGR':'sum'}).reset_index()
    title,x_title = 'GGR per day', 'date'
if timeframe == 'Weekly':
    grouped = data.groupby(['product_status',data.date.dt.strftime('%Y-%W')]).agg({'total_GGR':'sum'}).reset_index()
    title,x_title = 'GGR per Week', 'week'

if timeframe == 'Monthly':
    grouped = data.groupby(['product_status',data.date.dt.strftime('%Y-%m')]).agg({'total_GGR':'sum'}).reset_index()
    title,x_title = 'GGR per Month', 'month'


grouped = grouped[grouped.product_status !='Unknown']
fig = Create_line_chart(grouped
                              ,x='date',y='total_GGR',color='product_status'
                              , title=title
                              ,x_title=x_title,y_title='GGR amount'
                              ,width=1500
                              )


st.plotly_chart(fig)