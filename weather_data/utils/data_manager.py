import streamlit as st
import pandas as pd


def load_data(path):
    return(pd.read_csv(path))

def tweak_data(data):
    def round_data(df_):
        cols = df_.select_dtypes(include='float').columns
        return  df_[cols].applymap(lambda x: round(x,2))

    return(data
           .assign(Date_Time = lambda x: pd.to_datetime(x.Date_Time)) # convert to datetime
           .pipe(round_data)
           )


