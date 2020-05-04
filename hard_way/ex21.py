##Learning Python the Hard Way
##Exercise 21
##Fuctions can return something

def add(a, b):
    print(f"ADDING {a} + {b}")
    return a+b

def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a-b

def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a/b

def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a*b

print("Let's do some math with just functions!")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

#A puzzle for the extra credit:
print("Here is a puzzle.")

what=add(age, subtract(height, multiply(weight, divide(iq, 2))))
#25
#4500
#74-4500=-4426
#-4426+35 = -4391
guess=-4391
print("That becomes: ", what, "can you do it by hand?")
print(f"My guess: {guess}")
    

##study question
print(divide(add(24, 34), subtract(100, 1023)))
