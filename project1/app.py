import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

st.title("My Expense Tracker")

df = pd.read_csv("expenses.csv")

st.sidebar.header("ADD EXPENSE")

amount = st.sidebar.number_input("Amount (\u20B9)", min_value=0)
category = st.sidebar.text_input("Category")
date = st.sidebar.date_input("Date")
note = st.sidebar.text_input("Note")

if st.sidebar.button("Add Expense"):

    new_expense = {
        "Date": date,
        "Category": category,
        "Note": note,
        "Amount": amount
    }

    df.loc[len(df)] = new_expense
    df.to_csv("expenses.csv", index=False)

    st.success("Expense added!")

total = df["Amount"].sum()

st.subheader("Total Spent")
st.write("\u20B9", total)

st.subheader("Spending by Category")

category_total = df.groupby("Category")["Amount"].sum()

fig, ax = plt.subplots()

ax.bar(category_total.index, category_total.values)

ax.set_xlabel("Category")
ax.set_ylabel("Amount (\u20B9)")

st.pyplot(fig)

st.subheader("Recent Expenses")

st.dataframe(df)
