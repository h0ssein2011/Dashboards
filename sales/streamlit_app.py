import streamlit as st
from pathlib import Path
import pandas as pd


def main():
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
    path_csv = path /'data/sales_data_sample.csv'
    df = pd.read_csv(path_csv,encoding = "ISO-8859-1")
    return df

def set_sessions():
    if 'sales_data' not in st.session_state:
        st.session_state['sales_data'] = load_data()
df = load_data()
st.write(df.head())

if __name__ == "__main__":
    set_sessions()
    main()
