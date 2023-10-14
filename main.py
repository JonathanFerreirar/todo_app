from termcolor import colored
import time

from functions import get_todos, write_todos, clear_console

now = time.strftime("%d/%b - ")

colors = {
    'system': '',
    'data': 'blue',
    'warning': 'red',
    'text': 'white'
}

QUESTION_MESSAGE = colored("Type add, list, edit, done, clear or  exit: ", 'light_cyan', attrs=['bold'])
ERROR_MESSAGE = colored("Your command is not válid", colors['warning'], attrs=['bold'])
THERE_IS_NO_ITEM = colored("There is no item with that number", colors['warning'], attrs=['bold'])
EMPTY_TODO = colored("There is no item", colors['warning'], attrs=['bold'])

while True:
    user_action = input(QUESTION_MESSAGE).strip()

    if user_action.startswith("add"):
        todo = user_action[4:] + "\n"

        todos: list[str] = get_todos()

        todos.append(now + todo)

        write_todos(todos)

    elif user_action.startswith("show") or user_action.startswith("list"):
        data = user_action[5:]

        todos: list[str] = get_todos()

        if not todos:
            print(EMPTY_TODO)
        else:
            todos.sort(reverse=True)

            # list comprehensions in Python
            new_todos = [item.strip('\n') for item in todos]
            for index, todo in enumerate(new_todos):
                new_todo = todo.split('-')
                if data:
                    if todo.find(data) != -1:
                        print(colored(f"{index + 1} - {new_todo[0]}", colors['data'], attrs=['bold']) + colored(
                            f"{new_todo[1]}", colors['text'],
                            attrs=['bold']))

                else:

                    print(
                        colored(f"{index + 1} - {new_todo[0]}", colors['data'], attrs=['bold']) + colored(
                            f"{new_todo[1]}", colors['text'],
                            attrs=['bold']))

    elif user_action.startswith("edit"):
        try:
            number: int = int(user_action[5:])

            todos: list[str] = get_todos()
            todos.sort(reverse=True)

            if number <= len(todos):
                new_todo = input("Enter new todo: ")
                todos[number - 1] = now + new_todo + '\n'

                write_todos(todos)
            else:
                print(THERE_IS_NO_ITEM)
        except ValueError:
            print(ERROR_MESSAGE)
            continue

    elif user_action.startswith("done") or user_action.startswith("completed"):
        try:
            number: int = int(user_action[5:])

            todos: list[str] = get_todos()
            todos.sort(reverse=True)

            if number <= len(todos):

                todo_to_remove = todos.pop(number - 1).strip('\n')

                print(
                    colored(f"{todo_to_remove}", colors['warning'], attrs=['bold']) + colored(f" was removed",
                                                                                              colors['text'],
                                                                                              attrs=['bold']))

                write_todos(todos)
            else:
                print(THERE_IS_NO_ITEM)
        except ValueError:
            print(ERROR_MESSAGE)
            continue

    elif 'clear' in user_action:
        clear_console()

    elif 'exit' in user_action:
        clear_console()
        break
    else:
        print(ERROR_MESSAGE)
