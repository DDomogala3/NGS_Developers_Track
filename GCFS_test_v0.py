import streamlit as st
from pysam import bcftools
import os
from st_files_connection import FilesConnection
import gcsfs

fs = gcfs.GCSFileSystem(project="ddd-wgs")
fs.ls("ngsappbucket")
