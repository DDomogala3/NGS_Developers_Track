import streamlit as st
from pysam import bcftools
st.write("This is the first streamlit app.")
st.write("Please answer quiz question 1")
st.user_info = "DDD"
st.text_input("What is soft clipping an alignment file?: " )
uploaded_file = st.file_uploader("Please upload BCF file: ")
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    st.write(bytes_data)

    #region = '11:524657,5246555'
    #Pyview = pysam.view(uploaded_file.name,region)
    #print(Pyview)
    #st.write(Pyview)

    with open("Galaxy117-[HBB_Gene]_streamlit.vcf","w") as f:
        HBB_vcf = bcftools.call(uploaded_file.name,"-o", "Galaxy117-[HBB_Gene].vcf", "-c")
        st.write(HBB_vcf)
        f.write(HBB_vcf)
