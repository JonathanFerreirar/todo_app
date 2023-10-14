import glob
import csv
import shutil
import webbrowser

# With this module you find a file by his extension
myfiles = glob.glob("filetest/*.txt")

for filepath in myfiles:
    with open(filepath) as file:
        pass
#       print(file.read())


# csv file
with open("weather.csv") as csvFiles:
    data = list(csv.reader(csvFiles))

#    print(data)

# shutil → This library create files, in wished format

shutil.make_archive("output", "zip", "filetest")

# webbrowser
user_term = input("enter a search term: ")

webbrowser.open("https://google.com/search?q=" + user_term)
