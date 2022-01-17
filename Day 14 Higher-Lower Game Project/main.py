from game_data import data
from random import choice
from art import logo, vs
from replit import clear

def has_more_followers(A,B):
  """Checks who has more followers (A or B) and returns a string result 'a' or 'b'"""
  if A["follower_count"] >= B["follower_count"]:
    return "a"
  elif B["follower_count"] >= A["follower_count"]:
    return "b"

def compare(A,B):
  """ Prints the items to be compared"""
  print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}.")
  print(vs)
  print(f"Against B: {B['name']}, a {B['description']}, from {B['country']}.")

def game():
  print(logo)

  # Select random item from the data list
  item_B = choice(data)

  # Keep track of score
  score = 0

  # Game start
  game_on = True

  while game_on:
    # Select random items and show them to the user
    item_A = item_B
    item_B = choice(data)
    compare(item_A, item_B)

    # Ask user to answer and compare his answer to the correct answer
    user_answer = input("Who has more followers? Type 'A' or 'B': ").lower()
    correct_answer = has_more_followers(item_A, item_B)

    clear()
    print(logo)

    # If user is right, add a score point and continue to the next item
    if user_answer == correct_answer:
      score += 1
      print(f"You're right! Current score: {score}.")

    # If user is wrong, game ends and the final score is displayed
    else:
      game_on = False
      print(f"Sorry, that's wrong. Final score: {score}")

      if input("Play again? Type 'y' for yes or 'n' for no: ") == "y":
        clear()
        game()
      else:
        print("Have a nice day! Goodbye!")

game()
