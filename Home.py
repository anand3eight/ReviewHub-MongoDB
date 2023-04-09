import streamlit as st
import sys
sys.path.insert(0, '/Users/anand/PycharmProjects/DbmsProject/LoginPage/DBOperations')
import DBUserOperations as DB

if __name__ == "__main__" :
    x = st.empty()
    dbObj = DB.DBUser()
    st.markdown("<h1 style='text-align: center; color: white;'>Welcome to Google Reviews⭐️</h1>", unsafe_allow_html=True)