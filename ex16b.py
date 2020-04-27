## Learn python 3 the hard way Ex16b
## Reading and Writing Files
## Study drills - can I write a read program without help?
## Update - fucking right i can.

##start with the argv module
from sys import argv

#assign variables
script, argument1 = argv
#I like doing this, rather than shortening the above, maybe i'm just wasting time?
filename = argument1

#open the file (taking a punt at read only)
file = open(filename, "r")

#read the contents of the file
file_contents = file.read()

#display the contents to screen
print(file_contents)

#close the file
file.close()

