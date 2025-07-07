'''
Program calculates the expression a^5 + 2abc + b^3 + c^4 by taking inputs for variables a, b, and c.
'''
# Function to calculate the expression
def calculate_expression(a, b, c):
    return a**5 + 2*a*b*c + b**3 + c**4

# Input from user
a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))
c = float(input("Enter the value of c: "))

# Calculate the expression
result = calculate_expression(a, b, c)

# Display output
print(f"\nThe result of a^5 + 2abc + b^3 + c^4 where a = {a}, b = {b}, and c = {c} is: {result}")
