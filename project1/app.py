import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path


# ---------------- PAGE SETTINGS ----------------

st.set_page_config(
    page_title="My Expense Tracker",
    page_icon="💰",
    layout="wide"
)


# ---------------- CSS ----------------

st.markdown("""
<style>

/* Whole page */
.stApp {
    background-color: white;
}


/* Main title */
h1 {
    background-color: black !important;
    color: red !important;
    text-align: center !important;
    padding: 15px !important;
    border: 2px solid red !important;
    border-radius: 10px !important;
    margin-bottom: 25px !important;
}


/* Add Expense and other headings */
h2, h3, h4 {
    color: black !important;
    font-weight: bold !important;
}


/* Add Expense heading */
.expense-heading {
    background-color: black;
    color: white;
    padding: 15px;
    border-left: 8px solid red;
    border-radius: 8px;
    font-size: 24px;
    font-weight: bold;
    margin-bottom: 20px;
}


/* Labels */
label {
    color: black !important;
    font-weight: bold !important;
}


/* Input boxes */
div[data-baseweb="input"] {
    border: 1px solid black;
}


/* ---------------- BUTTON ---------------- */

/* Normal */
.stButton > button {
    background-color: red !important;
    color: white !important;
    border: 2px solid red !important;
    border-radius: 6px !important;
    width: 100%;
    font-weight: bold !important;
}


/* Hover */
.stButton > button:hover {
    background-color: black !important;
    color: white !important;
    border: 2px solid black !important;
}


/* Click */
.stButton > button:active {
    background-color: black !important;
    color: white !important;
}


/* Focus */
.stButton > button:focus {
    background-color: black !important;
    color: white !important;
}


/* ---------------- TOTAL BOX ---------------- */

.total-box {
    background-color: black;
    color: white;
    padding: 20px;
    border-left: 8px solid red;
    border-radius: 8px;
    margin-top: 25px;
    margin-bottom: 25px;
}

.total-label {
    color: white;
    font-size: 16px;
    font-weight: bold;
}

.total-value {
    color: red;
    font-size: 32px;
    font-weight: bold;
}


/* Chart heading */
.chart-heading {
    color: black;
    font-size: 22px;
    font-weight: bold;
    margin-top: 20px;
}

</style>
""", unsafe_allow_html=True)


# ---------------- TITLE ----------------

st.markdown(
    '<h1>MY EXPENSE TRACKER 💰</h1>',
    unsafe_allow_html=True
)


# ---------------- CSV FILE ----------------

csv_path = Path(__file__).parent / "expenses.csv"

df = pd.read_csv(csv_path)


# ---------------- ADD EXPENSE ----------------

st.markdown(
    '<div class="expense-heading">Add Your Expense 👇</div>',
    unsafe_allow_html=True
)


col1, col2 = st.columns(2)


# Left column
with col1:

    amount = st.number_input(
        "Amount (₹)",
        min_value=0,
        step=10
    )

    category = st.text_input(
        "Category"
    )


# Right column
with col2:

    date = st.date_input(
        "Date"
    )

    note = st.text_input(
        "Note"
    )


# ---------------- ADD BUTTON ----------------

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


# ---------------- TOTAL SPENT ----------------

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


# ---------------- CHART ----------------

# ---------------- CHART ----------------

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

# ---------------- RECENT EXPENSES ----------------

st.subheader("Recent Expenses")

st.dataframe(
    df,
    use_container_width=True,
    hide_index=True
)