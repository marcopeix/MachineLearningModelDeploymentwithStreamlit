import streamlit as st
import pandas as pd

df = pd.read_csv("data/sample.csv", dtype="int")

st.dataframe(df)
st.write(df)

st.table(df)

st.metric(label="Expenses", value=900, delta=20, delta_color="inverse")