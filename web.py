from functions import get_todos, write_todos
import streamlit as st

todos = get_todos()


def add_todo():
    todo_typed_by_user = st.session_state["new_todo"]
    todos.append(todo_typed_by_user + '\n')
    write_todos(todos)
    st.session_state["new_todo"] = ''


st.title("todo with Python")
st.subheader("This is my todo app")
st.write("This app is to improve your productivity")

for key, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=key)
    if checkbox:
        todos.pop(key)
        write_todos(todos)
        del st.session_state[key]
        st.experimental_rerun()

st.text_input(label="Enter a todo", placeholder="Add new todo...", on_change=add_todo, key="new_todo")
