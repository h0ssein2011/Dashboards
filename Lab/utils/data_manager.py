import re
import numpy as np
import streamlit as st
from pathlib import Path
import pandas as pd

def tweak_data(df):
    def get_integer(id):
        id = str(id)
        temp = re.findall(r'\d+', id)
        if temp:
            return int(temp[0])
        else:
            return 0
    df = df.fillna(0)
    return (df
            .assign(date = lambda x:pd.to_datetime(x.date,format='%d/%m/%Y')
                    ,casino_GGR = lambda x:(x.casino_bet_amount - x.casino_win_amount)
                    ,sports_GGR = lambda x:(x.sports_bet_amount - x.sports_win_amount)
                    ,user_affiliate_id = lambda x:x.user_affiliate_id.map(get_integer)
                    ,is_affiliate = lambda x:np.where(x.user_affiliate_id > 0,1,0)
                    )
                    .assign(product_status = lambda x:np.where((x.casino_GGR != 0) & (x.sports_GGR==0),'Casino'
                                                        ,np.where((x.casino_GGR==0) & (x.sports_GGR != 0),'Sports'
                                                        ,np.where((x.casino_GGR==0) & (x.casino_GGR == 0),'Unknown','Both')))
                    ,total_GGR = lambda x: x.casino_GGR + x.sports_GGR
                                                        )

    )


def load_data():
    path = Path(__file__).parent
    path_csv = path /'../data/data.csv'
    data = pd.read_csv(path_csv,sep=',')
    data = tweak_data(data)
    return data

def set_sessions():
    if 'player_data' not in st.session_state:
        st.session_state['player_data'] = load_data()

def format_number(num):
    if num >= 1_000_000_000:
        formatted_num = f"{num / 1_000_000_000:.1f}B"
    elif num >= 1_000_000:
        formatted_num = f"{num / 1_000_000:.1f}M"
    elif num >= 1_000:
        formatted_num = f"{num / 1_000:.1f}K"
    else:
        formatted_num = str(num)
    return formatted_num