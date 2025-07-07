'''
Program continuously takes input from the user to find the sum of odd and even numbers.
Program is menu-driven, allowing the user to continue or exit the program.
'''

# Function to calculate the sum of odd and even numbers
def calculate_sums(numbers):
    sum_even = sum(num for num in numbers if num % 2 == 0)
    sum_odd = sum(num for num in numbers if num % 2 != 0)
    return sum_even, sum_odd

# Main program loop
def main():
    numbers = []
    
    while True:
        user_input = input("Enter a number (or type 'exit' to finish): ")
        
        if user_input.lower() == 'exit':
            break
        
        # Validate input
        if user_input.isdigit() or (user_input.startswith('-') and user_input[1:].isdigit()):
            numbers.append(int(user_input))
        else:
            print("Error: Please enter a valid integer.")
            continue
        
        # Ask if the user wants to continue
        continue_input = input("Do you want to continue? (yes/no): ").strip().lower()
        if continue_input != 'yes':
            break

    # Calculate sums
    sum_even, sum_odd = calculate_sums(numbers)
    
    # Display results
    print(f"\nSum of even numbers: {sum_even}")
    print(f"Sum of odd numbers: {sum_odd}")

# Call the main function to run the program
main()

