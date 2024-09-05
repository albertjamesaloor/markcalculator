import streamlit as st
from PIL import Image

img = Image.open('logo.jpg')

st.set_page_config(page_title="Marks Calculator", page_icon=img)
