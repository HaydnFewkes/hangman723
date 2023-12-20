# File for milestone_3, using functions to check if a letter is in the word

# Function that checks if the letter in in the word, the word is not given yet
def check_guess(guess):
    guess = guess.lower()
    word = "apple"
    if guess in word:
        print("Good guess! ("+guess+") is in the word.")
    else:
        print("Sorry, ("+guess+") is not in the word. Try again.")

# Function that takes the user input and makes sure its a single letter, then checks if its in the word
def ask_for_input():
    while True:
        guess = input("Enter a single letter: ")
        if guess.isalpha() == True and len(guess) == 1:
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
    check_guess(guess)

ask_for_input()