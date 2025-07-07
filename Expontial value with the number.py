'''
Program takes a number and an exponent as input from the user and displays the result of raising the number to the exponent.
'''

# Function to calculate the exponent value
def calculate_exponent(base, exponent):
    return base ** exponent

# Input from user
base = float(input("Enter the base number: "))
exponent = float(input("Enter the exponent: "))

# Calculate the exponent value and store result
result = calculate_exponent(base, exponent)

# Display output of the program
print(f"\nThe result of {base} raised to the power of {exponent} is: {result}")
