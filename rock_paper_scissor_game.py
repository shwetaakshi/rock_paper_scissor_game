# -*- coding: utf-8 -*-
"""rock_paper_scissor_game.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1pIfWDU45n0goOrHjX9yq0NC8LQnO5Azd
"""

import random

def get_choices():
  player_choice = input("Enter a choice (rock, paper, scissors):")
  options = ["rock", "paper", "scissors"]
  computer_choice = random.choice(options)
  choices = {"player":player_choice,"computer": computer_choice}
  return choices

def check_win(player , computer):
  print(f"You chose {player}, computer chose {computer}")
  if player == computer:
    return "It's a tie!"
  elif player == "rock":
    if computer == "scissors":
      return "Rock smashes scissors! You Win!"
    else:
      return "Paper covers rock! You lose."
  elif player == "paper":
    if computer == "rock":
      return "Paper covers rock! You Win!"
    else:
      return "Scissors cuts paper! You lose."
  elif player == "scissors":
    if computer == "paper":
      return "Scissors cuts paper ! You Win!"
    else:
      return "Rock smashes scissors! You lose."

choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)