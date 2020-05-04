##Learning Python the Hard Way
##Exercise 33
##While Loops

numbers=[]

def sequence (first_value, steps, size):
    i= 1
    number_list=[]
    #while i <= size:
    for i in range(0, size):
        #print(f"At the top i is {i}")
        current_value = first_value + (i * steps)
        number_list.append(current_value)
        #i += 1
        
        #print("Numbers now:", numbers)
        #print(f"At the bottom i is {i}")
    
    return number_list

initial_number = int( input("First Value: ") )
gaps_between = int( input("Step Size: ") )
number_of_entries = int( input("Size of List: ") )

numbers = sequence (initial_number, gaps_between, number_of_entries)
#print("The numbers:", numbers)

for num in numbers:
    print(num)
