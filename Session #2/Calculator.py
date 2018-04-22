# Simple calculator

# Print instructions
print("Select your operation.")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

# Asks user for choice
choice = int(input("Enter choice (1/2/3/4): "))

# Asks user for two numbers
num_1 = int(input("Enter first number: "))
num_2 = int(input("Enter second number: "))

# Calculate
if choice == 1:  # Addition
    print(num_1, "+", num_2, "=", num_1 + num_2)
elif choice == 2:  # Subtraction
    print(num_1, "-", num_2, "=", num_1 - num_2)
elif choice == 3:  # Multiplication
    print(num_1, "*", num_2, "=", num_1 * num_2)
elif choice == 4:  # Division
    print(num_1, "/", num_2, "=", num_1 / num_2)
else:  # If choice is not 1, 2, 3 or 4, that means it is an invalid input
    print("Invalid input.")
