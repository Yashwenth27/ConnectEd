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
            <h3>Search Mentors</h3>
    <hr>
""", unsafe_allow_html=True)

with open("log.txt","r") as f:
    un=f.read()

ref = db.reference("/mentors")
all = ref.get()
for one in all:
    with st.chat_message("human"):
        st.subheader(all[one]["name"])
        st.write("Qualifications: "+all[one]["degree"])
        st.write("Experience: "+str(all[one]["exp"])+" Years")
        st.subheader(str(all[one]["rating"])+"⭐")
        if st.button("Choose as mentor",key=all[one]["name"]):
            students_ref = db.reference("/students")
            alls = students_ref.get()
            oner = None
            for oneo in alls:
                if alls[oneo]["username"]== un:
                    oner = oneo
                    break
            alls[oner]["mentor"] = all[one]["name"]
            #mentor side update
            all[one]["mentee"] = alls[oner]["name"]
            ref.update({one: all[one]})
            st.success("Mentor Changed Successfully")
            students_ref.update({oner: alls[oner]})
