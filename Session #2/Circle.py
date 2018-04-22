# Circle area/circumference calculator
# Does not use math module for pi since we haven't discussed that yet

# Define pi
pi = 3.14159

# Instructions
print("This calculator will calculate the area or circumference of a circle.")

# Inputs
choice = int(input("Calculate area (1) or circumference (2): "))
radius = int(input("Please input the radius of the circle: "))

# Calculate
if choice == 1:  # Area
    area = pi * radius ** 2
    print("The area is", area)
elif choice == 2:  # Circumference
    circumference = 2 * pi * radius
    print("The circumference is", circumference)
else:  # Invalid input
    print("Invalid input.")
