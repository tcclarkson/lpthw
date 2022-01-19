# sets number of cars
cars = 100
# sets number of seats in one vehicle
space_in_a_car = 4
# number of available drivers
drivers = 30
# number of total passengers
passengers = 90
# cars that don't have drivers
cars_not_driven = cars - drivers
# cars that do have drivers
cars_driven = drivers
# total seats
carpool_capacity = cars_driven * space_in_a_car
# how many per car
average_passengers_per_car = passengers / cars_driven


print("There are", cars, "cars_available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car,
      "in each car.")
