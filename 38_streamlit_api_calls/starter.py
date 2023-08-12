import streamlit as st
import pandas as pd
import requests


# Function to make a GET request


@st.cache_data(show_spinner="Searching...")
def search_gutenberg(author, title):
    # Define your base url

    # Replace whitespace with %20 as per the documentation
    # For the search parameters

    # Make a url from the search parameters

    # Make the final search url (combine base with params url)

    try:
        pass
        # Make a get request

        # Get the JSON response

        # If your JSON has no results, return False
        # Else, return the JSON reponse
    except:
        return False

# Function to format the JSON response as a DataFrame


@st.cache_data
def format_json_res(json_res):
    cols = ['Id', 'Author', 'Title', 'Language', 'Link']

    rows = []

    try:
        # For loop to access all data in the response

        df = pd.DataFrame(rows, columns=cols)

        return df
    except:
        st.error("Error while parsing data")


if __name__ == "__main__":
    st.title("📚 Search Project Gutenberg")
    with st.form("search-form"):
        col1, col2 = st.columns(2)

        with col1:
            author = st.text_input("Author")
        with col2:
            title = st.text_input("Title")

        search = st.form_submit_button("Search", type='primary')
