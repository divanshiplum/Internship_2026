import streamlit as st

st.title("Counter - BROKEN")

counter = 0

if st.button("Click me", key="increment_button"):
    counter += 1

st.write(f"Count: {counter}")