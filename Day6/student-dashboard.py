import pandas as pd
import streamlit as st


def all_option(values: pd.Series) -> list[str]:
    """Build a dropdown option list: "All" first, then each unique value."""
    return ["All"] + values.unique().tolist()


st.title("Student Dashboard")

df = pd.read_csv("students.csv")


# Sidebar filters
with st.sidebar:
    st.write("Filters")

    branch = st.selectbox(
        "Branch",
        all_option(df["branch"]),
        key="filter_branch"
    )

    city = st.selectbox(
        "City",
        all_option(df["city"]),
        key="filter_city"
    )

    low, high = st.slider(
        "Marks range",
        0,
        100,
        (0, 100),
        key="filter_marks"
    )


# Search
search = st.text_input(
    "Search by name",
    key="filter_search"
)


# Show all students
st.write("All students")
st.dataframe(df)

st.write(f"Total: {len(df)} students")


# Apply filters
filtered = df

if branch != "All":
    filtered = filtered[filtered["branch"] == branch]

if city != "All":
    filtered = filtered[filtered["city"] == city]

filtered = filtered[
    (filtered["marks"] >= low) &
    (filtered["marks"] <= high)
]

if search:
    filtered = filtered[
        filtered["name"].str.contains(
            search,
            case=False,
            na=False
        )
    ]


# Show filtered students
st.write(f"Filtered: {len(filtered)} students")
st.dataframe(filtered)


# Statistics
if len(filtered) > 0:
    average_col, highest_col, lowest_col = st.columns(3)

    average_col.metric(
        label="Average",
        value=f"{filtered['marks'].mean():.1f}"
    )

    highest_col.metric(
        label="Highest",
        value=f"{filtered['marks'].max()}"
    )

    lowest_col.metric(
        label="Lowest",
        value=f"{filtered['marks'].min()}"
    )

else:
    st.warning(
        "No students match these filters. "
        "Widen the range or clear the search."
    )
