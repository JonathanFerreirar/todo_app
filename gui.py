import PySimpleGUI as sg

from functions import get_todos, write_todos

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo")
add_button = sg.Button("Add")

window = sg.Window('To-do App', layout=[[[label], [input_box, add_button]]])

window.read()
window.close()
