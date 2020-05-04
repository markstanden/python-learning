vowels = ["a", "e", "i", "o", "u"]
word_to_check = input ("What word would you like to check for vowels? :")
found_vowels=[]

for letter in word_to_check:
    if letter in vowels and letter not in found_vowels:
        found_vowels.append(letter)
        
found_vowels.sort()
print(found_vowels)
