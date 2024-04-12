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

with open("log.txt","r") as f:
    un=f.read()

st.markdown("""
    <h1 style='color: white;'>Connect<span style='color: yellow;'>Ed</span></h1>
            <h2>Mentor Details</h2>
    <hr>
""", unsafe_allow_html=True)

students_ref = db.reference("/students")
all = students_ref.get()
oner = None
for one in all:
    if all[one]["username"]== un:
        oner = all[one]
        break

mentor = oner["mentor"]

mentor_ref = db.reference("/mentors")

moner = None
allm = mentor_ref.get()
for i in allm:
    if allm[i]["name"] == mentor:
        moner = allm[i]
        with st.chat_message("human"):
            st.subheader("Name: "+moner["name"])
            st.subheader("Qualifications: "+moner["degree"])
            st.subheader("Experience: "+str(moner["exp"])+" Years")
            st.header(str(allm[i]["rating"])+"⭐")
        break

if st.button("Back to Dashboard!"):
    st.switch_page("pages/Your_Meetings.py")

        



# mentor_ref.push({
#     "name" : "Elena",
#     "degree" : "M. Tech",
#     "exp" : 18,
#     "rating" : 3.1,
#     "mentee" : "Null"
# })
