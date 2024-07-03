'''Rock-Paper-Scissors Game Simulation
This program simulates the classic game of Rock-Paper-Scissors against a computer opponent. Players can choose their move and
see the computer's choice, with outcomes displayed (win, lose, or draw). The game continues until the player decides to end it.

Game Setup: Allows players to start by entering "ENTER" and then choosing between "rock," "paper," or "scissors."
Interactive Gameplay: Displays ASCII art representing player and computer choices, and determines the winner.
End Options: Offers players the choice to continue playing ("play") or end the game ("end") after each round.'''



rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

start_input = input("Welcome to the Game. Type 'ENTER' to start the game.\n")
lower_start_input = start_input.lower() 

while lower_start_input == "enter" or lower_start_input == "play" or lower_start_input == "end":
    if lower_start_input == "enter" or lower_start_input == "play":
        print("What is your choice? Rock, Paper, or Scissors?")
        user_input = input()
        change_lower = user_input.lower()
        computer_side = ["rock", "paper", "scissor"]

        if change_lower == "rock" or change_lower == "paper" or change_lower == "scissor":
            if change_lower == "rock":
                print(rock)
            if change_lower == "paper":
                print(paper)
            if change_lower == "scissor":
                print(scissors)

            computer_choice = random.choice(computer_side)
            print(f"The computer chose {computer_choice}")

            if computer_choice == "rock":
                print(rock)
            if computer_choice == "paper":
                print(paper)
            if computer_choice == "scissor":
                print(scissors)

            if change_lower == "rock" and computer_choice == "scissor":
                print("YOU WIN")
            elif change_lower == "scissor" and computer_choice == "paper":
                print("YOU WIN")
            elif change_lower == "paper" and computer_choice == "rock":
                print("YOU WIN")
            elif change_lower == computer_choice:
                print("IT'S A DRAW")
            else:
                print("YOU LOSE")

            lower_start_input = input("Type 'play' to play again or 'end' to quit.\n")
    
    if lower_start_input == "end":
        print("Thank you for playing. Goodbye!")
        break  
    
    while lower_start_input != "end" and lower_start_input != "play":
        lower_start_input = input("Please enter a valid command: 'play' or 'end'.\n")
else:
    print("Invalid command. Please start again.")                
       




















        













































    
