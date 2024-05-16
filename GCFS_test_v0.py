import streamlit as st
from pysam import bcftools
import os
from st_files_connection import FilesConnection
import gcsfs

fs = gcsfs.GCSFileSystem(project="ddd-wgs")
contents = fs.ls("ngsappbucket")
st.write(contents)

conn = st.connection('gcs', type=FilesConnection)
