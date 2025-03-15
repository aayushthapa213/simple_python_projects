import random

lower_num = 1
higher_num = 100 

answer = random.randint(lower_num, higher_num)

guesses = 0

is_running = True

print("------------------------------------------")
print("Python Number Guessing Game:")
print(f"Select a number between {lower_num} and {higher_num}: ")
print("------------------------------------------")

while is_running:
  guess = input("Enter your guess: ")
  if guess.isdigit():
    guess = int(guess)
    guesses += 1

    if guess < lower_num or guess > higher_num:
      print("The number is out of range!")
      print(f"Please select a number between {lower_num} and {higher_num}: ")
    elif guess < answer:
      print("Too Low!") 
    elif guess > answer:
      print("Too High!")
    else:
      print(f"Correct! The answer was {answer}.")
      print(f"Total Guesses: {guesses}")
      is_running = False

  else:
    print("Invalid Guess!")
    print(f"Please select a number between {lower_num} and {higher_num}: ")
