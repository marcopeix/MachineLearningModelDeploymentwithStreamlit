import streamlit as st

# Set page configuration

# Initialize a sample df and store it in the session state

# Initialize state with the key "product" set to 0

# Define a function to multiply two numbers

if __name__ == "__main__":

    st.title("Homepage")

    col1, col2 = st.columns(2)

    with col1:
        x1 = st.number_input("Pick a number", 0, 10, key="x1")
    with col2:
        x2 = st.number_input("Pick another number", 0, 10, key="x2")

    st.button("Multiply!", type="primary")

st.write(st.session_state)
