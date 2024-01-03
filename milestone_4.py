import random

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