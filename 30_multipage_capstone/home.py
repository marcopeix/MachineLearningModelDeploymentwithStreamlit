import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Homepage",
    page_icon="🏡",
    layout="centered",
    initial_sidebar_state="auto"
)

if all(key not in st.session_state.keys() for key in ('model', 'num_features', 'score')):
    st.session_state['model'] = []
    st.session_state['num_features'] = []
    st.session_state['score'] = []

def display_df():
    df = pd.DataFrame({"Model": st.session_state['model'],
                       "Number of features": st.session_state['num_features'],
                       "F1-Score": st.session_state['score']})
    
    sorted_df = df.sort_values(by=['F1-Score'], ascending=False).reset_index(drop=True)

    st.write(sorted_df)

if __name__ == "__main__":
    st.title("🏆 Model ranking")

    if len(st.session_state['model']) == 0:
        st.subheader("Train a model in the next page to see the results 👉")
    else:
        display_df()

    st.write(st.session_state)