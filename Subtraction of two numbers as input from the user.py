'''
Program takes two numbers as input from the user and displays the result of their subtraction.
'''

# Function to perform subtraction
def subtract_numbers(a, b):
    return a - b

# Input from user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Perform subtraction between two numbers
result = subtract_numbers(num1, num2)

# Display result 
print(f"\nThe result of subtracting {num2} from {num1} is: {result}")
