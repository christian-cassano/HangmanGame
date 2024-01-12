import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        """
        Initialize the Hangman game.

        Parameters:
        - word_list (list): List of words to be guessed.
        - num_lives (int): Number of lives for the player (default is 5).
        """
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = self.choose_random_word()
        self.word_progress = ['_'] * len(self.word)
        self.num_letters = len(set(self.word))
        self.guesses = []

    def choose_random_word(self):
        """
        Choose a random word from the list.

        Returns:
        - str: Randomly selected word.
        """
        return random.choice(self.word_list)

    def is_valid_input(self, input_str):
        """
        Check if the input is a valid single alphabetical character.

        Parameters:
        - input_str (str): Input to be validated.

        Returns:
        - bool: True if the input is valid, False otherwise.
        """
        return len(input_str) == 1 and input_str.isalpha()

    def update_word_progress(self, guess):
        """
        Update the word progress with the correct guesses.

        Parameters:
        - guess (str): The letter guessed by the player.
        """
        for i, letter in enumerate(self.word):
            if letter == guess:
                self.word_progress[i] = guess
        self.num_letters -= 1

    def check_guess(self, guess):
        """
        Check if the guess is in the word.

        Parameters:
        - guess (str): The letter guessed by the player.
        """
        guess = guess.lower()

        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            self.update_word_progress(guess)
        else:
            print(f"Sorry, {guess} is not in the word.")
            self.num_lives -= 1
            print(f"You have {self.num_lives} lives left.")

    def ask_for_input(self):
        """
        Prompt the user to guess a letter and handle input validation.
        """
        while True:
            guess = input("Guess a letter: ")

            if not self.is_valid_input(guess):
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.guesses:
                print("You already tried that letter!")
            else:
                self.guesses.append(guess)
                self.check_guess(guess)
                break
            
# If you wish change the list to change the topic of the game 
word_list = ["apple", "banana", "orange", "grapes", "watermelon"]
hangman_game = Hangman(word_list)

while hangman_game.num_lives > 0 and '_' in hangman_game.word_progress:
    hangman_game.ask_for_input()

# Game over message
if '_' not in hangman_game.word_progress:
    print("Congratulations! You guessed the word.")
else:
    print(f"Sorry, you ran out of lives. The word was {hangman_game.word}.")

