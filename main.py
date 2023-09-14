import streamlit  as st
import pandas as pd

dataset = pd.read_csv("csc.csv")

st.dataframe(dataset)