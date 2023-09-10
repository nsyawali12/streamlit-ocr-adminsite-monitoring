import pandas as pd
import streamlit as st
import base64


from hit_curl_form import perform_ocr
from converter_json_to_csv import convert_json


st.title("OCR MONITORING HARIAN v1")

model_name = st.selectbox("Select OCR Model", ["monitoring_harian_air_v1"])

# Image upload
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

# Perform OCR when the "Run OCR" button is clicked
if st.button("Do OCR"):
    if uploaded_file is not None:
        st.text("Performing OCR")
        # Display the uploaded image
        st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
        ocr_result = perform_ocr(model_name, uploaded_file)
        st.text("This the OCR Result")
        
        if ocr_result.get("status", False):
            csv_filename = "ocr_result.csv"
            
            # Call the CSV conversion function
            convert_json(ocr_result, csv_filename)
             # Provide a download link for the CSV file
            st.text("Here You can Download OCR Result as CSV on this link: ")
            # Create a download link for the CSV file
            csv_link = f'<a href="data:file/csv;base64,{base64.b64encode(open(csv_filename, "rb").read()).decode()}" download="{csv_filename}">Download {csv_filename}</a>'
            
            # Display the download link
            st.markdown(csv_link, unsafe_allow_html=True)
        else:
            st.text("OCR failed. Please check the uploaded image or try again.")
        
        st.text("Here are the JSON Result: ")
        st.json(ocr_result)
    else:
        st.text("Please upload an image first")
        
