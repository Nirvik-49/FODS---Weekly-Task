'''
Program takes a number as input from the user and displays the square root of that number.
'''
import math  # Importing the built-in math module to use the sqrt function

# Function to calculate the square root of a number

def calculate_square_root(number):
    if number < 0:
        return "Error: Cannot calculate the square root of a negative number."
    return math.sqrt(number)

# Input from user
num = float(input("Enter a number: "))

# Calculate the square root and store result
result = calculate_square_root(num)

# Display output of the program
print(f"\nThe square root of {num} is: {result}")


