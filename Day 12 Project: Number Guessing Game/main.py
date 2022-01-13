import random
from art import logo
from replit import clear

def set_dificulty():
  dificulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if dificulty == "easy":
    return 10
  else:
    return 5

def check_guess(guess,the_number,no_of_guesses):
  """Checks if the player's guess is lower, higher or equal to the number."""
  if guess > the_number:
    print("Too high!")
    return no_of_guesses - 1
  elif guess < the_number:
    print("Too low!")
    return no_of_guesses - 1
  else:
    print(f"You got it! The answer was {the_number}")

def game():
  print(logo)
  print("Welcome to guess the number!")
  print("I am thinking of a number between 1 and 100")
  the_number = random.choice(range(1,101))
  no_of_guesses = set_dificulty()
  guess = 0

  while guess != the_number and no_of_guesses != 0:
    print(f"You have {no_of_guesses} remaining attempts to guess the number.")
    guess = int(input("Make a guess: "))
    no_of_guesses = check_guess(guess,the_number,no_of_guesses)
    if no_of_guesses == 0:
      print("You ran out of guesses. You lost.")
    elif guess != the_number and no_of_guesses != 0:
      print("Try again.")

  print("")
  if input("Do you want to play again? Type 'y' for Yes or 'n' for No: ") == "y":
    clear()
    game()
  else:
    print("Have a nice day!")

game()
