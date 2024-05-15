import streamlit as st
from pysam import bcftools
import os
from st_files_connection import FilesConnection
import pandas as pd
import gcsfs
conn = st.connection('gcs',type = FilesConnection)
#COSMIC = conn.read("ngsappbucket/Galaxy73-[Cosmic_GenomeScreensMutant_v99_GRCh37.vcf.gz].vcf_bgzip",input_format="txt",ttl=600)
#conn = st.connection('gcs',type = FilesConnection)
COSMIC = conn.open("ngsappbucket/Galaxy73-[Cosmic_GenomeScreensMutant_v99_GRCh37.vcf.gz].vcf_bgzip",mode = "rb")
COSMIC_Index = conn.open("ngsappbucket/Galaxy73-[Cosmic_GenomeScreensMutant_v99_GRCh37.vcf.gz].tbi",mode = "rb")
#TEST_FS = conn.fs()
#TEST_READ = conn.read("ngsappbucket/bio_info_data_set.csv", input_format="csv", ttl = 600)
TEST_READ = conn.open("ngsappbucket/bio_info_data_set.csv", mode = "rb")
st.write(TEST_READ)
#path_file = os.path.dirname("/Users/danieldomogala/Documents/Personal/Codeacademy_notebooks/")
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
        fs = gcsfs.GCSFileSystem(project='ddd-wgs')
    with fs.open("ngsappbucket/output.vcf","wb") as f:
        for i in vcf:
            f.write(i)
     
    st.download_button(
    label="Download vcf",
    data = vcf,
    file_name=output,
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
    fs = gcsfs.GCSFileSystem(project='ddd-wgs')
    with fs.open("ngsappbucket/uploaded_file","wb") as f:
        for i in uploaded_file:
            f.write(i)
    target = fs.url("Downloads/") + uploaded_file.name
    
    #fs.put_file(target,"ngsappbucket/")
    fs.du("ngsappbucket/uploaded_file")
    #region = '11:524657,5246555'
    #Pyview = pysam.view(uploaded_file.name,region)
    #print(Pyview)
    #st.write(Pyview)
    output = st.text_input("Please name your output vcf file: ")

    generate_vcf(uploaded_file.name,output)

