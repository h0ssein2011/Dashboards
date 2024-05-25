import streamlit as st
from pathlib import Path
import pandas as pd


def Generate_sidebar(data):
    min_date = data.orderdate.min()
    max_date = data.orderdate.max()

    status = data.status.unique()
    productline = data.productline.unique()
    country = data.country.unique()
    city = data.city.unique()
    deal_size = data.dealsize.unique()


    start_date = st.sidebar.date_input('start date ',value = min_date, min_value=min_date, max_value=max_date, format="DD/MM/YYYY")
    end_date = st.sidebar.date_input('end date ',value = max_date, min_value=min_date, max_value=max_date, format="DD/MM/YYYY")

    status = st.sidebar.multiselect("Choose status to show", status, status,key='multiselect1')
    productline = st.sidebar.multiselect("Choose product line to show", productline, productline,key='multiselect2')
    country = st.sidebar.multiselect("Choose country to show", country, country,key='multiselect4')
    city = st.sidebar.multiselect("Choose city to show", city, city,key='multiselect5')
    deal_size = st.sidebar.multiselect("Choose deal_size to show", deal_size, deal_size,key='multiselect6')


    return start_date,end_date,status,productline,country,city,deal_size


def filter_data(data):
    start_date,end_date,status,productline,country,city,deal_size= Generate_sidebar(data)
    data = data.query('status.isin(@status)')
    data = data.query('orderdate >= @start_date and orderdate <= @end_date')
    data = data.query('productline.isin(@productline)')
    data = data.query('country.isin(@country)')
    data = data.query('city.isin(@city)')
    data = data.query('dealsize.isin(@deal_size)')
    return data

