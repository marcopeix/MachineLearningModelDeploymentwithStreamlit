import streamlit as st
import pandas as pd
from sklearn.metrics import f1_score
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.dummy import DummyClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
from sklearn.feature_selection import SelectKBest, mutual_info_classif

# Set page config:
# The title is "Experiment"
# Choose an icon for the page
# The layout is centered
# The sidebar is set to "auto"

# Write a function to load the wine dataset from sklearn
# Should you cache it?

# Run the function to load the data

# Write a function for train/test split.
# Use stratification, and keep 30% of the data for the test set
# Should you cache it?

# Run your train/test split function

# Write a function to select features using SelectKbest and mutual_info_classif
# Should you cache it?

# Write a function that fits the selected model and computes the F1-score
# The function must return the F1-Score
# Inside this function, you must run feature selection
# Should you cache it?

# Write a callback function that runs the model fitting and scoring function
# The callback appends the model, number of features, and score to the state.
# The callback takes 2 arguments: the model and the number of features to keep

if __name__ == "__main__":
    
    with st.container():
        st.title("🧪 Experiments")

    col1, col2 = st.columns(2)

    with col1:
        model = st.selectbox("Choose a model", ["Baseline", "Decision Tree", "Random Forest", "Gradient Boosted Classifier"])
    with col2:
        k = st.number_input("Choose the number of features to keep", 1, 13)

    # Plug in your callback and define the arguments
    st.button("Train", type="primary")

    # Display the full dataset inside an expander

    if len(st.session_state['score']) != 0:
        st.subheader(f"The model has an F1-Score of: {st.session_state['score'][-1]}")
        




