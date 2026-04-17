import streamlit as st
import pandas as pd
from data_cleaning import DataCleaning
from ai_module import ask_ai

st.set_page_config(page_title="AI Data Cleaning App", layout="wide")

st.title("🤖 AI-Powered Data Cleaning App")

st.write("Upload your CSV or Excel file → Clean → Get AI Suggestions → Download")

uploaded_file = st.file_uploader("Upload File", type=["csv", "xlsx"])

cleaner = DataCleaning()

if uploaded_file is not None:

    # =========================
    # Load File
    # =========================
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    st.subheader("📊 Original Data")
    st.dataframe(df)

    st.write("🔢 Original Shape:", df.shape)

    # =========================
    # Clean Data
    # =========================
    df_clean = cleaner.clean_data(df.copy())

    st.subheader("✅ Cleaned Data")
    st.dataframe(df_clean)

    st.write("🔢 Cleaned Shape:", df_clean.shape)

    # =========================
    # AI Suggestions
    # =========================
    prompt = f"""
    You are a data analyst.
    Suggest data cleaning and preprocessing steps for this dataset:

    Columns: {df_clean.columns.tolist()}

    Sample Data:
    {df_clean.head(10).to_string()}
    """

    ai_output = ask_ai(prompt)

    st.subheader("🤖 AI Suggestions")
    st.write(ai_output)

    # =========================
    # Download Cleaned Data
    # =========================
    csv = df_clean.to_csv(index=False).encode('utf-8')

    st.download_button(
        label="⬇️ Download Cleaned CSV",
        data=csv,
        file_name="cleaned_data.csv",
        mime="text/csv"
    )