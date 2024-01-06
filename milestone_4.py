import random

# Initiate the Hangman  class
class Hangman:
    def __init__(self, word_list, num_lives = 5):
        self.num_lives = num_lives
        self.word_list = word_list
        self.word = random.choice(self.word_list)
        self.word_guessed = []
        self.repeat_letters = []
        for i in range(0,len(self.word)):
            self.word_guessed.append("_")
        for letter in self.word:
            if letter not in self.repeat_letters:
                self.repeat_letters.append(letter)
        self.num_letters = len(self.repeat_letters)
        self.list_of_guesses = []

    # Function that checks if the letter in in the word
    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print("Good guess! ("+guess+") is in the word.")
            index = 0
            for letter in self.word:
                if letter == guess:
                    self.word_guessed[index] = guess
                index += 1
            self.num_letters -= 1
            print(self.word_guessed)
        else:
            print("Sorry, ("+guess+") is not in the word. Try again.")
            self.num_lives -= 1
            print("You have "+str(self.num_lives)+" lives left.")

    # Function that takes the user input and makes sure its a single letter, then checks if its in the word
    def ask_for_input(self):
        while True:
            guess = input("Enter a single letter: ")
            if guess.isalpha() != True or len(guess) != 1:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter.")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
        


game = Hangman(["apple"])
game.ask_for_input()