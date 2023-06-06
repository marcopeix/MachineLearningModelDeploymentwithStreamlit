import streamlit as st
import pandas as pd


# Buttons
primary_btn = st.button(label="Primary", type="primary")
secondary_btn = st.button(label="Secondary", type="secondary")

if primary_btn:
    st.write("Hello from primary")

if secondary_btn:
    st.write("Hello from secondary")

# Checkbox
st.divider()

checkbox = st.checkbox("Remember me")

if checkbox:
    st.write("I will remember you")
else:
    st.write("I will forget you")

# Radio buttons
st.divider()

df = pd.read_csv("data/sample.csv")

radio = st.radio("Choose a column", options=df.columns[1:], index=1, horizontal=True)
st.write(radio)

# Selectbox
st.divider()

select = st.selectbox("Choose a column", options=df.columns[1:], index=0)
st.write(select)

# Mutliselect
st.divider()


# Slider
st.divider()


# Text input
st.divider()


# Number input
st.divider()


# Text area
st.divider()
