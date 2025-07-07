'''
Program finds all numbers between a given range that are divisible by 7 but not a multiple of 5.
'''

# Function to find numbers divisible by 7 but not a multiple of 5
def find_numbers(start, end):
    numbers = []
    for num in range(start, end + 1):
        if num % 7 == 0 and num % 5 != 0:
            numbers.append(num)
    return numbers

# Fixed range between 2000 and 3200
start_fixed = 2000
end_fixed = 3200


# Find numbers in the fixed range
numbers_fixed = find_numbers(start_fixed, end_fixed)
print(f"Numbers between {start_fixed} and {end_fixed} that are divisible by 7 but not a multiple of 5:")
print(numbers_fixed)


# Input from user for custom range
start_user = int(input("\nEnter the starting number: "))
end_user = int(input("Enter the ending number: "))


# Find numbers in the user-defined range
numbers_user = find_numbers(start_user, end_user)
print(f"\nNumbers between {start_user} and {end_user} that are divisible by 7 but not a multiple of 5:")
print(numbers_user)


