import streamlit as st
import pandas as pd

# Load data from Jupyter Notebook
df = pd.read_csv("Dataset.csv")

st.title("group2 project 3")
st.write(df)
