from sys import argv
import io

file_to_read = open(argv[1], "r")

#print(args)

def check_word(word_to_check, letter_dict):
    for i in word_to_check:
        #if i not in letter_dict:
        #    letter_dict[i] = 0
        letter_dict.setdefault(i, 0)
        letter_dict[i] += 1
    
    return (letter_dict)

def display_dict (dict_to_display, order):
    print("After an extensive search...")
    
    if order == "key-alphabetical" or order == "ka":
        for i in sorted(dict_to_display):
            if i in full_alphabet_and_numbers:
                print (f"I found {dict_to_display[i]} x {i}'s")

    elif order == "value-numerical-descending" or order == "vnd":
        for i in sorted(dict_to_display, key=dict_to_display.get, reverse = True):
            if i in full_alphabet_and_numbers:
                print (i)
        
        ##This works!
        #for i in sorted(dict_to_display, key=dict_to_display.get, reverse = True):
        #    if i in full_alphabet_and_numbers:
        #        print (i)
        
        
        ##The follwoing works ok!
        #for order_of_letters in sorted( dict_to_display, key = lambda i : dict_to_display[i], reverse=True ):
        #    if order_of_letters in full_alphabet_and_numbers:
        #        print(f"{dict_to_display[order_of_letters]} x {order_of_letters}")
    
    else:
        for i in dict_to_display:
            if i in full_alphabet_and_numbers:
                print (f"I found {dict_to_display[i]} x {i}'s")

    print("... and nothing else.")

#initialise an empty dict & word counter variable
alphabet_dict = {}
word_count = 0
spaces = [" ", "\n", "_"]
full_alphabet_and_numbers = set("abcdefghijklmnopqrstuvwxyz0123456789")

print(f"Ok, I'll check your file: \n{argv[1]}\n for words and letters, and let you know")

for character in file_to_read.read():
    if character in spaces:
        #print(character)
        word_count += 1
        
    alphabet_dict = check_word( character.lower(), alphabet_dict )

#display_dict (alphabet_dict, "key-alphabetical")
display_dict (alphabet_dict, "vnd")
print(f"Number of words: {word_count}!")
#if order_of_letters in full_alphabet_and_numbers: