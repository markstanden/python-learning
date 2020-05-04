## Learn python 3 the hard way Ex15
## Reading Files

from sys import argv
script, filename = argv

#open filename provided as argument, create file object, fill it.
txt = open(filename)

#display the caught argument
print(f"Here's your file {filename}:")

#read the text from the file, pass to print
print(txt.read())

#text to describe what is required from prompt below
print("type the filename again:")
#prompt to fill the string with a filename
file_again = input("> ")

#create a file object called txt_again, fill it with typed file at prompt
txt_again = open(file_again)

#read contents of file, pass string to print to display on screen.
print(txt_again.read())

