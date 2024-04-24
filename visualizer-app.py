import streamlit as st
import pandas as pd
import openai
from openai import OpenAI
import seaborn as sns
import matplotlib.pyplot as plt


def generate_visualization():
    api_key = st.secrets["openai_secret"]
    client = OpenAI(api_key=api_key)

    st.set_page_config( 
    page_icon=":bar_chart:",
    layout="wide",  
    initial_sidebar_state="expanded")


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
            question = st.text_area("Do you want to see suggested ways to analyze your data?")

            if question:
                
                prompt = f"The user has selected columns: {', '.join(selected_columns)}. Based on these columns, generate Python code to suggest suitable visualizations using a visualization library (e.g., Matplotlib, Seaborn). for each individual visual, include a paragraph about what insights the visual will help the user gain. Suggest at least five different visuals when possible. Assume the dataset is already loaded."

                # Construct the prompt including selected columns and user's question
                #prompt = f"The user has asked: {question} Based on the uploaded dataset, generate Python code to visualize the aswer using suitable visualization technique using seaborn. Please only provide the code for the visualization and exclude any additional code or comments. assume the dataset is already loaded. only provide code for the visualization"
                 
                # Pass the prompt to the GPT model to generate code for data visualization davinci-002
                response = client.chat.completions.create(
                    messages=[{"role": "user", "content": prompt}],
                    model="gpt-3.5-turbo"
                )
                
                answer = response.choices[0].message.content
                
                st.subheader("Suggested Visualizations:")
                st.code(answer, language="python")
            

generate_visualization()

