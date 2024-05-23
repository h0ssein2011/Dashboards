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



if __name__ == "__main__":
    main()
