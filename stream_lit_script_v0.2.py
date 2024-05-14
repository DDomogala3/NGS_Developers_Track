import streamlit as st
from pysam import bcftools
import os
path_file = os.path.dirname("/Users/danieldomogala/Documents/Personal/Codeacademy_notebooks/")
st.header("NGS Developer's APP FINAL PROJECT 2024")
st.subheader("Developed by Dan Domogala and Allison Bellman")
st.write("Please answer quiz question 1")
st.user_info = "DDD"
st.text_input("What is soft clipping an alignment file?: " )
st.header("Variant Calling Pipelining APP")
st.markdown( "**Step 1)** Please both upload your BAM, BCF (pileup), or VCF file to the **class github repo** (https://github.com/DDomogala3/NGS_Developers_Track/) and upload the file and press the download button." )
st.markdown( "**Step 2)** Download output to your computer after analysis  finishes.")


def generate_vcf(input,output):
    with open(output,"w") as f:
        vcf = bcftools.call(input,"-o", output, "-c")
        st.write(vcf)
        f.write(vcf)
     
    st.download_button(
    label="Download vcf",
    data = vcf,
    file_name="output",
    mime="vcf",)
    return vcf

# Go from BCF (pileup to Variant Calling Format (VCF) 
st.markdown("Upload :red[BCF] to :green[VCF]")
uploaded_file = st.file_uploader("Please upload BCF file: ")
#uploaded_file = .join uploaded_file
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    st.write(bytes_data)

    #region = '11:524657,5246555'
    #Pyview = pysam.view(uploaded_file.name,region)
    #print(Pyview)
    #st.write(Pyview)
    output = st.text_input("Please name your output vcf file: ")
#def generate_vcf(input,output):
#    with open("output","w") as f:
#        vcf = bcftools.call(uploaded_file.name,"-o", "input", "-c")
 #       st.write(vcf)
 #       f.write(vcf)
    generate_vcf(uploaded_file.name,output)
 #   st.download_button(
  #  label="Download vcf",
   # data = vcf,
   ## file_name="output",
    #mime="vcf",)
#generate_vcf(uploaded_file.name,output)
