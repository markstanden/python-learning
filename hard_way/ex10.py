## Learn Python the hard way - ex 10
## What was that?

# \t inserts a tab character
tabby_cat = "\tI'm tabbed in"
# \n inserts a new line character
persian_cat = "I'm split\non a line"
# \\ produces a \ within the string
backslash_cat = "I'm \\ a \\ cat."

# """ allows multi line string
fat_cat = """
I'll do a list:
\t* Cat Food
\t* Fishies
# Comment -Nope
\t* Catnip\n\t* Grass
"""

other_fat_cat = '''
I would use this for dialogue:


"\vHello"
\t"Why, Hello there!"
"\vHow do you do?"
\t"Well thank you"
'''

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)
print(other_fat_cat)
