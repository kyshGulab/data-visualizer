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


#api_key = "sk-proj-fB8SWqk8dMxXjRwzGdFQT3BlbkFJjt2Zd2yenJe3GMzNFnqH"
#openai.api_key = api_key

question = st.text_area("How do you want to see your data")

#response = client.completions.create(
    #model="davinci-002",  # Use the model of your choice
    #prompt= "generate a data visual to answer:, {}".format(question) ,
    #max_tokens=100
#)

#answer = response.choices[0].text.strip()
#st.write(answer)



if question:
  # Construct the prompt including selected columns and user's question
  prompt = f"use seaborn to generate python code to create a visualization to answer: '{question}', generate raw code, not instructions. use the column names based on columns: {', '.join(selected_columns)}"
  
  # Pass the prompt to the GPT model to generate code for data visualization
  response = client.completions.create(
      model="davinci-002",
      prompt=prompt,
      max_tokens=100
  )
  answer = response.choices[0].text.strip()

  st.write(answer)
