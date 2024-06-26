import streamlit as st
from pysam import bcftools
import os
from st_files_connection import FilesConnection
import pandas as pd
import gcsfs
from random import choice
from pysam import VariantFile
number = choice(range(0,10000000000))
#conn = st.connection('gcs',type = FilesConnection)
#COSMIC = conn.read("ngsappbucket/Galaxy73-[Cosmic_GenomeScreensMutant_v99_GRCh37.vcf.gz].vcf_bgzip",input_format="txt",ttl=600)
#conn = st.connection('gcs',type = FilesConnection)
#COSMIC = conn.open("ngsappbucket/Galaxy73-[Cosmic_GenomeScreensMutant_v99_GRCh37.vcf.gz].vcf_bgzip",mode = "rb")
#COSMIC_Index = conn.open("ngsappbucket/Galaxy73-[Cosmic_GenomeScreensMutant_v99_GRCh37.vcf.gz].tbi",mode = "rb")
#TEST_FS = conn.fs()
#TEST_READ = conn.read("ngsappbucket/bio_info_data_set.csv", input_format="csv", ttl = 600)
#TEST_READ = conn.open("ngsappbucket/bio_info_data_set.csv", mode = "rb")
#st.write(TEST_READ)
#path_file = os.path.dirname("/Users/danieldomogala/Documents/Personal/Codeacademy_notebooks/")
st.header("NGS Developer's APP FINAL PROJECT 2024")
st.subheader("Developed by Dan Domogala and Allison Bellman")
st.write("Please answer quiz question 1")
st.user_info = "DDD"
st.text_input("What is soft clipping an alignment file?: " )
st.header("Variant Calling Pipelining APP")
st.markdown( "**Step 1)** Please both upload your BAM, BCF (pileup), or VCF file to the **class github repo** (https://github.com/DDomogala3/NGS_Developers_Track/) and upload the file and press the download button." )
st.markdown( "**Step 2)** Download output to your computer after analysis  finishes.")


def generate_vcf(input,output_vcf):
   
   # with open(output_vcf,"w") as f:
   
   st.write(bcftools.call(input,"-o", output_vcf, "-c"))
   vcf = bcftools.call(input,"-o", output_vcf, "-c")
   
    
def cloud_pipeline_vcf(input):
    file_type = str()
    path = "ngsappbucket/output_vcf"
    with fs.open(path,"wb") as f:
        for i in input:
            f.write(i)
    
# Go from BCF (pileup to Variant Calling Format (VCF) 
st.markdown("Upload :red[BCF] to :green[VCF]")
uploaded_file = st.file_uploader("Please upload BCF file: ")

#uploaded_file = .join uploaded_file
if uploaded_file is not None:
   output = st.text_input("Please name your output vcf file: ")
 #  generate_vcf(uploaded_file.name,output)
    # To read file as bytes:
   bytes_data = uploaded_file.getvalue()
   st.write(bytes_data)
    
   fs = gcsfs.GCSFileSystem(project='ddd-wgs')
   with fs.open("ngsappbucket/uploaded_file","wb") as f:
      for i in uploaded_file:
         f.write(i)
         st.write(i)
         #generate_vcf(f,output)
            #f.close()
    #output = st.text_input("Please name your output vcf file: ", key = number)    


    
    
   fs.du("ngsappbucket/uploaded_file")

   with fs.open("ngsappbucket/output_vcf","r") as f:
      st.download_button(
         label="Download vcf",
         data = f,
         file_name=output,
         mime="vcf",)
  
   
        



