import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

st.set_page_config(
    page_title="My Expense Tracker",
    page_icon="💰",
    layout="wide"
)

st.markdown("""
<style>
.stApp {
    background: linear-gradient(
        135deg,
        #ffffff 0%,
        #ffd6d6 45%,
        #ff4d4d 100%
    );
    min-height: 100vh;
}

h1 {
    background: linear-gradient(90deg, #8b0000, #c1121f) !important;
    color: white !important;
    text-align: center !important;
    padding: 15px !important;
    border-radius: 10px !important;
    margin-bottom: 25px !important;
}

h2, h3, h4 {
    color: black !important;
    font-weight: bold !important;
}

.expense-heading {
    background: linear-gradient(90deg, #4a0000, #8b0000);
    color: white !important;
    padding: 15px;
    border-left: 8px solid #ff1e1e;
    border-radius: 8px;
    font-size: 24px;
    font-weight: bold;
    margin-bottom: 20px;
}

label {
    color: black !important;
    font-weight: bold !important;
}

div[data-baseweb="input"] {
    border: 1px solid black;
}

.stButton > button {
    background-color: red !important;
    color: white !important;
    border: 2px solid red !important;
    border-radius: 6px !important;
    width: 100%;
    font-weight: bold !important;
}

.stButton > button:hover {
    background-color: black !important;
    color: white !important;
    border: 2px solid black !important;
}

.stButton > button:active {
    background-color: black !important;
    color: white !important;
}

.stButton > button:focus {
    background-color: black !important;
    color: white !important;
}

.total-box {
    background: linear-gradient(90deg, #4a0000, #8b0000);
    color: white;
    padding: 20px;
    border-left: 8px solid #ff1e1e;
    border-radius: 8px;
    margin-top: 25px;
    margin-bottom: 25px;
}

.total-label {
    color: white;
}

.total-value {
    color: #ff4d4d;
}

.chart-heading {
    color: black;
    font-size: 22px;
    font-weight: bold;
    margin-top: 20px;
}
</style>
""", unsafe_allow_html=True)

st.markdown(
    '<h1>MY EXPENSE TRACKER 💸</h1>',
    unsafe_allow_html=True
)

csv_path = Path(__file__).parent / "expenses.csv"

df = pd.read_csv(csv_path)

st.markdown(
    '<div class="expense-heading">Add Your Expense 👇</div>',
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:

    amount = st.number_input(
        "Amount (₹)",
        min_value=0,
        step=10
    )

    category = st.text_input(
        "Category"
    )

with col2:

    date = st.date_input(
        "Date"
    )

    note = st.text_input(
        "Note"
    )

if st.button("ADD EXPENSE"):

    if amount <= 0:

        st.error("⚠️ Please enter a valid amount.")

    elif category.strip() == "":

        st.error("⚠️ Please enter a category.")

    elif note.strip() == "":

        st.error("⚠️ Please enter a note.")

    else:

        new_expense = {
            "Date": date,
            "Category": category.strip(),
            "Note": note.strip(),
            "Amount": amount
        }

        df.loc[len(df)] = new_expense

        df.to_csv(csv_path, index=False)

        st.success("✅ Expense added successfully!")

        st.rerun()

total = df["Amount"].sum()

st.markdown(
    f"""
    <div class="total-box">
        <div class="total-label">TOTAL SPENT</div>
        <div class="total-value">₹ {total:,.0f}</div>
    </div>
    """,
    unsafe_allow_html=True
)

st.subheader("Spending by Category")

category_total = df.groupby("Category")["Amount"].sum()

fig, ax = plt.subplots(figsize=(6, 3))

ax.bar(
    category_total.index,
    category_total.values,
    color="red"
)

ax.set_xlabel(
    "Category",
    labelpad=8
)

ax.set_ylabel("Amount (₹)")

plt.tight_layout()

st.pyplot(fig)

st.subheader("Recent Expenses")

st.dataframe(
    df,
    use_container_width=True,
    hide_index=True
)