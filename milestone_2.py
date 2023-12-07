import random

word_list = ["Banana", "Pear", "Kiwi", "Peach", "Grape"]
word = random.choice(word_list)
guess = input("Enter a single letter: ")
if len(guess) == 1:
    print("Good Guess!")
else:
    print("Oops! That is not a valid input.")
print(word, guess)