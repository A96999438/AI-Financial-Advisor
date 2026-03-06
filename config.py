import streamlit as st
import google.generativeai as genai

# Get API key from Streamlit secrets
api_key = st.secrets["GEMINI_API_KEY"]

# Configure Gemini
genai.configure(api_key=api_key)

# Create Gemini model
model = genai.GenerativeModel("gemini-pro")
