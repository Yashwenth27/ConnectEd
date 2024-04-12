import streamlit as st
import firebase_admin
st.set_page_config(layout="wide")
from firebase_admin import db, credentials

# Check if Firebase app is already initialized
if not firebase_admin._apps:
    try:
        # Initialize Firebase Admin SDK
        cred = credentials.Certificate("connected-3948a-firebase-adminsdk-zthtg-53ccdd7723.json")
        firebase_admin.initialize_app(cred, {"databaseURL": "https://connected-3948a-default-rtdb.firebaseio.com"})
    except Exception as e:
        st.error(f"Firebase initialization error: {e}")

# Set up Streamlit layout
st.markdown("""
    <h1 style='color: white;'>Connect<span style='color: yellow;'>Ed</span></h1>
            <h2>Sign Up</h2>
    <hr>
""", unsafe_allow_html=True)

# Input fields
name = st.text_input("Enter Name:")
regno = st.text_input("Enter Register Number:")

c1, c2 = st.columns(2)
with c1:
    un = st.text_input("Enter Username:")
with c2:
    pw = st.text_input("Enter Password:")

# Dropdown for course selection
options = ["CSE", "Mech", "EEE", "ECE", "BioTech"]
course = st.selectbox("Choose your stream:", options)

# Create a schema dictionary with input values
import random as r
schema = {
    "name": name,
    "regno": regno,
    "username": un,
    "password": pw,
    "course": course,
    "mentor": "Null",
    "meetings": ["Null"],
    "attendance": r.randint(0,100)

}

# Submit button
if st.button('Submit'):
    try:
        # Get reference to the '/students' node
        students_ref = db.reference("/students")
        
        # Push the schema dictionary to the database
        students_ref.push(schema)
        with open("log.txt", "w") as file:
            file.write(un)
        st.success("Data uploaded successfully!")
        st.switch_page("pages/Your_Meetings.py")
        
    except Exception as e:
        st.error(f"Error uploading data: {e}")
