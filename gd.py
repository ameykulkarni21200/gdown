import streamlit as st
import gdown
import pandas as pd
from docx import Document
import pickle



# Function to download and display file
def download_and_display_file(file_url):
    # Download the file using gdown
    output = 'PF Form11 - New Format.docx'  # Change the file name and extension as needed
    gdown.download(file_url, output, quiet=False)

    doc = Document(output)
    content = []
    for para in doc.paragraphs:
          content.append(para.text)
    st.write("\n".join(content))

# Streamlit UI
st.title("Google Drive File Access with gdown")

# Input for Google Drive file URL
file_url = 'https://docs.google.com/document/d/1BesDWSNjNHeF9pjYGgki92cFDyvoR3Bl/edit?usp=drive_link&ouid=114939215147549650885&rtpof=true&sd=true'

if st.button("Download and Display"):
    if file_url:
        download_and_display_file(file_url)
    else:
        st.error("Please enter a valid Google Drive file URL.")
