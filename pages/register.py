import streamlit as st
import requests

st.markdown("""
<style>
[data-testid="stSidebarNav"] {display: none;}
</style>
""", unsafe_allow_html=True)
st.set_page_config(initial_sidebar_state="collapsed")

#title
st.title("Dev Tracker 🧠")

url="http://127.0.0.1:8000"

#main section
name=st.text_input('enter your name')
email=st.text_input('enter your email')
password=st.text_input('enter your password',type='password')

payload={
    'name':name,
    'email':email,
    'password':password
}

#register button
if st.button('register'):
    if not email or not password or not name:
        st.error("Please enter email, name and password")
    else:
        response=requests.post(url+'/register',json=payload).json()
        if response=='success':
            st.write('user_registered pls login again')
            st.switch_page('frontend.py')
        else:
            st.error('Duplicate email-id')

#login button
if st.button('wanna login?'):
    st.switch_page('frontend.py')