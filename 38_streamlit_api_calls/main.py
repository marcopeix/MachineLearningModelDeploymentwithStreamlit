import streamlit as st
import pandas as pd
import requests


@st.cache_data(show_spinner="Searching...")
def search_gutenberg(author, title):
    BASE_URL = "https://gutendex.com/books?search="
    author = author.replace(" ", "%20")
    title = title.replace(" ", "%20")

    params_url = f"{author}%20{title}"

    search_url = f"{BASE_URL}{params_url}"

    try:
        res = requests.get(search_url)

        json_res = res.json()

        if json_res["count"] == 0:
            return False
        else:
            return json_res
    except:
        return False


@st.cache_data
def format_json_res(json_res):
    cols = ['Id', 'Author', 'Title', 'Language', 'Link']

    rows = []

    try:
        for result in json_res["results"]:

            id = result["id"]
            author = result["authors"][0]["name"]
            title = result["title"]
            language = result["languages"][0]
            link = f"https://www.gutenberg.org/ebooks/{id}"

            rows.append([id, author, title, language, link])

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

    if search:
        json_res = search_gutenberg(author, title)

        if json_res:
            df = format_json_res(json_res)
            st.subheader("Results")
            st.table(df)
        else:
            st.error("No results found")
