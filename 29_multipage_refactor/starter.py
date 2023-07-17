import streamlit as st

st.set_page_config(
    page_title="Homepage",
    page_icon="🏡",
    layout="centered",
    initial_sidebar_state="expanded"
)

if "product" not in st.session_state:
    st.session_state['product'] = 0


def multiply(x1, x2):
    st.session_state["product"] = x1 * x2

# Workaround from: https://stackoverflow.com/questions/74968179/session-state-is-reset-in-streamlit-multipage-app

# Function to keep a value (copy from temporary to permanent)

# Function to reassign value to temporary key (copy from permanent to temporary)


if __name__ == "__main__":

    st.title("Homepage")

    col1, col2 = st.columns(2)

    with col1:
        x1 = st.number_input("Pick a number", 0, 10, key="x1")
    with col2:
        x2 = st.number_input("Pick another number", 0, 10, key='x2')

    st.button("Multiply!", type="primary", on_click=multiply, args=((x1, x2)))

st.write(st.session_state)
