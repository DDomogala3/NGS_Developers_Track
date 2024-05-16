import streamlit as st
from pysam import bcftools
import os
from st_files_connection import FilesConnection
import gcsfs

fs = gcsfs.GCSFileSystem(project="ddd-wgs")
contents = fs.ls("ngsappbucket")
st.write(contents)

with fs.read_bytes("ngsappbucket/uploaded_file") as bam_file:
  st.write(bam_file)
