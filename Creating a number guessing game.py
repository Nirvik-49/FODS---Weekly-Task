'''
This program implements a number guessing game where the user has to guess a randomly generated number.
The user has a maximum of 5 attempts to guess the correct number.
'''
import random  # Importing the random module to generate a random number.

# Generate a random number between 1 and 100
answer = random.randint(1, 100)

# Initialize the number of attempts
attempts = 5
print("Welcome to the Number Guessing Game!")
print("Select a number between 1 and 100.")
print("You have 5 attempts to guess the correct number.")

# Loop for a maximum of 5 attempts
for attempt in range(attempts):
    
    # Prompt the user for a number input
    guess = int(input(f"Attempt {attempt + 1}: Please enter your guess: "))
    
    # Provide feedback based on the user's guess
    if guess < answer:
        print("Too low!")
    elif guess > answer:
        print("Too high!")
    else:
        print("Correct number! You've guessed it!")
        break  # Exit the loop if the guess is correct
    
# Check if the user has used all attempts

if guess != answer:
    print("Game Over! The correct number was:", answer)
