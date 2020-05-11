#Get the word to check
word_to_parse = input("What word would you like to check for vowels? :").lower()

#create an zeroed dict
vowel_counter = {
                    "a" : 0,
                    "e" : 0,
                    "i" : 0,
                    "o" : 0,
                    "u" : 0 }

#iterate the word
for i in word_to_parse:
    #for every letter of the word, see if it is in the dict
    if i in vowel_counter:
        #if it is add 1
        vowel_counter[i] += 1

#display the dict in a nice way
print(f"Ok, I've run the word {word_to_parse} through my super secret algorithm, results as follows:")
for i in vowel_counter:
    print(f"{vowel_counter[i]} {i}'s")