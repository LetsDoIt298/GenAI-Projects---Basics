from urllib import response
from dotenv import load_dotenv
load_dotenv() #Loads all envirnment variables

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

#Function to load gemini model and get responses
model =  genai.GenerativeModel('gemini-pro')
def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text

#Setting streamlit app
st.set_page_config(page_title="QA Demo")
st.header("Gemini LLM Aplication")

input = st.text_input("Input: ",key='input')
submit = st.button("Ask the question")

#When submit
if submit:
    response = get_gemini_response(input)
    st.subheader("The response is:- ")
    st.write(response)
    