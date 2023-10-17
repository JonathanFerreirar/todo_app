import PySimpleGUI as sg

label1 = sg.Text("Select files to compress: ")
input1 = sg.Input()
chose_button1 = sg.FileBrowse("Choose")

label2 = sg.Text("Select destination folder: ")
input2 = sg.Input()
chose_button2 = sg.FolderBrowse("Choose")

compress_button = sg.Button("Compressor")

window = sg.Window("File Compressor", layout=[
    [label1, input1, chose_button1],
    [label2, input2, chose_button2],
    [compress_button]
])

window.read()
window.close()

# label1 = sg.Text("Enter feet")
# label2 = sg.Text("Enter inches")
#
# input1 = sg.InputText()
# input2 = sg.InputText()
#
# button = sg.Button("Convert")
#
# window = sg.Window("Converto", layout=[
#     [label1, input1],
#     [label2, input2],
#     [button]
# ])
#
# window.read()
# window.close()
