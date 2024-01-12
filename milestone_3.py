from milestone_2 import word
import random

def check_guess(guess, word):
    """
    Check if the guessed letter is in the word.

    Parameters:
    - guess (str): The letter guessed by the player.
    - word (str): The word to be guessed.

    Prints:
    - Feedback message based on whether the guess is correct.
    """
    # Convert the guess into lower case.
    guess = guess.lower()

    # Check if the guess is in the word.
    if guess in word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")

def ask_for_input():
    """
    Prompt the user to guess a letter and handle input validation.

    Calls the check_guess function to check if the guess is in the word.
    """
    while True:
        guess = input("Guess a letter: ")

        if guess.isalpha() and len(guess) == 1:
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")

    # Call the check_guess function to check if the guess is in the word.
    check_guess(guess, word)

# Call the ask_for_input function to test your code.
ask_for_input()
