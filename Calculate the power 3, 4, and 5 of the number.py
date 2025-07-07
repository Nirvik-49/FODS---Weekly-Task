'''
Program takes a number as input from the user
and displays the results of raising the number to the powers of 3, 4, and 5.
'''
# Function to calculate the powers of a number
def calculate_powers(number):
    power_3 = number ** 3
    power_4 = number ** 4
    power_5 = number ** 5
    return power_3, power_4, power_5

# Input from user
num = float(input("Enter a number: "))

# Calculate the powers and store results
power_3, power_4, power_5 = calculate_powers(num)

# Display output
print(f"\nThe number {num} raised to the power of 3 is: {power_3}")
print(f"The number {num} raised to the power of 4 is: {power_4}")
print(f"The number {num} raised to the power of 5 is: {power_5}")

