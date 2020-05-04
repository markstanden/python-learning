## Learn python 3 the hard way Ex11
## Inputs

#print("How old are you?", end = ' ')
#age = input()
#print("How tall are you?", end = ' ' )
#height = input()
#print("How much do you weigh?", end  = ' ')
#weight = input()

#print(f"So, you're {age} old, {height} tall and {weight} heavy.")

name = input ("What is your name? ")
spouse = input ("What is your spouses' name? ")
print (f"Pass this to {spouse}, and press return")
input()
#print (f"Hi {spouse}, {name} is feeling sexy...")
print("Hi {}, {} is feeling sexy".format(spouse, name))


