import streamlit as st

if all (key not in st.session_state.keys() for key in ('username', 'pwd', 'pwd_correct', 'form_submitted')):
    st.session_state['username'] = ""
    st.session_state['pwd'] = ""
    st.session_state['pwd_correct'] = False
    st.session_state['form_submitted'] = False

# Check if login credentials are correct
def check_login():
    pass

# Function to display the login form
def display_login_form():
    pass

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
