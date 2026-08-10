import streamlit as st

st.title("Counter - FIXED")

if "counter" not in st.session_state:
    st.session_state.counter = 0

if st.button("Click me", key="increment_button"):
    st.session_state.counter += 1

st.write(f"Count: {st.session_state.counter}")