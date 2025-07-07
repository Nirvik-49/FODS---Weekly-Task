'''
Program takes a number as input from the user and displays the square of that number.
'''
# Function to calculate the square of a number
def calculate_square(number):
    return number ** 2

# Input from user
num = float(input("Enter a number: "))

# Calculate the square and store result
result = calculate_square(num)

# Display output of the program
print(f"\nThe square of {num} is: {result}")


