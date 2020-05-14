def break_words(text):
    """Breaks sentence into multiple words and returns a list of words"""
    words = text.split()
    #Strips preceding and trailing punctuation from words
    count = 0
    for word in words:
        to_strip = """ "',. """
        words[count] = word.strip(to_strip)
        count += 1
    return words

def count_words(words):
    """counts the number of words in a list and returns as int"""
    return len(words)

def sort_words(words):
    """Takes an unsorted list, returns alphabetically sorted list"""
    #key=str.casefold sorts the list disregarding case
    words.sort(key=str.casefold)
    return words

def sort_sentence(sentence):
    """Takes a sentence, breaks into individual words within a list, and returns a sorted list"""
    words = break_words(sentence)
    return sort_words(words)

def print_first_word(words):
    """Prints the first word after popping it off"""
    word = words.pop(0)
    print(word)

def print_last_word(words):
    """Prints the last word after popping it off"""
    word = words.pop(-1)
    print(word)

def print_first_and_last_word(sentence):
    """Prints the first and last words of the sentence"""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def sing(bottles):
    """Calls the relevant functions to print the bottles of beer song to the screen, argument is max number of bottles"""
    
    def print_verse(bottles):
        """prints the main verse of the song, takes the number of bottles on the wall"""
        print(bottles, "bottles of beer on the wall,", end=' ')
        print(bottles, "bottles of beer.")
        print("Take one down and pass it around,", end=' ')
        print(bottles - 1, "bottles of beer on the wall.\n")

    def print_last_bottle():
        """prints the last bottle of beer on the wall, doesn't need an argument"""
        print("1 bottle of beer on the wall,", end=' ')
        print("1 bottle of beer.")
        print("Take one down and pass it around,", end=' ')
        print("no more bottles of beer on the wall.\n")

    def print_last_two_bottles():
        """prints the last 2 bottles of beer on the wall, requires no argument"""
        print("2 bottles of beer on the wall,", end=' ')
        print("2 bottles of beer.")
        print("Take one down and pass it around,", end=' ')
        print("1 bottle of beer on the wall.\n")

    def print_last_verse():
        """prints no more beer on the wall, no argument required"""
        print("No more bottles of beer on the wall,", end=' ') 
        print("no more bottles of beer.")
        print("Go to the store and buy some more,", end=' ')
        print("99 bottles of beer on the wall.\n")

    for number in reversed(range(bottles + 1)):
        if number == 0:
            print_last_verse()
        elif number == 1:
            print_last_bottle()
        elif number == 2:
            print_last_two_bottles()
        else:
            print_verse(number)


##Joke
demitri_martin_joke = "I used to play sports. \n\t Then I realized you can buy trophies. Now I am good at everything."

print("\n----------")
print(demitri_martin_joke)
print("----------\n")


##Bottles of Beer
bottles_of_beer = 100 + 10 - 15 + 4
print("This should be ninety-nine:", bottles_of_beer)

sing(bottles_of_beer)


##Word play
sentence = "I think it's interesting that 'Cologne' rhymes with 'alone'."
words = break_words(sentence)
sorted_words = sort_sentence(sentence)

print( '"{}" has {} words'.format(sentence, count_words(words)) )
print( "The words are:", words )
print( "The sorted words are:", sorted_words )

print_first_word(words)
print_last_word(words)
print_first_and_last_word(sentence)