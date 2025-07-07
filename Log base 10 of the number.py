'''
Program takes a number as input from the user and displays the logarithm base 10 of that number.
'''

import math  # Importing the built-in math module to use the log10 function

# Function to calculate the logarithm base 10 of a number
def calculate_log_base_10(number):
    if number <= 0:
        return "Error: Logarithm is not defined for non-positive numbers."
    return math.log10(number)

# Input from user
num = float(input("Enter a number: "))

# Calculate the logarithm base 10 and store result
result = calculate_log_base_10(num)

# Display output of the program
print(f"\nThe logarithm base 10 of {num} is: {result}")
