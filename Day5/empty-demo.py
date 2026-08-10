import time

import streamlit as st

st.title("Empty Demo")

status = st.empty()

status.write("Loading...")

time.sleep(1)

status.write("Done!")