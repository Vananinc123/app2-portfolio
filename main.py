import streamlit as st

st.set_page_config(layout="wide")


col1, col2 = st.columns(2)
import pandas

with col1:
    st.image("images/IMG_2044.png")

with col2:
    st.title("Saravanan Nagaraj")
    content = """
    Hi, I'm Saravanan Nagaraj a Python programmer, business owner and a teacher. I'm from India and moved to the 
    United States. now i'm learning and creating web application using Python program"""

    st.info(content)

content2= """
    Below you can find some of the apps I have built in Python. Feel free to contact me!
    """
st.write(content2)

col3, col4 = st.columns(2)

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])







