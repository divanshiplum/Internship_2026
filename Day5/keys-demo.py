import streamlit as st

st.title("Widget Keys Demo")

col_without_key, col_with_key = st.columns(2)

with col_without_key:
    st.write("**Without a key**")
    anonymous_name = st.text_input("Your name (no key)")
    st.caption("Only reachable through the returned value.")

with col_with_key:
    st.write("**With a key**")
    keyed_name = st.text_input("Your name (keyed)", key="user_name")
    st.caption("Also reachable as st.session_state.user_name")

st.divider()

if st.button("Read the keyed widget from session_state", key="read_button"):
    st.write(f"st.session_state.user_name = {st.session_state.user_name!r}")
    st.write(f"The unkeyed box returned: {anonymous_name!r} (variable only)")