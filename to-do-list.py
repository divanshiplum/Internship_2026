import streamlit as st
from datetime import date

# ==================================================
# PAGE CONFIG
# ==================================================

st.set_page_config(
    page_title="My To-Do List",
    page_icon="✅",
    layout="wide"
)


# ==================================================
# CUSTOM CSS
# ==================================================

st.markdown("""
<style>

.main {
    background-color: #f5f7fb;
}

.title {
    text-align: center;
    font-size: 45px;
    font-weight: bold;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    color: #666;
    margin-bottom: 30px;
}

div.stButton > button {
    border-radius: 8px;
    font-weight: 600;
}

</style>
""", unsafe_allow_html=True)


# ==================================================
# SESSION STATE
# ==================================================

if "tasks" not in st.session_state:
    st.session_state.tasks = []


# ==================================================
# TITLE
# ==================================================

st.markdown(
    '<div class="title">✅ My To-Do List</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Organize your tasks and stay productive 🚀</div>',
    unsafe_allow_html=True
)


# ==================================================
# ADD NEW TASK
# ==================================================

st.header("➕ Add New Task")

# Create two equal columns
left_col, right_col = st.columns(2)


# ==================================================
# LEFT COLUMN
# ==================================================

with left_col:

    # ---------------- TASK NAME ----------------

    task_name = st.text_input(
        "📝 Task Name",
        placeholder="Enter task..."
    )


    # ---------------- CATEGORY ----------------

    category = st.selectbox(
        "📂 Category",
        [
            "Personal",
            "Work",
            "Study",
            "Shopping",
            "Fitness",
            "Other"
        ]
    )


    # ---------------- DUE DATE ----------------

    task_date = st.date_input(
        "📅 Due Date",
        value=date.today()
    )


# ==================================================
# RIGHT COLUMN
# ==================================================

with right_col:

    # ---------------- DUE TIME ----------------

    st.write("⏰ Due Time")

    time_col1, time_col2, time_col3 = st.columns(3)

    with time_col1:
        hour = st.selectbox(
            "Hour",
            list(range(1, 13)),
            key="hour"
        )

    with time_col2:
        minute = st.selectbox(
            "Minute",
            [f"{i:02d}" for i in range(0, 60, 5)],
            key="minute"
        )

    with time_col3:
        am_pm = st.selectbox(
            "AM / PM",
            ["AM", "PM"],
            key="am_pm"
        )

    task_time = f"{hour}:{minute} {am_pm}"


    # ---------------- PRIORITY ----------------

    priority = st.selectbox(
        "🔥 Priority",
        [
            "Low",
            "Medium",
            "High"
        ]
    )


    # ---------------- INITIAL PROGRESS ----------------

    progress = st.slider(
        "📈 Initial Progress",
        min_value=0,
        max_value=100,
        value=0,
        step=10
    )


# ==================================================
# DESCRIPTION
# ==================================================

description = st.text_area(
    "🗒️ Task Description",
    placeholder="Write some details about the task..."
)


# ==================================================
# COMPLETED CHECKBOX
# ==================================================

completed = st.checkbox(
    "☑️ Mark task as completed"
)


# ==================================================
# ADD TASK BUTTON
# ==================================================

if st.button(
    "➕ Add Task",
    use_container_width=True
):

    if task_name.strip() == "":
        st.warning("⚠️ Please enter a task name.")

    else:

        new_task = {
            "name": task_name,
            "category": category,
            "date": task_date,
            "time": task_time,
            "priority": priority,
            "progress": 100 if completed else progress,
            "description": description,
            "completed": completed
        }

        st.session_state.tasks.append(new_task)

        st.success("✅ Task added successfully!")

        st.rerun()


# ==================================================
# STATISTICS
# ==================================================

st.divider()

st.header("📊 Task Statistics")

total_tasks = len(st.session_state.tasks)

completed_tasks = sum(
    task["completed"]
    for task in st.session_state.tasks
)

pending_tasks = total_tasks - completed_tasks


col1, col2, col3 = st.columns(3)


with col1:

    st.metric(
        "📋 Total Tasks",
        total_tasks
    )


with col2:

    st.metric(
        "✅ Completed",
        completed_tasks
    )


with col3:

    st.metric(
        "⏳ Pending",
        pending_tasks
    )


# ==================================================
# SEARCH & FILTER
# ==================================================

st.divider()

st.header("🔍 Search & Filter")

col1, col2 = st.columns(2)


with col1:

    search = st.text_input(
        "🔎 Search Task",
        placeholder="Search by task name..."
    )


with col2:

    filter_category = st.selectbox(
        "📂 Filter by Category",
        [
            "All",
            "Personal",
            "Work",
            "Study",
            "Shopping",
            "Fitness",
            "Other"
        ]
    )


# ==================================================
# DISPLAY TASKS
# ==================================================

st.divider()

st.header("📋 My Tasks")


if len(st.session_state.tasks) == 0:

    st.info(
        "📭 No tasks available. Add your first task above!"
    )

else:

    found_task = False

    for index, task in enumerate(st.session_state.tasks):

        # Search filter
        if search.lower() not in task["name"].lower():
            continue

        # Category filter
        if (
            filter_category != "All"
            and task["category"] != filter_category
        ):
            continue

        found_task = True

        # ==================================================
        # TASK EXPANDER
        # ==================================================

        status_icon = "✅" if task["completed"] else "⏳"

        with st.expander(
            f"{status_icon} {task['name']} — {task['priority']} Priority"
        ):

            col1, col2 = st.columns(2)


            # ---------------- TASK INFORMATION ----------------

            with col1:

                st.write(
                    f"**📂 Category:** {task['category']}"
                )

                st.write(
                    f"**📅 Due Date:** {task['date']}"
                )

                st.write(
                    f"**⏰ Due Time:** {task['time']}"
                )

                st.write(
                    f"**🔥 Priority:** {task['priority']}"
                )


            # ---------------- PROGRESS ----------------

            with col2:

                st.write("**📈 Progress**")

                st.progress(
                    task["progress"] / 100
                )

                st.write(
                    f"{task['progress']}% completed"
                )

                if task["description"]:

                    st.write(
                        f"**📝 Description:** "
                        f"{task['description']}"
                    )

                else:

                    st.write(
                        "**📝 Description:** No description"
                    )


            st.divider()


            # ==================================================
            # TASK BUTTONS
            # ==================================================

            button1, button2, button3 = st.columns(3)


            # ---------------- COMPLETE ----------------

            with button1:

                if st.button(
                    "☑️ Complete",
                    key=f"complete_{index}",
                    use_container_width=True
                ):

                    st.session_state.tasks[index]["completed"] = True

                    st.session_state.tasks[index]["progress"] = 100

                    st.rerun()


            # ---------------- RESET ----------------

            with button2:

                if st.button(
                    "🔄 Reset",
                    key=f"reset_{index}",
                    use_container_width=True
                ):

                    st.session_state.tasks[index]["completed"] = False

                    st.session_state.tasks[index]["progress"] = 0

                    st.rerun()


            # ---------------- DELETE ----------------

            with button3:

                if st.button(
                    "🗑️ Delete",
                    key=f"delete_{index}",
                    use_container_width=True
                ):

                    st.session_state.tasks.pop(index)

                    st.rerun()


    # ==================================================
    # NO SEARCH RESULTS
    # ==================================================

    if not found_task:

        st.warning(
            "🔍 No tasks found matching your search/filter."
        )


# ==================================================
# FOOTER
# ==================================================

st.divider()

st.caption(
    "Made with ❤️ using Python & Streamlit"
)