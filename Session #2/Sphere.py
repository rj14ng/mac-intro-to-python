# Sphere volume/surface area calculator
# Does not use math module for pi since we haven't discussed that yet

# Define pi
pi = 3.14159

# Instructions
print("This calculator will calculate the volume or surface area of a sphere.")

# Inputs
choice = int(input("Calculate volume (1) or surface area (2): "))
radius = int(input("Please input the radius of the sphere: "))

# Calculate
if choice == 1:  # Volume
    volume = 4 / 3 * pi * radius ** 3
    print("The volume is", volume)
elif choice == 2:  # Surface area
    surface_area = 4 * pi * radius ** 2
    print("The surface area is", surface_area)
else:  # Invalid input
    print("Invalid input.")
