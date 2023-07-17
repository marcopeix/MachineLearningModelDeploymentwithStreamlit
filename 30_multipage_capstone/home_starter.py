import streamlit as st
import pandas as pd

# Set page config:
# The title is "Homepage"
# Choose an icon for the page
# The layout is centered
# The sidebar is set to "auto"

# Initialize the state with the keys: [model, num_features, score]
# This is where we store the info to display the ranking

# Write a function to display a DataFrame ranked in descending order of F1-Score
# The DataFrame has 3 columns: Model, Number of Features, F1-Score

if __name__ == "__main__":
    st.title("🏆 Model ranking")

    if len(st.session_state['model']) == 0:
        st.subheader("Train a model in the next page to see the results 👉")
    else:
        # Function that display the DataFrame runs here
        pass
    
    st.write(st.session_state)