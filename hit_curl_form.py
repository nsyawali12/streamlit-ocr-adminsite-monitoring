import requests
import os

def perform_ocr(model, image_filename):
    api_url = "https://stg-ocrdocs.api.efishery.com/azure_ocr"

    # Prepare the payload 
    data = {
        "model_name": model
    }

    files = {
        "image" : image_filename
    }

    response = requests.post(api_url, data=data, files=files)

    # Check the response
    if response.status_code == 200:
        ocr_result = response.json()
        return ocr_result
    else:
        return f"Error: {response.status_code} - {response.text}"
    


