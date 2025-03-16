import random

options = ('rock', 'paper', 'scissors')

running = True

while running:
  
  computer_choice = random.choice(options)
  player_choice = None

  while player_choice not in options:
    player_choice = input("Enter your choice: ('rock', 'paper', 'scissors') ").lower()

  if player_choice == computer_choice:
    print(f"Computer's Choice: {computer_choice}")
    print(f"Player's Choice: {player_choice}")
    print("It's a tie!")
  elif player_choice == 'rock' and computer_choice == 'paper':
    print(f"Computer's Choice: {computer_choice}")
    print(f"Player's Choice: {player_choice}")
    print("You Loose!")
  elif player_choice == 'paper' and computer_choice == 'scissors':
    print(f"Computer's Choice: {computer_choice}")
    print(f"Player's Choice: {player_choice}")
    print("You Loose!")
  elif player_choice == 'scissors' and computer_choice == 'rock':
    print(f"Computer's Choice: {computer_choice}")
    print(f"Player's Choice: {player_choice}")
    print("You Loose!")
  else:
    print(f"Computer's Choice: {computer_choice}")
    print(f"Player's Choice: {player_choice}")
    print("You Won!")

  play_again = input("Do you want to play another game( y/n )! ").lower()
  if not play_again == 'y':
    running = False
  
print("Thanks For Playing!")