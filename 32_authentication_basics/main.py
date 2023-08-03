import streamlit as st

if all (key not in st.session_state.keys() for key in ('pwd', 'pwd_correct', 'form_submitted')):
    st.session_state['pwd'] = ""
    st.session_state['pwd_correct'] = False
    st.session_state['form_submitted'] = False

def check_password():
    st.session_state['form_submitted'] = True

    if st.session_state['pwd'] == st.secrets['password']:
        st.session_state['pwd_correct'] = True
        st.session_state['pwd'] = ""
    else:
        st.session_state['pwd_correct'] = False

def display_login_form():
    with st.form("login_form"):
        st.text_input("Password", type="password", key="pwd")

        st.form_submit_button("Login", on_click=check_password)

if (st.session_state['pwd_correct'] == False and st.session_state['form_submitted'] == False):
    display_login_form()
elif (st.session_state['pwd_correct'] == False and st.session_state["form_submitted"] == True):
    display_login_form()
    st.error("Invalid password")
elif (st.session_state['pwd_correct'] == True and st.session_state["form_submitted"] == True):
    st.write("User logged in")
else:
    display_login_form()

st.write(st.session_state)

