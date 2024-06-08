import streamlit as st
import pandas as pd
from utils.data_manager import load_data,tweak_data


df = load_data(path='data/weather_data.csv')
st.write(df.head())
st.write(df.dtypes)

df = tweak_data(df)
st.write(df.dtypes)
st.write(df.head())
# st.write(df.Location.value_counts())
