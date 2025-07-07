'''
Program calculates the factorial of a number taken as input from the user.
It validates the input to ensure it is a positive integer.
Check for error in the program.
'''

# Function to calculate factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result


# Input from user
user_input = input("Enter a positive integer to calculate its factorial: ")


# Validate input
if user_input.isdigit():
    number = int(user_input)
    if number < 0:
        print("Error: Please enter a positive integer.")
    else:
        # Calculate factorial
        fact = factorial(number)
        print(f"The factorial of {number} is: {fact}")
else:
    print("Error: Not a number.")

    
