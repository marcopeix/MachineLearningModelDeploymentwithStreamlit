import streamlit as st
import pandas as pd
from sklearn.metrics import f1_score
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.dummy import DummyClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
from sklearn.feature_selection import SelectKBest, mutual_info_classif

st.set_page_config(
    page_title="Experiment",
    page_icon="🧪",
    layout="centered",
    initial_sidebar_state="auto"
)

@st.cache_data(show_spinner="Loading data...")
def load_data():
    wine_data = load_wine()
    wine_df = pd.DataFrame(data=wine_data.data, columns=wine_data.feature_names)

    wine_df['target'] = wine_data.target

    return wine_df

wine_df = load_data()

@st.cache_data
def split_data(df):

    X = df.drop(['target'], axis=1)
    y = df['target']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, shuffle=True, stratify=y, random_state=42)

    return X_train, X_test, y_train, y_test

X_train, X_test, y_train, y_test = split_data(wine_df)

@st.cache_data()
def select_features(X_train, y_train, X_test, k):
    selector = SelectKBest(mutual_info_classif, k=k)
    selector.fit(X_train, y_train)

    sel_X_train = selector.transform(X_train)
    sel_X_test = selector.transform(X_test)

    return sel_X_train, sel_X_test

@st.cache_data(show_spinner="Training and evaluating model")
def fit_and_score(model, k):
    
    if model == "Baseline":
        clf = DummyClassifier(strategy="stratified", random_state=42)
    elif model == "Decision Tree":
        clf = DecisionTreeClassifier(random_state=42)
    elif model == "Random Forest":
        clf = RandomForestClassifier(random_state=42)
    else:
        clf = GradientBoostingClassifier(random_state=42)
    
    sel_X_train, sel_X_test = select_features(X_train, y_train, X_test, k)

    clf.fit(sel_X_train, y_train)

    preds = clf.predict(sel_X_test)

    score = round(f1_score(y_test, preds, average='weighted'),3)

    return score
    
def save_performance(model, k):

    score = fit_and_score(model, k)

    st.session_state['model'].append(model)
    st.session_state['num_features'].append(k)
    st.session_state['score'].append(score)


if __name__ == "__main__":
    
    with st.container():
        st.title("🧪 Experiments")

    col1, col2 = st.columns(2)

    with col1:
        model = st.selectbox("Choose a model", ["Baseline", "Decision Tree", "Random Forest", "Gradient Boosted Classifier"])
    with col2:
        k = st.number_input("Choose the number of features to keep", 1, 13)

    st.button("Train", type="primary", on_click=save_performance, args=((model, k)))

    with st.expander("See full dataset"):
        st.write(wine_df)

    if len(st.session_state['score']) != 0:
        st.subheader(f"The model has an F1-Score of: {st.session_state['score'][-1]}")
        




