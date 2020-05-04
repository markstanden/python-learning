##Ask for string to reverse
string_to_reverse = input("What word would you like me to reverse?\n -->>")

#create an empty string (needed to add empty section to the end of the first letter)
backwards_string = ""

#reads the string
for letters in string_to_reverse:
    #add each letter before previous letter
    backwards_string = letters + backwards_string
    
#display full word backwards
print(backwards_string)

#Pythonista way!
print (backwards_string[::-1])
#print (string_to_reverse[3:1:-1])
