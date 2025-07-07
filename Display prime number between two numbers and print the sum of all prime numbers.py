'''
Program takes two numbers as input from the user and displays all the prime numbers between those two numbers,
along with the sum of all the prime numbers found.
'''

# Function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


# Function to find prime numbers between two numbers
def find_primes_between(start, end):
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes


# Input from user
start_num = int(input("Enter the starting number: "))
end_num = int(input("Enter the ending number: "))

# Find prime numbers between the two numbers
prime_numbers = find_primes_between(start_num, end_num)

# Calculate the sum of prime numbers
sum_of_primes = sum(prime_numbers)

# Display output of the program
print(f"\nPrime numbers between {start_num} and {end_num} are: {prime_numbers}")
print(f"Sum of all prime numbers between {start_num} and {end_num} is: {sum_of_primes}")

