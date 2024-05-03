import numpy as np
import streamlit as st
from pathlib import Path
import pandas as pd

def load_data():
    path = Path(__file__).parent
    path_csv = path /'../data/data.csv'
    data = pd.read_csv(path_csv,sep=',')
    data['date'] = pd.to_datetime(data['date'],format='%d/%m/%Y')
    data['is_affiliate'] = np.where(data['user_affiliate_id'].isna() ,0,1)
    return data

def set_sessions():
    if 'player_data' not in st.session_state:
        st.session_state['player_data'] = load_data()