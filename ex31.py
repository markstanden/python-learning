##Learning Python the Hard Way
##Exercise 31
##Making Decisions

prompt = "-->"

print("""You enter a dark room with two doors,
Do you go through door #1 or door #2?""")

door = input(prompt)

if door == "1":
    print("There's a giant bear here eating a cheese cake.")
    print("What do you do?")
    print("1. Take the Cake")
    print("2. Scream at the Bear")
    
    bear = input(prompt)
    
    if bear == "1":
        print("The hungry bear eats you - Good Job")
    elif bear == "2":
        print("The bear eats your legs - Good Job")
    else:
        print(f"Well doing {bear} is probably the better choice")
        print("The bear runs away")

elif door == "2":
    print("You stare into the endless abyss at Cthulhu's retina")
    print("""1. Blueberries
2. Yellow Jacket clothespins
3. Understanding revolvers yelling melodies.""")
    
    insanity = input(prompt)
    
    if insanity == "1" or insanity == "2":
        print("your body survives powered by a mind of jelly")
        print("Good Job")
    else:
        print("The insanity rots your eyes into a pool of muck")
        print("Good Job")

else:
    print("You stumble around and fall onto a knife and die.  Good Job.")
