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
