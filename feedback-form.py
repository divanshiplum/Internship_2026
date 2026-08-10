import streamlit as st

st.set_page_config(
    page_title="Feedback Form",
    page_icon="📝",
    layout="centered"
)

st.title("📝 Feedback Form")
st.write("We would love to hear your feedback!")

with st.form("feedback_form"):

    name = st.text_input(
        "Your Name",
        placeholder="Enter your name"
    )

    email = st.text_input(
        "Email Address",
        placeholder="Enter your email"
    )

    gender = st.selectbox(
        "Gender",
        [
            "Select Gender",
            "Male",
            "Female",
            "Other",
            "Prefer not to say"
        ]
    )

    rating = st.slider(
        "How would you rate your experience?",
        min_value=1.0,
        max_value=5.0,
        value=1.0,
        step=0.1,
        format="%.1f"
    )

    feedback = st.text_area(
        "Your Feedback",
        placeholder="Tell us about your experience..."
    )

    suggestion = st.text_area(
        "Any Suggestions?",
        placeholder="How can we improve?"
    )

    submitted = st.form_submit_button("Submit Feedback")

if submitted:
    
    if (
        name.strip() == ""
        or email.strip() == ""
        or gender == "Select Gender"
        or feedback.strip() == ""
        or suggestion.strip() == ""
    ):
        st.warning("⚠️ Please fill in all the fields.")

    else:
        st.success("✅ Thank you for your valuable feedback!")

        st.write("### Your Feedback")

        st.write(f"**Name:** {name}")
        st.write(f"**Email:** {email}")
        st.write(f"**Gender:** {gender}")
        st.write(f"**Rating:** {rating:.1f} ⭐")
        st.write(f"**Feedback:** {feedback}")

        if suggestion.strip():
            st.write(f"**Suggestion:** {suggestion}")