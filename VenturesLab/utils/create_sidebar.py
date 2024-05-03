import streamlit as st
from pathlib import Path
import pandas as pd


def Generate_sidebar(data):
    min_date = data.date.min()
    max_date = data.date.max()
    brands = data.brand.unique()
    new_user ={'Yes':1,'No':0}
    first_depositor ={'Yes':1,'No':0}
    is_affiliate = {'Yes':1,'No':0}

    start_date = st.sidebar.date_input('start date ',value = min_date, min_value=min_date, max_value=max_date, format="DD/MM/YYYY")
    end_date = st.sidebar.date_input('end date ',value = max_date, min_value=min_date, max_value=max_date, format="DD/MM/YYYY")

    brands = st.sidebar.multiselect("Choose Brands to show", brands, brands,key='multiselect1')
    new_user_sb = st.sidebar.multiselect("New user status", new_user.keys(), new_user.keys(),key='multiselect2')
    new_user = [new_user[t] for t in new_user_sb]
    first_depositor_sb = st.sidebar.multiselect("First Depositor Status", first_depositor.keys(), first_depositor.keys(),key='multiselect3')
    first_depositor = [first_depositor[t] for t in first_depositor_sb]
    is_affiliate_sb = st.sidebar.multiselect("Affiliate Yser Status", is_affiliate.keys(), is_affiliate.keys(),key='multiselect4')
    is_affiliate = [is_affiliate[t] for t in is_affiliate_sb]

    return start_date,end_date,brands,new_user,first_depositor,is_affiliate


def filter_data(data):
    start_date,end_date,brands,new_user,first_depositor ,is_affiliate= Generate_sidebar(data)
    data = data.query('date >= @start_date and date <= @end_date')
    data = data.query('brand.isin(@brands)')
    data = data.query('new_registration.isin(@new_user)')
    data = data.query('first_time_deposit.isin(@first_depositor)')
    data = data.query('is_affiliate.isin(@is_affiliate)')
    return data

