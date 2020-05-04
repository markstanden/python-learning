##Learning Python the Hard Way
##Exercise 19
##Functions and Variables

def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses")
    print(f"You have {boxes_of_crackers} boxes of crackers")
    print("That's enough for a party")
    print("Get a blanket.\n")

print("We can give the function numbers directly")
cheese_and_crackers(20,20)

print("Or we can use numbers from our script:")
amount_of_cheese = 30
amount_of_crackers = 20
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("we can do math in the function call:")
cheese_and_crackers(10+10, 20+20)

print("we can use variables and maths combined")
x = 10
y = 20
cheese_and_crackers(x+2, y+5)


