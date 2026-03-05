import os
from dotenv import load_dotenv
import google.generativeai as genai
import streamlit as st

load_dotenv()

api_key = st.secrets["GEMINI_API_KEY"]

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-1.5-flash-latest")