import random

def __init__(self, player1_choice=None, player2_choice=None):
    """Initializes the Rock-Paper-Scissors game with optional player choices."""
    self.player1_choice = player1_choice if player1_choice else __generate_random_choice()
    self.player2_choice = player2_choice if player2_choice else __generate_random_choice()
    
def __generate_random_choice():
    """Generates a random choice of 'rock', 'paper', or 'scissors'."""
    return random.choice(['rock', 'paper', 'scissors'])

def play_rps(player1_choice, player2_choice):
    choices = ['rock', 'paper', 'scissors']
    
    if player1_choice not in choices or player2_choice not in choices:
        raise ValueError("Invalid choice. Choose from 'rock', 'paper', or 'scissors'.")

    if player1_choice == player2_choice:
        return "It's a tie!"
    
    if (player1_choice == 'rock' and player2_choice == 'scissors') or \
       (player1_choice == 'paper' and player2_choice == 'rock') or \
       (player1_choice == 'scissors' and player2_choice == 'paper'):
        return "Player 1 wins!"
    
    return "Player 2 wins!"

def main():
    player1_choice = input("Player 1, enter your choice (rock, paper, scissors): ").strip().lower()
    player2_choice = input("Player 2, enter your choice (rock, paper, scissors): ").strip().lower()
    
    try:
        result = play_rps(player1_choice, player2_choice)
        print(result)
    except ValueError as e:
        print(e)