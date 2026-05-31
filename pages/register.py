import streamlit as st
import requests
from utils import validate_password,validate_email_util

st.markdown("""
<style>
[data-testid="stSidebarNav"] {display: none;}
</style>
""", unsafe_allow_html=True)
st.set_page_config(initial_sidebar_state="collapsed")

#title
st.title("Dev Tracker 🧠")

url = "https://fast-api-dev-tracker.onrender.com"

#main section
name=st.text_input('enter your name')
email=st.text_input('enter your email')
password=st.text_input('enter your password', type='password', help="Min 8 chars, 1 uppercase, 1 number, 1 special character")

if email and not validate_email_util(email):
    st.error("Please enter a valid email address")
    st.stop()

payload={
    'name':name,
    'email':email,
    'password':password
}

if st.button('register'):
    if not email or not password or not name:
        st.error("Please enter email, name and password")
    else:
        error = validate_password(password)
        if error:
            st.error(error)
        else:
            response=requests.post(url+'/register',json=payload).json()
            if response.get('message') == 'registered successfully':
                st.write('user_registered pls login again')
                st.switch_page('frontend.py')
            else:
                st.error('Duplicate email-id')

#login button
if st.button('wanna login?'):
    st.switch_page('frontend.py')