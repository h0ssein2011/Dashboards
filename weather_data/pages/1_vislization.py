import streamlit as st
import pandas as pd
from utils.data_manager import load_data,tweak_data
from utils.make_charts import Make_linechart


df = load_data(path='data/weather_data.csv')
st.write(df.head())
st.write(df.dtypes)

df = tweak_data(df)
st.write(df.dtypes)
st.write(df.head())
# st.write(df.Location.value_counts())

grouped = df.groupby('Location')['temperature_c'].mean().reset_index()
st.write(grouped.head())
fig = Make_linechart(grouped, x='location',y='temperature_c',name='Avg temp per city')
st.plotly_chart(fig)