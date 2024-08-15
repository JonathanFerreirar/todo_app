from functions import get_todos, write_todos
import time

now = time.strftime("%b %d, %y")

FILEPATH_DELETED = "deleted.txt"

while True:
    user_action = input("Type add, list, edit, done or exit: ").strip()

    if user_action.lower().startswith("add"):
        todo = user_action[4:].strip()
        todos: list[str] = get_todos()
        todos.append(f'{todo} - created: {now}\n')
        write_todos(todos)

    elif user_action.lower().startswith("list"):
        # Se o comando for "list done", apenas exiba os itens concluídos
        if 'done' in user_action.lower():
            todos: list[str] = get_todos(FILEPATH_DELETED)
        else:
            # Caso contrário, verifique se há um termo de busca
            search_term = user_action[5:].strip() if len(
                user_action) > 5 else ""
            todos: list[str] = get_todos()

            # Filtra os itens que contêm o termo de busca e mantém os índices originais
            filtered_todos = [(i + 1, todo) for i, todo in enumerate(todos)
                              if search_term.lower() in todo.lower()]

        # Exibe os itens da lista, mantendo as quebras de linha e mostrando o índice original
        if 'done' in user_action.lower():
            for index, todo in enumerate(todos):
                print(f"{index + 1} | {todo.strip()}")
        else:
            if filtered_todos:
                for original_index, todo in filtered_todos:
                    print(f"{original_index} | {todo.strip()}")
            else:
                print("No items match your search.")

    elif user_action.lower().startswith("edit"):
        try:
            number: int = int(user_action[5:].strip())
            todos: list[str] = get_todos()

            if 1 <= number <= len(todos):
                new_todo = input("Enter new todo: ").strip()
                todos[number - 1] = f'{new_todo} - created: {now}\n'
                write_todos(todos)
            else:
                print("There is no item with that number")
        except ValueError:
            print("Your command is not valid")
            continue

    elif user_action.lower().startswith("done") or user_action.lower().startswith("completed"):
        try:
            number: int = int(user_action[5:].strip())
            todos: list[str] = get_todos()
            deleted: list[str] = get_todos(FILEPATH_DELETED)

            if 1 <= number <= len(todos):
                todo_to_remove = todos.pop(number - 1).strip()
                todo_splited = todo_to_remove.split('-')[0].strip()
                deleted.append(f'{todo_splited} - removed: {now}\r')
                print(f"'{todo_to_remove}' was removed from the list")
                write_todos(todos)
                write_todos(deleted, FILEPATH_DELETED)
            else:
                print("There is no item with that number")
        except ValueError:
            print("Your command is not valid")
            continue

    elif 'exit' in user_action.lower():
        break

    else:
        print("Your command is not valid")
