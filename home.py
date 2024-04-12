import streamlit as st
st.set_page_config(layout="wide")
st.markdown("""
    <h1 style='color: white;'>Connect<span style='color: yellow;'>Ed</span></h1>
    <hr>
""", unsafe_allow_html=True)
st.subheader("One Stop Place to update all your university life...")
image_urls = [
    "https://images.pexels.com/photos/1438072/pexels-photo-1438072.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
    "https://images.pexels.com/photos/159775/library-la-trobe-study-students-159775.jpeg?auto=compress&cs=tinysrgb&w=600"
]
col1, col2 = st.columns(2)

# Add elements to the first column
with col1:
    st.image(image_urls[1],width=500)
with col2:
    st.image(image_urls[0],width=500)

st.subheader("Sign In Now!")

if st.button("Sign In >>"):
    st.switch_page("pages/Login.py")
