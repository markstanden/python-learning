## Learn Python the hard way - ex 8
## Printing, Printing

#creates a string that has placeholders for other strings/variables etc
formatter = "{} {} {} {}"

#prints to stdout the formatter placeholder string, with the four (arguments?) integers 1,2,3,4
print (formatter.format(1, 2, 3, 4))

#prints the four strings, filling the placeholder string formatter
print (formatter.format("one", "two", "three", "four"))

#fills placeholder with booleans
print (formatter.format(True, False, False, True))

#fills the placeholder with more placeholders... I guess this will be empty
print (formatter.format(formatter, formatter, formatter, formatter)) #actually fills this with curly brackets

#fill with user text over multiple lines
print (formatter.format(
        "he wants me to fill these strings",
        "with my own text",
        "I'll do my best",
        "but I have limited imagination"
       ))
       
#fills the placeholder with more placeholders... just let me check something myself
print (formatter.format(formatter.format(1, 2, 3, 4), formatter, formatter, formatter))
print (formatter)
