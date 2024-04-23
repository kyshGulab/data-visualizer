import streamlit as st
import pandas as pd
import openai
from openai import OpenAI
import matplotlib


def generate_visualization():
    api_key = st.secrets["openai_secret"]
    client = OpenAI(api_key=api_key)

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
                prompt = f"The user will upload a dataset to streamlit and call it df, use python to Generate code to construct a data visual to answer '{question}' based on the following columns: {', '.join(selected_columns)} in df. Do not create sample data in your output. Do not provide steps, just provide the code to answer the question."  
                # Pass the prompt to the GPT model to generate code for data visualization davinci-002
                response = client.chat.completions.create(
                    messages=[{"role": "user", "content": prompt}],
                    model="gpt-3.5-turbo"
                )
                
                answer = response.choices[0].message.content
                
                st.write(answer)

generate_visualization()
