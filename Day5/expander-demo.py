import streamlit as st

st.title("Expander Demo")

user_name = st.text_input("Your name", key="user_name")

with st.expander("Advanced options", expanded=False):
    threshold = st.slider("Threshold", 0.0, 1.0, 0.5, key="threshold")
    use_cache = st.checkbox("Use cache", value=True, key="use_cache")

st.write(f"Threshold: {threshold}, Cache: {use_cache}")