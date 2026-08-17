import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Page settings
st.set_page_config(
    page_title="My Expense Tracker",
    page_icon="💰"
)

# CSS
st.markdown("""
<style>

.stApp {
    background-color: white;
    color: black;
}

h1 {
    color: red;
    text-align: center;
}

h2, h3 {
    color: black;
    margin-top: 5px;
}

.expense-box {
    background-color: black;
    padding: 20px;
    border-radius: 10px;
    border: 2px solid red;
}

.expense-title {
    color: white;
    font-size: 25px;
    font-weight: bold;
}

.stButton > button {
    background-color: red;
    color: white;
    width: 100%;
    border-radius: 6px;
    font-weight: bold;
}

.total-box {
    background-color: black;
    color: white;
    padding: 20px;
    border-radius: 10px;
    border-left: 8px solid red;
    margin-top: 20px;
}

.total-title {
    color: white;
    font-size: 15px;
}

.total-amount {
    color: red;
    font-size: 30px;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)


# Title
st.title("MY EXPENSE TRACKER")


# CSV file
csv_path = Path(__file__).parent / "expenses.csv"

df = pd.read_csv(csv_path)


# ---------------- ADD EXPENSE ----------------

st.markdown("""
<div class="expense-box">
    <div class="expense-title">➕ Add Expense</div>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:

    st.markdown("**Amount (₹)**")
    amount = st.number_input(
        "Amount",   
        step=10,
        label_visibility="collapsed"
    )

    st.markdown("**Category**")
    category = st.text_input(
        "Category",
        label_visibility="collapsed"
    )


with col2:

    st.markdown("**Date**")
    date = st.date_input(
        "Date",
        label_visibility="collapsed"
    )

    st.markdown("**Note**")
    note = st.text_input(
        "Note",
        label_visibility="collapsed"
    )

# Add button
if st.button("ADD EXPENSE"):

    new_expense = {
        "Date": date,
        "Category": category,
        "Note": note,
        "Amount": amount
    }

    df.loc[len(df)] = new_expense

    df.to_csv(csv_path, index=False)

    st.success("Expense added successfully!")

    st.rerun()


# ---------------- TOTAL ----------------

total = df["Amount"].sum()

st.markdown(f"""
<div class="total-box">
    <div class="total-title">TOTAL SPENT</div>
    <div class="total-amount">₹ {total:,.0f}</div>
</div>
""", unsafe_allow_html=True)


# ---------------- CHART ----------------

st.subheader("Spending by Category")

category_total = df.groupby("Category")["Amount"].sum()

fig, ax = plt.subplots()

ax.bar(
    category_total.index,
    category_total.values,
    color="red"
)

st.pyplot(fig)


# ---------------- RECENT EXPENSES ----------------

st.subheader("Recent Expenses")

st.dataframe(
    df,
    use_container_width=True,
    hide_index=True
)