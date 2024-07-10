"""This code implements a number guessing game using Python functions and random number generation.
It prompts the user to guess a randomly generated number within a specified range and provides feedback on each guess.

Random Number Generation and User Interface: This part of the code imports the random module, generates a random number between 1
                                            and 100, and prints a welcome message to the user.
Gameplay Logic: The steps function handles the main gameplay loop, where the user is prompted to guess the number.
                                           The function provides feedback ("Too high", "Too low") and tracks the number of attempts remaining.
                                           The user wins if they guess the number correctly within the allowed attempts; otherwise, they lose."""



art="""

   ______                        __  __            _   __                __             
  / ____/_  _____  __________   / /_/ /_  ___     / | / /_  ______ ___  / /_  ___  _____
 / / __/ / / / _ \/ ___/ ___/  / __/ __ \/ _ \   /  |/ / / / / __ `__ \/ __ \/ _ \/ ___/
/ /_/ / /_/ /  __(__  |__  )  / /_/ / / /  __/  / /|  / /_/ / / / / / / /_/ /  __/ /    
\____/\__,_/\___/____/____/   \__/_/ /_/\___/  /_/ |_/\__,_/_/ /_/ /_/_.___/\___/_/     
                                                                                        
"""
import random

def random_number():
    random_numbers=random.randint(1,100)
    return random_numbers
number=random_number()



def steps(turn):
    print(f"You have {turn} attempts remaining to guess the number")        
    count=0
    A=0
    while A==0:
            user_input=int(input("Make a guess:"))
            if user_input==number:
                print(f"You got it! The answer was {number}")
                print(".......You Win.......")
                break
            else:
                if user_input>number:
                    print("Too high")
                    
                elif user_input<number:
                    print("Too Low")
                count+=1
                if count!=turn:
                    life=turn-count
                    print(f"You have still {life} chance more")
            if count==turn:
                A=1
                print(".......You Lose.......")
    
print(art)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100..")
#print(f"number={number}")
difficulty_input=input("Choose a difficulty.Type 'easy' or 'hard':")
if difficulty_input=="easy":
    steps(turn=10)
elif difficulty_input=="hard":
    steps(turn=5)
    

