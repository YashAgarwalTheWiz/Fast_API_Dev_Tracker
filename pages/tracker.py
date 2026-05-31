import streamlit as st 
from datetime import date
import requests
import matplotlib.pyplot as plt
import calendar
from utils import streak_calculator
import pandas as pd

# stopping that side bar from appearing
st.set_page_config(initial_sidebar_state="collapsed")

st.markdown("""
<style>
[data-testid="stSidebarNav"] {display: none;}
</style>
""", unsafe_allow_html=True)

# managing the session state and not letting anyone login by directly pasting url
if 'token' not in st.session_state:
    st.error("Please login first")
    st.switch_page("frontend.py")
    st.stop()

token = st.session_state['token']
headers = {"Authorization": f"Bearer {token}"}

url = "https://fast-api-dev-tracker.onrender.com"

dates=requests.get(url+'/activedates',headers=headers).json()

#subheader 
months=["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
st.subheader(f"📅 {months[date.today().month-1]} {date.today().year} Activity")
days_col=st.columns(7)

#for priniting the boxes
days_list = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
for i in range(0,7):
    with days_col[i]:
        st.write(days_list[i])
dates_list=[row['entry_date'] for row in dates]
cols=st.columns(7)
weekday,total_days=calendar.monthrange(date.today().year,date.today().month)
for day in range(1,total_days+1):
    with cols[weekday]:
        if str(date(date.today().year,date.today().month, day)) in dates_list:
            st.write('✅')
        else:
            st.write('☐')
    weekday+=1
    if weekday==7:
        weekday=0
        cols=st.columns(7)

#calculating the streak
streak=streak_calculator(dates_list)
st.write(f'your streak is {streak}')
st.divider()

#main section starts
problems=st.text_input("Enter your problems")
topic=st.selectbox("Enter the topic",("Array", "String", "Linked List", "Stack", "Queue", "Deque", "Hashing", "Tree", "Binary Search Tree", "Heap", "Trie", "Graph", "Matrix", "Recursion", "Backtracking", "Dynamic Programming", "Greedy", "Divide and Conquer", "Sorting", "Searching", "Binary Search", "Bit Manipulation", "Math", "Two Pointers", "Sliding Window"))
difficulty=st.selectbox("select the difficulty",('easy','medium','hard'))
date=date.today()

payload={
    'problem_name':problems,
    'topic':topic,
    'difficulty':difficulty,
    'entry_date':str(date)
}

#saving the data
if st.button("save data"):
    if not problems:
        st.error('please add problem name')
    else:
        response = requests.post(url+'/insert_data', json=payload, headers=headers)
        if response.status_code==200:
            st.write('saved successfully')
            st.rerun()
        else:
            st.write('kuch fata')

#viewing the data
st.divider()
if st.button("see data"):
    data=requests.get(url+'/my_problems',headers=headers).json()
    df = pd.DataFrame(data)
    df.drop(columns=['user_id'],inplace=True)
    df.index=df.index+1
    st.dataframe(df)

#pie charts
if st.button('pie chart by difficulty'):
    response=requests.get(url+'/count_by_difficulty',headers=headers)
    sizes=[]
    labels=[]
    for row in response.json():
        sizes.append(row['count'])
        labels.append(row['difficulty'])  # or row['topic'] for the topic chart
    fig,ax=plt.subplots(figsize=(2,2))
    ax.pie(sizes,labels=labels,autopct='%1.1f%%',textprops={'fontsize': 8})
    ax.set_title("Problems by Difficulty")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.pyplot(fig)

if st.button('pie chart by topic'):
    response=requests.get(url+'/count_by_topic',headers=headers)
    sizes=[]
    labels=[]
    for row in response.json():
        sizes.append(row['count'])
        labels.append(row['topic'])  
    fig,ax=plt.subplots(figsize=(2,2))
    ax.pie(sizes,labels=labels,autopct='%1.1f%%',textprops={'fontsize': 8})
    ax.set_title("Problems by topic")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.pyplot(fig)

st.divider()

#logout button 
if st.button('logout?'):
    st.session_state.clear()
    st.switch_page('frontend.py')