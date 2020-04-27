#Total number of cars available
cars = 100

#Total number of seats in the car, excluding the driver
space_in_a_car = 4

#Number of Drivers
drivers = 30

#Number of Passengers
passengers = 90

#Idle cars that can't be driven due to lack of a driver
cars_not_driven = cars - drivers

#Cars that can be driven because we have a driver for them
cars_driven = drivers

#Maximum number of passengers that can be transported
carpool_capacity = cars_driven * space_in_a_car

#Average number of passengers per car
average_passengers_per_car = passengers / cars_driven


print("There are", cars, "cars available")
print("There are only", drivers, "drivers available")
print("There will be", cars_not_driven, "empty cars today")
print("We can transport", carpool_capacity, "people today")
print("We have", passengers, "to carpool today")
print("We need to put about", average_passengers_per_car,
            "in each car")
