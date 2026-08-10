import streamlit as st

st.title("Dashboard Demo")

with st.sidebar:
    st.write("**Controls**")
    user_name = st.text_input("Name", key="user_name")
    user_age = st.slider("Age", 0, 100, 20, key="user_age")
    favorite_color = st.selectbox(
        "Favorite color",
        ["Red", "Green", "Blue"],
        key="favorite_color",
    )
  
st.write(f"Hello, **{user_name}**!")
st.write(f"You are **{user_age}** years old.")
st.write(f"Your favorite color is **{favorite_color}**.")