import streamlit as st
import pandas as pd

# Load data from Jupyter Notebook
df = pd.read_csv("Dataset.csv")

st.title("My Streamlit App")
st.write(df)
