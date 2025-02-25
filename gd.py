import streamlit as st
import gdown
import pandas as pd
from docx import Document
import pickle



# Function to download and display file
def download_and_display_file(file_url):
    # Download the file using gdown
    output = 'fantasy_score_model.pkl'  # Change the file name and extension as needed
    gdown.download(file_url, output, quiet=False)

    with open(output, 'rb') as file:
            data = pickle.load(file)
    st.write(data)

# Streamlit UI
st.title("Google Drive File Access with gdown")

# Input for Google Drive file URL
file_url = 'https://drive.google.com/uc?id=https://drive.google.com/file/d/1D1kPHNLC1MpVirOp-jhU3ViXkDJVUS_N/view?usp=drive_link'

if st.button("Download and Display"):
    if file_url:
        download_and_display_file(file_url)
    else:
        st.error("Please enter a valid Google Drive file URL.")
