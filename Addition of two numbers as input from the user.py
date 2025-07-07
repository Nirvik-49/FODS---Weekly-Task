'''
Program takes two numbers as input from the user and displays the result of their addition.
'''
# Function to perform addition
def add_numbers(a, b):
    return a + b

# Input from user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Perform addition and store result
result = add_numbers(num1, num2)

# Display output
print(f"\nThe result of adding {num1} and {num2} is: {result}")
