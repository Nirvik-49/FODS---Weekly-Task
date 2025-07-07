'''
Program calculates the expression a² + 2ab + b² by taking inputs for variables a and b.
'''
# Function to calculate the expression
def calculate_expression(a, b):
    return a**2 + 2*a*b + b**2

# Input from user
a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))

# Calculate the expression
result = calculate_expression(a, b)

# Display output
print(f"\nThe result of a² + 2ab + b² where a = {a} and b = {b} is: {result}")
