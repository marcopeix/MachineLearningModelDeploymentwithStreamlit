import streamlit as st

if all (key not in st.session_state.keys() for key in ('username', 'pwd', 'pwd_correct', 'form_submitted')):
    st.session_state['username'] = ""
    st.session_state['pwd'] = ""
    st.session_state['pwd_correct'] = False
    st.session_state['form_submitted'] = False

def check_login():
    st.session_state['form_submitted'] = True

    if (
        st.session_state["username"] in st.secrets["passwords"]
        and 
        st.session_state["pwd"] == st.secrets["passwords"][st.session_state["username"]]
    ):
        st.session_state['pwd_correct'] = True
        st.session_state['pwd'] = ""
        st.session_state['username'] = ""
    else:
        st.session_state['pwd_correct'] = False

def display_login_form():
    with st.form("login_form"):
        st.text_input("Username", key="username")
        st.text_input("Password", type="password", key="pwd")

        st.form_submit_button("Login", on_click=check_login)

if (st.session_state['pwd_correct'] == False and st.session_state['form_submitted'] == False):
    display_login_form()
elif (st.session_state['pwd_correct'] == False and st.session_state["form_submitted"] == True):
    display_login_form()
    st.error("Invalid user/password")
elif (st.session_state['pwd_correct'] == True and st.session_state["form_submitted"] == True):
    st.write("User logged in")
else:
    display_login_form()

st.write(st.session_state)
