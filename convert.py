import requests
import io
from PIL import Image
from processor import upload_file
import streamlit as st


def generate_image(book_title):

    API_URL = "https://api-inference.huggingface.co/models/runwayml/stable-diffusion-v1-5"
    headers = {"Authorization": F"Bearer {st.secrets.API_KEY}"}

    payload = {
        "inputs": f"Generate a children book cover for a book titled: {book_title}",
    }
    
    response = requests.post(API_URL, headers=headers, json=payload)
    image_bytes = response.content
    
    fd = io.BytesIO(image_bytes)

    link = upload_file(fd)
    return link



def generate_poem(title):
    API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2"
    headers = {"Authorization": F"Bearer {st.secrets.API_KEY}"}

    payload = {
        "inputs": f"Generate a sonnet poem for kids with the title: {title}",
    }
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()[0]['generated_text']