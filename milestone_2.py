# File for milestone_2, takes a list of words and selects a random one
import random

# Choosing a random word from the list
word_list = ["Banana", "Pear", "Kiwi", "Peach", "Grape"]
word = random.choice(word_list)
# Takes a userinput for a single letter
guess = input("Enter a single letter: ")
if len(guess) == 1:
    print("Good Guess!")
else:
    print("Oops! That is not a valid input.")
print(word, guess)