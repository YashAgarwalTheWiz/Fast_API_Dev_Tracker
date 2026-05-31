import streamlit as st
import requests

st.markdown("""
<style>
[data-testid="stSidebarNav"] {display: none;}
</style>
""", unsafe_allow_html=True)
st.set_page_config(initial_sidebar_state="collapsed")

st.title("Dev Tracker 🧠")

url = "https://fast-api-dev-tracker.onrender.com"

#main section
email=st.text_input('enter your email')
password=st.text_input('enter your password',type='password')

payload={
    'email':email,
    'password':password
}

#login button 
if st.button('login'):
    if not email or not password:
        st.error("Please enter email and password")
    else:
        response=requests.post(url+'/login',json=payload).json()
        if response:
            st.session_state['token']=response['access_token']
            st.switch_page('pages/tracker.py')
        else:
            st.error('login failed')
        

#register button 
if st.button("Don't have an account? Register"):
    st.switch_page("pages/register.py")