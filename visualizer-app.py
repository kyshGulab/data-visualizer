import streamlit as st
import pandas as pd
import openai
from openai import OpenAI


api_keyy = st.secrets["openai_secret"]
client = OpenAI(api_key = api_keyy)


st.title("Data Visualizer App")

uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file is not None:
  df = pd.read_csv(uploaded_file)
  column_names = df.columns.tolist()
  selected_columns = st.multiselect("Select columns to display", column_names)
  if selected_columns:
    df_selected = df[selected_columns]
    st.write("Selected DataFrame:")
    st.write(df_selected)


question = st.text_area("How do you want to see your data")




if question:
  # Construct the prompt including selected columns and user's question
  prompt = f"use python to Generate code to construct a data visual to answer '{question}' based on the following columns: {', '.join(selected_columns)}. Only provide the code and nothing else"  
  # Pass the prompt to the GPT model to generate code for data visualization davinci-002
  response = client.chat.completions.create( messages = [ {"role" : "user", "content" : prompt, }], model = "gpt-3.5-turbo", )
  
  answer = response.choices[0].message.content

  st.write(answer)
