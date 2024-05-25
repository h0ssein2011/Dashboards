import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px


def create_chart(data:pd.DataFrame,x:str,y:str,title:str,x_title:str,y_title:str, width=600,height=400,chart_type:str='line',color:str|None=None):
    fig = go.Figure()
    if chart_type == 'line':
        fig = px.line(data,x=x,y=y,color=color)
    elif chart_type == 'bar':
        fig = px.bar(data,x=x,y=y,color=color)

    fig.update_layout(
        title=title,
        width=width,
        height=height,
        xaxis_title=x_title,
        yaxis_title=y_title
    )

    return fig

