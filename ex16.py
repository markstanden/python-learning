## Learn python 3 the hard way Ex16
## Reading and Writing Files

from sys import argv
script, argument1 = argv

filename = argument1
prompt = "-->> "

print(type(filename))
print(f"We're going to erase {filename}.")
print("If you don't want to do that, hit CTRL-C now...")
print("If this is OK, hit RETURN")
input(prompt)

print("\n\nOpening the file ...")

#not sure what the 'w' is for (write permissions?)
target = open(filename, 'w')

#Just a confirmation of the object type of target, i'm expecting a file object, but we'll see what happens.
print(type(target))

##Erase current contents of the file
print("\nTruncating the file.  Goodbye file...!")
target.truncate()

#prompt for text to add to the file and fill string variables with the reply.
print("Now I'm going to ask you for three lines to write to the file.")
line1 = input("line1: ")
line2 = input("line2: ")
line3 = input("line3: ")

#Study drills want this written in one go, so creating a long string with new lines
multi_line_text = (line1 + "\n" + line2 + "\n" + line3 + "\n")
#obviously i could have just put (line1 + "\n" + line2 + "\n" + line3 + "\n") in the target.write brackets, but i like this way better.

#write the mega-string to the file
target.write(multi_line_text)

#close the file
print("\nAnd finally we close the file")
target.close()


