def uppercase_and_reverse (forwards):
    ## Too easy?
    # return forwards[::-1].upper()

    reversed = ''
    for letter in forwards.upper():
        reversed = letter + reversed
    return reversed

print(uppercase_and_reverse('banana'))