print ("Hello World")
print ("Hello again")
print ("I like typing this")
print ("This is fun")
print ('Yay! printing.')
print ("I'd much rather 'not'.")
print ('I "said" do not touch this.')

#Bootcamp examples. string work
my_dog = "Hodor"
print (len (my_dog))
print (my_dog[0])

#slicing
mystring = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#returns 3rd char all the way to the end
print (mystring[2:])
#returns beginningof string up to 3rd char (not including 4th [3])
print (mystring[:3])
#displays whole string
print (mystring[:3]+mystring[3:])
#attempt to grab KLM
print (mystring[10:12])
#got me with the upto stop, not including
print(mystring[10:13])
#print whole string (with a step size of 1)
print (mystring[::])
#or
print (mystring[::1])
# step size of 2
print (mystring[::2])
# step size of 3
print (mystring[::3])
# step size of -1 will quickly reverse the string
print (mystring[::-1])

#quick task to make "Sam" into "Pam"
name = "Sam"
desiredname = "Pam"
print (name + " to " + desiredname)
print (name)
name2 = desiredname[0] + name[1:]
name = name2
print (name)

stringtoplaywith = ("Humpty Dumpty sat on wall, Humpty Dumpty had a great fall.")
print (stringtoplaywith)
#splits string into a list, defaults at whitespace
print (stringtoplaywith.split())
#can use any char though
print (stringtoplaywith.split('u'))
#sends the uppercase version of the string to the function, string remains as defined.
print (stringtoplaywith.upper())
print (stringtoplaywith.lower())
print (stringtoplaywith)
#convert string to uppercase
stringtoplaywith = stringtoplaywith.upper()
print (stringtoplaywith)


## Hard Way ex3.py
print ("I will now count my chickens")

print ("Hens", 25+30/6)
print ("Roosters", 100 - 25 * 3 % 4)

print ("Now I will count the eggs:")
print (3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6)

print ("Is it true that 3 + 2 < 5 - 7?")
print (3 + 2 < 5 -7)

print ("What is 3+2?", 3+2)
print ("what is 5-7?", 5-7)

print ("Oh, That's why it's false.")
print ("How about some more.")

print ("is it greater", 5 > -2)
print("Is it greater than or equal?", 5 >= -2)
print ("Is it less than or equal?", 5 <= -2)

## Hard Way ex3.py now with floats
print ("I will now count my chickens")

print ("Hens", 25.0+30.0/6.0)
print ("Roosters", 100.0 - 25.0 * 3.0 % 4.0)

print ("Now I will count the eggs:")
print (3.0 + 2.0 + 1.0 - 5.0 + 4.0 % 2.0 - 1.0 / 4.0 + 6.0)

print ("Is it true that 3.0 + 2.0 < 5.0 - 7.0?")
print (3.0 + 2.0 < 5.0 -7.0)

print ("What is 3.0 + 2.0?", 3.0+2.0)
print ("what is 5.0 - 7.0?", 5.0-7.0)

print ("Oh, That's why it's false.")
print ("How about some more.")

print ("is it greater", 5.0 > -2.0)
print("Is it greater than or equal?", 5.0 >= -2.0)
print ("Is it less than or equal?", 5.0 <= -2.0)

#calculate the percentage of space occupied by earth from krypton

#surface area of a sphere is 4*pi*(radius**2)
pi = 3.14147
#speed of debris from supernova was clocked at 8 miles per second
debris_speed = 8 * 1600 #metres per second
#father claimed he would be a thousand earth years old
time_of_travel = 1000 * 365 * 24 * 60 * 60 # 1000 years * 365 Days * 24 Hours * 60 Mins * 60 Seconds
#distance (in metres)
radius = debris_speed * time_of_travel
print("Distance from Krytpon to Earth ", radius, "m")

#surface area that debris would be scattered over
sa_debris = 4 * pi * (radius**2)
print("Surface Area of debris after 1000 years", sa_debris, "m2")

rad_earth = 6371000 #radius of earth in metres
print("Radius of Earth", rad_earth, "m")
sa_earth = pi * (rad_earth**2)
print("Surface Area of the Earth ", sa_earth, "m2")

print("percentage of the debris sphere occupied by Earth", (sa_earth/sa_debris)/100, "%")

