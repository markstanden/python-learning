#create a string to convert
phrase_string = input("Enter phrase to convert: ")

#create a blank list
phrase_list = []

#iterate the string, each time adding the letter to a new item in the list
for i in phrase_string.lower():
    phrase_list.append(i)

#print both as a check
#print(phrase_string)
#print(phrase_list)

#Sort the list
phrase_list.sort()
#and display
print(phrase_list)

##second task was to take the output and create a new word:
new_word = input("What word can you spell from these letters?: ")
new_word_list = []

#iterate the word
for i in new_word.lower():
    for j in phrase_list:
        if i == j:
            phrase_list.remove(i)
            new_word_list.append(i)
            
print(f"Remaining Letters: {phrase_list}")
print(f"New Word (as a raw list): {new_word_list}")

new_word_from_list = ""
for i in new_word_list:
    new_word_from_list += i

print(f"New word (as a string): {new_word_from_list}")