import streamlit as st
import pandas as pd

st.title("CSV File Upload and DataFrame Display")

uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file is not None:
  df = pd.read_csv(uploaded_file)
  column_names = df.columns.tolist()
  selected_columns = st.multiselect("Select columns to display", column_names)
  if selected_columns:
    df_selected = df[selected_columns]
    st.write("Selected DataFrame:")
    st.write(df_selected)