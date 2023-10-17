import PySimpleGUI as sg

from zip_create import make_archive

label1 = sg.Text("Select files to compress: ")
input1 = sg.Input()
chose_button1 = sg.FilesBrowse("Choose", key="files")

label2 = sg.Text("Select destination folder: ")
input2 = sg.Input()
chose_button2 = sg.FolderBrowse("Choose", key="folder")

compress_button = sg.Button("Compressor")
output_label = sg.Text(key="output")

window = sg.Window("File Compressor", layout=[
    [label1, input1, chose_button1],
    [label2, input2, chose_button2],
    [compress_button, output_label]
])

while True:
    event, values = window.read()
    filepaths = values["files"].split(';')
    folder = values["folder"]
    make_archive(filepaths, folder)
    window['output'].update(value='Compression completed!')

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
