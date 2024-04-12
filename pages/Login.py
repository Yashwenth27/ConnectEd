import streamlit as st
import firebase_admin
from firebase_admin import db, credentials
st.set_page_config(layout="wide")

try:
    # Initialize Firebase Admin SDK
    cred = credentials.Certificate("connected-3948a-firebase-adminsdk-zthtg-53ccdd7723.json")
    firebase_admin.initialize_app(cred, {"databaseURL": "https://connected-3948a-default-rtdb.firebaseio.com"})
except Exception as e:
    print("hello")

# Get a reference to the '/students' node
students_ref = db.reference("/students")



# Check if the '/students' node exists
if not students_ref.get():
    try:
        print("'/students' node created successfully")
    except Exception as e:
        print(f"Error creating '/students' node: {e}")

st.markdown("""
    <h1 style='color: white;'>Connect<span style='color: yellow;'>Ed</span></h1>
    <hr>
""", unsafe_allow_html=True)
st.title('Login')
username = st.text_input('Username')
password = st.text_input('Password', type='password')
if st.button('Login'):
    if username and password:
        all = students_ref.get()
        for one in all:
            if all[one]["username"]== username and all[one]["password"]==password:
                st.success("Logging in!")
                with open("log.txt", "w") as file:
                    file.write(username)
                st.switch_page("pages/Your_Meetings.py")
            else:
                st.warning("Wrong credentials!")
    else:
        st.warning('Please enter both username and password.')

st.caption("New to ConnectEd?")
if st.button('Sign Up'):
    st.switch_page("pages/SignUp.py")
