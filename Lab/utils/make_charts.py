import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px


def Create_line_chart(data:pd.DataFrame,x:str,y:str,color:str|None,title:str,x_title:str,y_title:str, width=600,height=400):
    fig = go.Figure()
    fig = px.line(data,x=x,y=y,color=color)
    fig.update_layout(
        title=title,
        width=width,
        height=height,
        xaxis_title=x_title,
        yaxis_title=y_title
    )
    fig.update_traces(line={'width': 3})

    return fig