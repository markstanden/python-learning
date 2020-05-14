#Mattan has asked for a list of the squares of the numbers 1-10

# ### The initial script could be condensed to the following 4 lines
# squares = []
#
# for num in range (1,11):
#     squares.append(num ** 2)
#
# #print(squares)

#for nice looking output
import pprint

#Initialise the range to allow for easy changes later
first_number = 1
last_number = 5

#create an empty list for initial numbers, and for the powers
single_numbers = list(range (first_number, (last_number + 1)))
square_numbers = []
cube_numbers = []
#not sure what these are actually called, but this will do
quad_numbers = []
quin_numbers = []

#create the initial numbers, note last_number + 1, as range stops BEFORE the number in the argument.
for number in single_numbers:
    square_numbers.append(number ** 2)
    cube_numbers.append(number ** 3)
    quad_numbers.append(number ** 4)
    quin_numbers.append(number ** 5)

#create a list to hold the list of powers
powers_list = [ single_numbers, 
                square_numbers, 
                cube_numbers, 
                quad_numbers, 
                quin_numbers ]

#print both to screen
pprint.pprint(powers_list)