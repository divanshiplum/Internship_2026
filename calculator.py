import streamlit as st

st.title("🧮 Calculator")

# Input fields
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

# Operation
operation = st.selectbox(
    "Select Operation",
    ["Select Operation", "Addition", "Subtraction", "Multiplication", "Division"]
)

# Calculate button
if st.button("Calculate"):

    # Validation 1: First number
    if num1 is None:
        st.error("⚠️ Please enter the first number.")

    # Validation 2: Second number
    elif num2 is None:
        st.error("⚠️ Please enter the second number.")

    # Validation 3: Operation
    elif operation == "Select Operation":
        st.error("⚠️ Please select an operation.")

    # Validation 4: Division by zero
    elif operation == "Division" and num2 == 0:
        st.error("❌ Cannot divide by zero!")

    else:
        # Calculations
        if operation == "Addition":
            result = num1 + num2

        elif operation == "Subtraction":
            result = num1 - num2

        elif operation == "Multiplication":
            result = num1 * num2

        elif operation == "Division":
            result = num1 / num2

        # Display result
        st.success(f"✅ Result = {result}")