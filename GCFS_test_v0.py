import streamlit as st
from pysam import bcftools
import os
from st_files_connection import FilesConnection
import gcsfs

fs = gcsfs.GCSFileSystem(project="ddd-wgs")
contents = fs.ls("ngsappbucket")
st.write(contents)

with fs.open("ngsappbucket/uploaded_file", "rb") as bam_file:
  fs.read_bytes(bam_file)
