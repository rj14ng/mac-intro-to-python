# Quadratic equation calculator

# Instructions
print("Enter your quadratic equation in the form ax^2 + bx + c.")

# Inputs
a = int(input("Coefficient of a: "))
b = int(input("Coefficient of b: "))
c = int(input("Coefficient of c: "))

# Calculate discriminant
discriminant = b ** 2 - 4 * a * c

# Calculate
if discriminant < 0:
    print("No real solutions.")
elif discriminant == 0:
    x = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    print("One real solution:", x)
else:
    x1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    x2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    print("Two real solutions:", x1, "or", x2)
