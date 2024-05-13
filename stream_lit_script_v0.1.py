import streamlit as st
import pysam
st.write("This is the first streamlit app.")
st.write("Please answer quiz question 1")
st.user_info = "DDD"
st.text_input("What is soft clipping an alignment file?: " )
uploaded_file = st.file_uploader("Please upload BAM file: ")
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    st.write(bytes_data)
    region = '11:524657,5246555'
    Pyview = pysam.view(uploaded_file,region)
    st.write(Pyview)
