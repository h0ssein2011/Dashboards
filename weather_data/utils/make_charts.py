import pandas as pd
import streamlit as st
import plotly.graph_objects as go


def Make_linechart(df,x,y,name):
    fig = go.figure()
    fig.add_trace(go.Bar(name=name, x=df.x, y=df.y))
    return fig


