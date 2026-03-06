import streamlit as st
import google.generativeai as genai

# Get API key from Streamlit secrets
api_key = st.secrets["GEMINI_API_KEY"]

genai.configure(api_key=api_key)

# Use stable Gemini model
model = genai.GenerativeModel("gemini-pro")
