from typing import NewType, Union


def get_todos(filepath: str = 'todos.txt'):
    with open(filepath) as files:
        todos_local: [str] = files.readlines()

    return todos_local


type_write = NewType("type_write", Union[str | list[str]])


def write_todos(argument: type_write, filepath: str = 'todos.txt'):
    with open(filepath, 'w') as files:
        files.writelines(argument)


while True:
    user_action = input("Type add, list, edit, done or exit: ").strip()

    if user_action.startswith("add"):
        todo = user_action[4:] + "\n"

        todos: list[str] = get_todos()

        todos.append(todo)

        write_todos(todos)

    elif user_action.startswith("show") or user_action.startswith("list"):

        todos: list[str] = get_todos()

        # list comprehensions in Python
        new_todos = [item.strip('\n') for item in todos]

        for index, todo in enumerate(new_todos):
            print(f"{index + 1}  - {todo}")

    elif user_action.startswith("edit"):
        try:
            number: int = int(user_action[5:])

            todos: list[str] = get_todos()

            if number <= len(todos):
                new_todo = input("Enter new todo: ")
                todos[number - 1] = new_todo + '\n'

                write_todos(todos)
            else:
                print("There is no item with that number")
        except ValueError:
            print("Your command is not válid")
            continue

    elif user_action.startswith("done") or user_action.startswith("completed"):
        try:
            number: int = int(user_action[5:])

            todos: list[str] = get_todos()

            if number <= len(todos):

                todo_to_remove = todos.pop(number - 1).strip('\n')

                print(f"'{todo_to_remove}' was removed from the list")

                write_todos(todos)
            else:
                print("There is no item with that number")
        except ValueError:
            print("Your command is not válid")
            continue

    elif 'exit' in user_action:
        break
    else:
        print("Your command is not válid")
