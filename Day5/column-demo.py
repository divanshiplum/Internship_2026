import streamlit as st

st.title("Two Columns Demo")

col1, col2 = st.columns(2)

with col1:
    st.write("**Left column**")
    user_name = st.text_input("Name", key="user_name")

with col2:
    st.write("**Right column**")
    user_age = st.slider("Age", 0, 100, 20, key="user_age")

st.divider()
st.write(f"{user_name} is {user_age} years old.")
