import streamlit as st

st.title("Tabs Demo")

tab_input, tab_chart, tab_raw = st.tabs(["Input", "Chart", "Raw Data"])

with tab_input:
    st.write("**Enter your details**")
    user_name = st.text_input("Name", key="user_name")
    user_age = st.slider("Age", 0, 100, 20, key="user_age")
    st.write(f"{user_name} is {user_age} years old.")

with tab_chart:
    st.write("Chart goes here")
    st.caption("Real charts arrive on Day 7 - Charts & Dashboards.")

with tab_raw:
    st.write("Raw data goes here")
    st.caption("Real dataframes arrive on Day 6 - Working With Data.")