import streamlit as st
from utils.data_manager import set_sessions
from pathlib import Path
from PIL import Image


st.set_page_config(layout="wide")
path = Path(__file__).parent
image = Image.open(path  / 'image/logo.png')#.resize((700,200))
width , height = image.size
new_size = (int(width*0.6),int(height*0.6))
image = image.resize(new_size)
st.image(image)
def main():
    markdown_content = """
        ### This interactive dashboard presents the comprehensive analysis based on the sample dataset.
        #### There are 3 pages:
        1. **Business Analysis**
                - This section presents an overivew of  the overall business performance,
        2. **Brand Analysis**
                - Explore performance data for each of the three brands on a daily, weekly, and monthly basis.
        3. **User Analysis**
                - Analyze user performance metrics segmented by daily, weekly, and monthly intervals.

        You can see all codes developed with Python in my [Github link](https://github.com/h0ssein2011/Dashboards/tree/main/VenturesLab):


        """
    st.markdown(markdown_content , unsafe_allow_html=True)


if __name__ == "__main__":
    set_sessions()
    main()
