import streamlit as st
import authlib


IMAGE_ADDRESS = "https://medlineplus.gov/images/Diabetes_share.jpg"


if not st.user.is_logged_in:
    st.title("Diabetics Prediction")
    st.image(IMAGE_ADDRESS)
    if st.sidebar.button("Log in with Google", type="primary", icon=":material/login:"):
        st.login()
        

else:
    st.subheader('Please visit the App')
    #st.html(f"Hello, <span style='color: orange; font-weight: bold;'>{st.experimental_user.name}</span>!")
    if st.sidebar.button("Log out", type="secondary", icon=":material/logout:"):
        st.logout()
