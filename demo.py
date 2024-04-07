import streamlit as st

def main():
    st.title("Task Todo List")

    # Initialize columns
    column_names = ["To-Do", "In Progress", "Done"]
    column1, column2, column3 = st.sidebar.columns(3)

    # Get user-defined column names
    with column1:
        todo_name = st.text_input("To-Do Column Name", value="To-Do")
    with column2:
        in_progress_name = st.text_input("In Progress Column Name", value="In Progress")
    with column3:
        done_name = st.text_input("Done Column Name", value="Done")

    # Initialize tasks
    tasks = {
        todo_name: [],
        in_progress_name: [],
        done_name: []
    }

    # Add task function
    def add_task(task, status):
        tasks[status].append(task)

    # Task input
    task = st.text_input("Add Task")
    status = st.selectbox("Status", [todo_name, in_progress_name, done_name])

    # Add task button
    if st.button("Add Task"):
        add_task(task, status)

    # Display previous tasks
    st.write("## Previous Tasks:")
    for column_name, column_tasks in tasks.items():
        st.write(f"### {column_name}:")
        st.write(column_tasks)

if __name__ == "__main__":
    main()
