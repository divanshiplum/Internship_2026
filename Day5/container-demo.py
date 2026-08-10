import streamlit as st

st.title("Container Demo")

holder = st.container()

st.write("This renders first.")

with holder:
    st.write("This renders ABOVE 'first'.")
    st.write("Even though it is defined later in the script.")