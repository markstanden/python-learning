##Learning Python the Hard Way
##Exercise 32
##Loops and Lists

the_count = [1, 2, 3, 4, 5]
fruits = ["apples", "oranges", "pears", "apricots"]
change = [1, "pennies", 2, "10 pence", 3, "20 pence"]

for number in the_count:
    print(f"this is count {number}")

for fruit in fruits:
    print(f"Same as above: {fruit}")

for i in change:
    print(f"I got {i}")

#elements = []
#for i in range(0, 6):
#    print(f"adding {i} to the list")
#    elements.append(i)
elements = range(0, 10)
print (fruits.index("pears"))
print(elements)
print ("or individually:")
count = 1
for x in elements:
    print(f"\nItem {count}: {x}")
    count += 1

