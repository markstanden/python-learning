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