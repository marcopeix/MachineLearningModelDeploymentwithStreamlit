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

multiselect = st.multiselect("Choose as many columns as you want", options=df.columns[1:], default=["col2"], max_selections=2)
st.write(multiselect)

# Slider
st.divider()

slider = st.slider("Pick a number", min_value=0.0, max_value=10.0, value=5.0, step=0.1)
st.write(slider)

# Text input
st.divider()

text_input = st.text_input("What's your name?", placeholder="John Doe")
st.write(f"Your name is {text_input}")

# Number input
st.divider()

num_input = st.number_input("Pick a number", min_value=0, max_value=10, value=0, step=1)
st.write(f"You picked {num_input}")

# Text area
st.divider()

txt_area = st.text_area("What do you want to tell me?", height=500, placeholder="Write your message here")
st.write(txt_area)