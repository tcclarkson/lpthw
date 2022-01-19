name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
height_cm = int(round(height * 2.54, 0)) # height in cm
weight = 180 # lbs
weight_kg = round(weight / 2.205, 1) # weight in kg
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}.")
print(f"He's {height_cm} centimeters tall.")
print(f"He's {weight_kg} kilos heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"Hit teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height_cm + weight_kg
print(f"If I add {age}, {height_cm}, and {weight_kg} I get {total}.")
