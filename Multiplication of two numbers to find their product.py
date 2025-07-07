'''
Program takes two numbers as input from the user and displays their product.
'''
# Function to perform multiplication
def multiply_numbers(a, b):
    return a * b

# Input from user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Perform multiplication and store the result
result = multiply_numbers(num1, num2)

# Display output
print(f"\nThe product of {num1} and {num2} is: {result}")
