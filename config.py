import streamlit as st
import google.generativeai as genai

# Get API key from Streamlit Cloud secrets
api_key = st.secrets["GEMINI_API_KEY"]

# Configure Gemini
genai.configure(api_key=api_key)

# Use a supported Gemini model
model = genai.GenerativeModel("gemini-1.5-flash-latest")
