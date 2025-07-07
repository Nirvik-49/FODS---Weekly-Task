import random

'''
This program implements a number guessing game where the user has to guess a randomly generated number.
The user has a maximum of 5 attempts to guess the correct number.
'''

def number_guessing_game():
    # Generate a random number between 1 and 100
    answer = random.randint(1, 100)
    attempts = 5

    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100.")
    print("You have 5 attempts to guess the correct number.")

    for attempt in range(1, attempts + 1):
        user_input = input(f"Attempt {attempt}: Enter your guess: ")

        # Validate input
        if not user_input.isdigit():
            print("Error: Please enter a valid integer.")
            continue

        guess = int(user_input)

        if guess < answer:
            print("Too low!")
        elif guess > answer:
            print("Too high!")
        else:
            print("Correct number! You've guessed it!")
            break

    else:
        print("Game Over! The correct number was:", answer)


