from pathlib import Path
import streamlit as st
import pandas as pd
from src.data_processing import load_data
from src.utils import project_info

# Page config
st.set_page_config(page_title="Weekend Data Explorer", layout="wide", page_icon="📊")

# Sidebar
st.sidebar.image("assets/logo.png") if Path("assets/logo.png").exists() else None
st.sidebar.title("Project")
st.sidebar.markdown(project_info())
st.sidebar.markdown("---")
st.sidebar.markdown("**Tips:** Upload CSV or JSON. Use the slider to change preview rows.")

# Title
st.title("📊 Weekend Data Explorer")

# File uploader
uploaded_file = st.file_uploader("Upload CSV or JSON", type=["csv", "json"])

if uploaded_file is not None:
    try:
        df = load_data(uploaded_file)
    except Exception as e:
        st.error(f"Error loading file: {e}")
        st.stop()

    st.success(f"Loaded `{uploaded_file.name}` — Rows: {df.shape[0]}, Columns: {df.shape[1]}")

    # Overview
    st.subheader("Dataset overview")
    col1, col2, col3 = st.columns([1,1,1])
    with col1:
        st.write("**Shape**")
        st.write(f"{df.shape[0]} rows × {df.shape[1]} columns")
    with col2:
        st.write("**Columns**")
        st.write(df.columns.tolist())
    with col3:
        st.write("**Missing values**")
        st.write(df.isnull().sum().to_dict())

    # Interactive options
    st.subheader("Preview & interactive")
    rows = st.slider("Rows to preview", min_value=5, max_value=100, value=10, step=5)
    cols = st.multiselect("Columns to view (empty = all)", options=list(df.columns))
    if cols:
        st.dataframe(df[cols].head(rows))
    else:
        st.dataframe(df.head(rows))

    if st.checkbox("Show dtypes"):
        st.write(pd.DataFrame(df.dtypes, columns=["dtype"]))

    if st.checkbox("Show summary (numeric)"):
        st.write(df.describe())

    # Download processed csv
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button("Download CSV", data=csv, file_name="processed_data.csv", mime="text/csv")

else:
    st.info("Upload a CSV or JSON file to begin. You can use the sample `data/raw/sample.csv` if you don't have one.")

# Custom CSS (bonus)
st.markdown(
    """
    <style>
    .stApp { background-color: #f7f9fc; }
    .css-1v3fvcr { max-width: 1200px; }  /* Streamlit layout tweak (may vary by version) */
    h1 { color: #0b6efd; }
    </style>
    """, unsafe_allow_html=True
)
