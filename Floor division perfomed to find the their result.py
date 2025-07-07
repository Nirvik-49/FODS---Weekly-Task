'''
Program takes two numbers as input from the user and displays the result of their floor division.
'''
# Function to perform floor division
def floor_divide_numbers(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a // b

# Input from user
num1 = float(input("Enter the numerator (first number): "))
num2 = float(input("Enter the denominator (second number): "))

# Perform floor division and store result
result = floor_divide_numbers(num1, num2)

# Display output
print(f"\nThe result of floor dividing {num1} by {num2} is: {result}")
