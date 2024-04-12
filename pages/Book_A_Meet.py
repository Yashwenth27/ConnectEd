import streamlit as st
import firebase_admin
from firebase_admin import db, credentials
st.set_page_config(layout="wide")

# Check if Firebase app is already initialized
if not firebase_admin._apps:
    try:
        # Initialize Firebase Admin SDK
        cred = credentials.Certificate("connected-3948a-firebase-adminsdk-zthtg-53ccdd7723.json")
        firebase_admin.initialize_app(cred, {"databaseURL": "https://connected-3948a-default-rtdb.firebaseio.com"})
    except Exception as e:
        st.error(f"Firebase initialization error: {e}")

# Set up Streamlit layout
if st.button("Back to Dashboard"):
    st.switch_page("pages/Your_Meetings.py")
st.markdown("""
    <h1 style='color: white;'>Connect<span style='color: yellow;'>Ed</span></h1>
            <h3>Book a meeting with mentor!</h3>
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

meet = oner["meetings"]

st.subheader("Choose a time slot: ")
c1,c2,c3 = st.columns(3)
with c1:
    opt=st.radio("Morning",["8-9","9-10","10-11","11-12"],index=None)
with c2:
    opt2 = st.radio("Afternoon",["12-1","1-2","2-3","3-4"],index=None)
with c3:
    opt3 = st.radio("Evening",["4-5","5-6","6-7","7-8"],index=None)

if st.button("Fix a meet!"):
    meet.pop()
    if opt!=None and opt not in meet:
        meet.append(opt)
    else:
        st.warning("Selected Morning slot is unavailable!")
    if opt2!=None and opt2 not in meet:
        meet.append(opt2)
    else:
        st.warning("Selected afternoon slot is unavailable!")
    if opt3!=None and opt3 not in meet:
        meet.append(opt3)
    else:
        st.warning("Selected evening slot is unavailable!")
    st.success("Meeting Booked with Mentor")

students_ref.update({one:oner})
