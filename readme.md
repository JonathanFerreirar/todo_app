##How handle with textfile in python

###Create a .txt file

Use the open() funtion to open the file write ou read that,
see the example bellow:

###file = open('todos.txt', 'r') -> This method go to the file in
the path and open it on read mode

####todos = file.readlines() -> Now your are really reading the content

file.close() -> Don't forget to closer the connection if the txt file

###file = open('todos.txt', 'w') -> This method go to the file in
the path and open it on write mode

####file.writelines(todos) -> Now you are really writing the file and
creating a new content for it

file.close() -> As usual, don't forget to close the connection with the data
base

Q1: How can we have more structured layouts using PySimpleGUI?

A: For more structured layouts, you can use sg.Column to create column instances. Here is an example:

import PySimpleGUI as sg

# Prepare the widgets for the left column

left_column_content = [[sg.Text('Left 1')],
[sg.Text('Left 2')]]

# Prepare the widgets for the right column

right_column_content = [[sg.Text('Right 1')],
[sg.Text('Right 2')]]

# Construct the Column widgets

left_column = sg.Column(left_column_content)
right_column = sg.Column(right_column_content)

# Construct the layout

layout = [[left_column, right_column]]

# Construct and display the window

window = sg.Window('Columns', layout)
window.read()
window.close()
