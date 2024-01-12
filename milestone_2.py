import random

# Variable word_list (you can also change the topic game as you wish)
favorite_fruits_list = ["apple", "banana", "orange", "grapes", "watermelon"]

def get_random_word(word_list):
    """
    Get a random word from the provided list.

    Parameters:
    - word_list (list): List of words to choose from.

    Returns:
    - str: A randomly selected word from the list.
    """
    return random.choice(word_list)

# Get a random word
word = get_random_word(favorite_fruits_list)
print(word)

# Ask the user for input
guess = input("Enter a single letter: ")

def is_valid_input(input_str):
    """
    Validate if the input is a single alphabetical character.

    Parameters:
    - input_str (str): The input string to be validated.

    Returns:
    - bool: True if the input is valid, False otherwise.
    """
    return len(input_str) == 1 and input_str.isalpha()

if is_valid_input(guess):
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")