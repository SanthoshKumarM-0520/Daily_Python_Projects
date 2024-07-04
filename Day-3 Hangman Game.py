hangman = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

print("Welcome to the Hangman Game")
enter_input = input("Press 'Enter' to start the game:").lower()
correct_empty = []
wrong_empty = []
wrong_count = 0
correct = 0
import random
words = ["school", "party", "elephant"]
random_words = random.choice(words)
len_random_words = len(random_words)
len_hangman = len(random_words)
for m in range(len_random_words):
    correct_empty.append("_")
if enter_input == "enter":
    while wrong_count < 7 and correct < len_random_words:
        user_input = input("Enter a letter:").lower()
        my_word = random_words
        if user_input in my_word:
            for i in range(len_random_words):
                if my_word[i] == user_input:
                    correct += 1
                    correct_empty[i] = user_input
            print("Correct guess!")
            print("Current progress:", correct_empty)
        else:
            wrong_count += 1
            print("Incorrect guess!")
            print(hangman[(wrong_count - 1)])
    if wrong_count == 7:
        print("Game over! You ran out of guesses.")
    elif correct == len_random_words:
        print("Congratulations! You guessed the word.")
    else:
        print("Something went wrong.")
        print(f"Correct guesses: {correct}")
        print(f"Wrong guesses: {wrong_count}")

else:
    print("Invalid input. Please restart the game.")



