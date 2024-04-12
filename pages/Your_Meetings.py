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
            <h2>Your Dashboard</h2>
    <hr>
""", unsafe_allow_html=True)

with open("log.txt","r") as f:
    un=f.read()

students_ref = db.reference("/students")
all = students_ref.get()
oner = None
for one in all:
    if all[one]["username"]== un:
        oner = all[one]
        break
c1,c2 = st.columns(2)
with c1:
    with st.chat_message("human"):
        st.subheader(oner["name"])
        st.caption("@"+oner["username"])
        st.write("B.Tech, "+oner["course"] + " \n\nRegister No: "+oner["regno"])
        st.write("Mentor: "+oner["mentor"])

with c2:
    att = oner["attendance"]
    st.write(att)
    st.subheader("Attendance:")
    st.progress(att,str(att)+"%")
    st.subheader("Next Meeting: ")
    if len(oner["meetings"])==1:
        st.write("No Meetings Ahead!")
    else:
        #meeting id to meeting details
        st.write("Meeting with "+oner["mentor"]+" @ "+oner["meetings"][0])

a1,a2,a3 = st.columns(3)

with a1:
    if st.button("Mentor Details"):
        st.switch_page("pages/Mentor_Details.py")
with a2:
    if st.button("Get Mentor"):
        st.switch_page("pages/Search_Mentors.py")
with a3:
    if st.button("Book a Meet!"):
        st.switch_page("pages/Book_A_Meet.py")


