import streamlit as st
from pathlib import Path
import pandas as pd


def main():
    st.set_page_config(layout="wide")
    markdown_content = """
        ### This is a sample dashboard develped in my free time to enjoy the time and explore marketing analysis
        ### there are 3 pages so far:
            ➡ intro
            ➡ Sample data
            ➡ 3_Demographic Analysis

        #### Codes : [Github](https://github.com/h0ssein2011/Dashboards/tree/main/marketing)

        """
    st.markdown(markdown_content , unsafe_allow_html=True)

def load_data():
    path = Path(__file__).parent
    path_csv = path /'data/bank-full.csv'
    path_additional = path /'data/bank-additional-full.csv'
    bank = pd.read_csv(path_csv,sep=';')
    bank_addition = pd.read_csv(path_additional,sep=';')
    return bank , bank_addition

def set_sessions():
    if 'bank_data' not in st.session_state:
        st.session_state['bank_data'] = load_data()

if __name__ == "__main__":
    set_sessions()
    main()
