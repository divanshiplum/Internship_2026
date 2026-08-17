import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path


# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="My Expense Tracker",
    page_icon="💰",
    layout="wide"
)


# =========================
# CUSTOM CSS
# =========================

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


/* HEADER */

header[data-testid="stHeader"] {
    background: linear-gradient(
        90deg,
        #4a0000,
        #8b0000
    ) !important;
}

div[data-testid="stToolbar"] {
    background: transparent !important;
}


/* MENU */

div[role="menu"] {
    background: #4a0000 !important;
    border: 2px solid #8b0000 !important;
    border-radius: 10px !important;
    padding: 8px !important;
}

div[data-baseweb="popover"] {
    background: #4a0000 !important;
    border: 2px solid #8b0000 !important;
    border-radius: 10px !important;
}

div[role="menu"] div[role="menuitem"] {
    background: #5c1111 !important;
    color: white !important;
    border-radius: 6px !important;
}

div[role="menu"] div[role="menuitem"] * {
    color: white !important;
}

div[role="menu"] div[role="menuitem"]:hover {
    background: #7a2020 !important;
    color: white !important;
}

div[data-baseweb="menu"] {
    background: #4a0000 !important;
}

div[data-baseweb="menu"] li {
    background: #5c1111 !important;
    color: white !important;
}

div[data-baseweb="menu"] li:hover {
    background: #7a2020 !important;
    color: white !important;
}

div[data-testid="stMainMenu"] {
    background: #4a0000 !important;
    color: white !important;
}

div[data-testid="stMainMenu"] * {
    color: white !important;
}

div[data-testid="stMainMenu"] button {
    background: #5c1111 !important;
    color: white !important;
    border-radius: 6px !important;
}

div[data-testid="stMainMenu"] button:hover {
    background: #7a2020 !important;
    color: white !important;
}


/* HEADER BUTTON */

header[data-testid="stHeader"] button:hover {
    background-color: black !important;
    color: white !important;
    border-radius: 6px !important;
}

header[data-testid="stHeader"] button[aria-label*="Menu"]:hover {
    background-color: black !important;
    color: white !important;
}

div[data-testid="stToolbar"] button:hover {
    background-color: black !important;
    color: white !important;
}

header[data-testid="stHeader"] button:hover * {
    color: white !important;
}


/* MAIN TITLE */

h1 {
    background: linear-gradient(
        90deg,
        #8b0000,
        #c1121f
    ) !important;

    color: white !important;
    text-align: center !important;
    padding: 15px !important;
    border-radius: 10px !important;
    margin-bottom: 25px !important;
}


/* HEADINGS */

h2,
h3,
h4 {
    color: black !important;
    font-weight: bold !important;
}


/* SECTION HEADING */

.expense-heading {
    background: linear-gradient(
        90deg,
        #4a0000,
        #8b0000
    );

    color: white !important;
    padding: 15px;
    border-left: 8px solid #ff1e1e;
    border-radius: 8px;
    font-size: 24px;
    font-weight: bold;
    margin-bottom: 20px;
}


/* SIDEBAR HEADING */

[data-testid="stSidebar"] .expense-heading {
    font-size: 20px;
    padding: 12px;
}


/* LABELS */

label {
    color: black !important;
    font-weight: bold !important;
}


/* INPUT */

div[data-baseweb="input"] {
    border: 1px solid black;
}


/* BUTTON */

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


/* TOTAL BOX */

.total-box {
    background: linear-gradient(
        90deg,
        #4a0000,
        #8b0000
    );

    color: white;
    padding: 20px;
    border-left: 8px solid #ff1e1e;
    border-radius: 8px;
    margin-top: 25px;
    margin-bottom: 25px;
}

.total-label {
    color: white;
    font-weight: bold;
    font-size: 30px;
}

.total-value {
    color: #ff4d4d;
    font-weight: bold;
    font-size: 20px;
}


/* FILTER BOX */

.filter-box {
    background-color: rgba(255, 255, 255, 0.7);
    padding: 20px;
    border-radius: 10px;
    border: 2px solid #8b0000;
    margin-bottom: 25px;
}


/* SIDEBAR */

[data-testid="stSidebar"] {
    background: linear-gradient(
        180deg,
        #ffffff 0%,
        #ffd6d6 60%,
        #ffb3b3 100%
    );
}


/* SIDEBAR DIVIDER */

[data-testid="stSidebar"] hr {
    border-color: #8b0000 !important;
}

</style>
""", unsafe_allow_html=True)


# =========================
# TITLE
# =========================

st.markdown(
    '<h1>MY EXPENSE TRACKER 💸</h1>',
    unsafe_allow_html=True
)


# =========================
# CSV FILE
# =========================

csv_path = Path(__file__).parent / "expenses.csv"


# =========================
# LOAD DATA
# =========================

try:
    df = pd.read_csv(csv_path)
except FileNotFoundError:
    df = pd.DataFrame(
        columns=[
            "Date",
            "Category",
            "Note",
            "Amount"
        ]
    )


# =========================
# REQUIRED COLUMNS
# =========================

required_columns = [
    "Date",
    "Category",
    "Note",
    "Amount"
]

for column in required_columns:

    if column not in df.columns:
        df[column] = ""


# =========================
# DATA CLEANING
# =========================

df["Date"] = pd.to_datetime(
    df["Date"],
    errors="coerce"
).dt.date

df["Amount"] = pd.to_numeric(
    df["Amount"],
    errors="coerce"
).fillna(0)


# =========================
# SIDEBAR
# ADD EXPENSE
# =========================

with st.sidebar:

    st.markdown(
        '<div class="expense-heading">Add Your Expense 👇</div>',
        unsafe_allow_html=True
    )

    amount = st.number_input(
        "Amount (₹)",
        min_value=0,
        step=10
    )

    category = st.text_input(
        "Category"
    )

    date = st.date_input(
        "Date"
    )

    note = st.text_input(
        "Note"
    )

    st.markdown("---")

    if st.button("ADD EXPENSE"):

        if amount <= 0:

            st.error(
                "⚠️ Please enter a valid amount."
            )

        elif category.strip() == "":

            st.error(
                "⚠️ Please enter a category."
            )

        elif note.strip() == "":

            st.error(
                "⚠️ Please enter a note."
            )

        else:

            new_expense = {
                "Date": date,
                "Category": category.strip(),
                "Note": note.strip(),
                "Amount": amount
            }

            df.loc[len(df)] = new_expense

            df.to_csv(
                csv_path,
                index=False
            )

            st.success(
                "✅ Expense added successfully!"
            )

            st.rerun()


# =========================
# TOTAL SPENT
# =========================

total = df["Amount"].sum()


st.markdown(
    f"""
    <div class="total-box">
        <div class="total-label">
            TOTAL SPENT
        </div>

        <div class="total-value">
            ₹ {total:,.0f}
        </div>
    </div>
    """,
    unsafe_allow_html=True
)


# =========================
# FILTER EXPENSES
# =========================

st.markdown(
    '<div class="expense-heading">Filter Expenses 🔎</div>',
    unsafe_allow_html=True
)


# =========================
# FILTER ROW
# =========================

filter_col1, filter_col2, filter_col3 = st.columns(3)


# CATEGORY FILTER

with filter_col1:

    categories = (
        ["All"]
        +
        sorted(
            df["Category"]
            .dropna()
            .astype(str)
            .unique()
            .tolist()
        )
    )

    selected_category = st.selectbox(
        "Filter by Category",
        categories
    )


# MINIMUM AMOUNT

with filter_col2:

    if not df.empty:

        maximum_amount = int(
            df["Amount"].max()
        )

    else:

        maximum_amount = 0

    min_amount = st.number_input(
        "Minimum Amount (₹)",
        min_value=0,
        value=0,
        step=10
    )


# MAXIMUM AMOUNT

with filter_col3:

    max_amount = st.number_input(
        "Maximum Amount (₹)",
        min_value=0,
        value=maximum_amount,
        step=10
    )


# =========================
# DATE FILTER
# =========================

if (
    not df.empty
    and df["Date"].notna().any()
):

    min_date = (
        df["Date"]
        .dropna()
        .min()
    )

    max_date = (
        df["Date"]
        .dropna()
        .max()
    )

else:

    min_date = (
        pd.Timestamp
        .today()
        .date()
    )

    max_date = (
        pd.Timestamp
        .today()
        .date()
    )


date_col1, date_col2 = st.columns(2)


with date_col1:

    start_date = st.date_input(
        "From Date",
        value=min_date
    )


with date_col2:

    end_date = st.date_input(
        "To Date",
        value=max_date
    )


# =========================
# APPLY FILTERS
# =========================

filtered_df = df.copy()


# CATEGORY

if selected_category != "All":

    filtered_df = filtered_df[
        filtered_df["Category"]
        .astype(str)
        == selected_category
    ]


# AMOUNT

if min_amount <= max_amount:

    filtered_df = filtered_df[
        (filtered_df["Amount"] >= min_amount)
        &
        (filtered_df["Amount"] <= max_amount)
    ]

else:

    st.warning(
        "⚠️ Minimum amount cannot be greater than maximum amount."
    )

    filtered_df = filtered_df.iloc[0:0]


# DATE

if start_date <= end_date:

    filtered_df = filtered_df[
        (filtered_df["Date"] >= start_date)
        &
        (filtered_df["Date"] <= end_date)
    ]

else:

    st.warning(
        "⚠️ From Date cannot be after To Date."
    )

    filtered_df = filtered_df.iloc[0:0]


# =========================
# SHOWING COUNT
# =========================

st.markdown(
    f"""
    <div style="
        color: #4a0000;
        font-size: 18px;
        font-weight: bold;
        margin-top: 10px;
        margin-bottom: 10px;
    ">
        Showing {len(filtered_df)} expense(s)
    </div>
    """,
    unsafe_allow_html=True
)


# =========================
# FILTERED TOTAL
# =========================

filtered_total = filtered_df["Amount"].sum()


st.markdown(
    f"""
    <div class="total-box">
        <div class="total-label">
            FILTERED TOTAL
        </div>

        <div class="total-value">
            ₹ {filtered_total:,.0f}
        </div>
    </div>
    """,
    unsafe_allow_html=True
)


# =========================
# SPENDING BY CATEGORY
# =========================

st.subheader(
    "Spending by Category"
)


if not filtered_df.empty:

    category_total = (
        filtered_df
        .groupby("Category")["Amount"]
        .sum()
    )


    fig, ax = plt.subplots(
        figsize=(8, 4)
    )


    ax.bar(
        category_total.index,
        category_total.values,
        color="red"
    )


    ax.set_xlabel(
        "Category",
        labelpad=8
    )


    ax.set_ylabel(
        "Amount (₹)"
    )


    ax.set_title(
        "Expenses by Category"
    )


    plt.xticks(
        rotation=45,
        ha="right"
    )


    plt.tight_layout()


    st.pyplot(fig)


    plt.close(fig)


else:

    st.warning(
        "⚠️ No expenses found for the selected filters."
    )


# =========================
# RECENT EXPENSES
# =========================

st.subheader(
    "Recent Expenses"
)


if not filtered_df.empty:

    display_df = (
        filtered_df
        .sort_values(
            by="Date",
            ascending=False
        )
    )


    st.dataframe(
        display_df,
        use_container_width=True,
        hide_index=True
    )


else:

    st.info(
        "No expenses available to display."
    )