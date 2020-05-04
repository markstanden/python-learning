##Learning Python the Hard Way
##Exercise 30
##Else and If

people = 30
cars = 20
trucks = 40

if cars > people:
    print("We should take the cars.")
elif cars < people:
    print("We should not take the cars.")
else:
    print("We cannot decide.")

if trucks > cars:
    print("That's too many trucks.")
elif trucks < cars:
    print("Maybe we could take the trucks?")
else:
    print("We still can't decide")

if people > trucks:
    print("Alright, let's just take the trucks.")
else:
    print("Ok, let's just stay home then")


