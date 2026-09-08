import math # Imports math library

# User inputs the length of both legs
a = float(input("Enter the length for side a: "))
b = float(input("Enter the length for side b: "))

# The hypotenuse then gets calculated using the standard pythagorean formula
c = math.sqrt(math.pow(a, 2) + math.pow(b, 2))

# Outputs the hypotenuse length
print(f"The hypotenuse is: {c:.2f}")
