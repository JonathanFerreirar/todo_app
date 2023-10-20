import PySimpleGUI as sg

from functions import get_todos, write_todos
import time

sg.theme('DarkGrey7')
clock = sg.Text("", key='clock')
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button(image_source="add.png", mouseover_colors="LightBlue2", tooltip="Add a todo", key='Add')
list_box = sg.Listbox(values=get_todos(), key="todos",
                      enable_events=True, size=[45, 10])

edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

window = sg.Window('To-do App',
                   layout=[
                       [clock],
                       [label],
                       [input_box, add_button],
                       [list_box, edit_button, complete_button],
                       [exit_button]
                   ],
                   font=('Helvetica', 20))

while True:
    event, values = window.read(timeout=10)
    window["clock"].update(value=time.strftime("%b %d, %y %H:%M:%S"))

    match event:
        case "Add":
            todos = get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            write_todos(todos)
            window['todos'].update(todos)
            window['todo'].update(value='')

        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']
                todos = get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo + "\n"
                write_todos(todos)
                window['todos'].update(todos)
            except IndexError:
                sg.popup_error('Please select an item first.', font=("Helvetica", 20), title="EDIT_ERROR")

        case 'Complete':
            todo_to_complete = values['todos'][0]
            todos = get_todos()
            todos.remove(todo_to_complete)
            write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value='')
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case 'Exit':
            break

        case sg.WIN_CLOSED:
            break

window.close()
