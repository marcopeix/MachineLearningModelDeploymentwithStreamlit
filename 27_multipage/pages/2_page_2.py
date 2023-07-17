import streamlit as st

st.title("Second page")

st.write(st.session_state['df'])

product = st.session_state["product"]

st.subheader(f"The product is {product}🎉")

st.write(st.session_state)
