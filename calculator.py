import streamlit as st

st.title("🧮 Calculator")

num1 = st.number_input(
    "Enter first number",
    value=None,
    placeholder="Enter first number"
)

num2 = st.number_input(
    "Enter second number",
    value=None,
    placeholder="Enter second number"
)

operation = st.selectbox(
    "Select Operation",
    ["Select Operation", "Addition", "Subtraction", "Multiplication", "Division"]
)

if st.button("Calculate"):

    if num1 is None:
        st.error("⚠️ Please enter the first number.")

    elif num2 is None:
        st.error("⚠️ Please enter the second number.")

    elif operation == "Select Operation":
        st.error("⚠️ Please select an operation.")

    elif operation == "Division" and num2 == 0:
        st.error("❌ Cannot divide by zero!")

    else:
        
        if operation == "Addition":
            result = num1 + num2

        elif operation == "Subtraction":
            result = num1 - num2

        elif operation == "Multiplication":
            result = num1 * num2

        elif operation == "Division":
            result = num1 / num2

        st.success(f"✅ Result = {result}")
