import streamlit as st

# Initialize state to:
# Store the password
# Check if the password is correct
# Check if the form is submitted

# Function to check if the password is correct
def check_password():
    pass

# Function to display the login form
def display_login_form():
    pass

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

