'''
Program calculates the expression a^7 + 5a^3b^2c^6 + b^7 by taking inputs for variables a, b, and c.
'''
# Function to calculate the expression
def calculate_expression(a, b, c):
    return a**7 + 5*a**3*b**2*c**6 + b**7

# Input from user
a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))
c = float(input("Enter the value of c: "))

# Calculate the expression
result = calculate_expression(a, b, c)

# Display output of the program
print(f"\nThe result of a^7 + 5a^3b^2c^6 + b^7 where a = {a}, b = {b}, and c = {c} is: {result}")
