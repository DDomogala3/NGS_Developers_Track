import streamlit as st

st.write("This is the first streamlit app.")
st.write("Please answer quiz question 1")
st.user_info = "DDD"
st.text_input("What is soft clipping an alignment file?: " )
data = st.uploader("Please upload BAM file: ")
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    st.write(bytes_data)
