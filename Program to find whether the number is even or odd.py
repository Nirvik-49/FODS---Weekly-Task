'''
Program takes a number as input from the user and displays whether the number is even or odd.
'''
# Function to check if a number is even or odd
def check_even_odd(number):
    if number % 2 == 0:
        return "even"
    else:
        return "odd"
    
# Input from user
num = int(input("Enter a number: "))

# Check if the number is even or odd and store result
result = check_even_odd(num)

# Display output
print(f"\nThe number {num} is {result}.")




