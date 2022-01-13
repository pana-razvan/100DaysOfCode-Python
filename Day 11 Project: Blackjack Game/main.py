from art import logo
import random
from replit import clear

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 5, 5, 5, 5]

def has_blackjack(player):
  if sum(player) == 21 and len(player) == 2:
    return True
  else:
    return False

def calculate_score(player):
  if 11 in player and sum(player) > 21:
    player.remove(11)
    player.append(1)
  return sum(player)

def play():
  print(logo)

  user = []
  computer = []
  game_on = True

  for i in range(2):
    user.append(random.choice(cards))
    computer.append(random.choice(cards))

  print(f"  Your cards: {user}, current score: {sum(user)}")
  print(f"  Computer's first card: {computer[0]}")

  if has_blackjack(computer):
    game_on = False
  elif has_blackjack(user):
    game_on = False
  else:
    game_on = True

  while game_on:
    deal = input("Type 'y' to get another card, type 'n' to pass: ")
    if deal == "y":
      user.append(random.choice(cards))
      calculate_score(user)
      if calculate_score(user) >= 21:
        game_on = False
      else:
        print(f"  Your cards: {user}, current score: {calculate_score(user)}")
        print(f"  Computer's first card: {computer[0]}")

    elif deal == "n":
      while calculate_score(computer) < 17 and calculate_score(computer) < calculate_score(user):
        computer.append(random.choice(cards))
      game_on = False
  
  print(f"  Your final hand: {user}, final score: {calculate_score(user)}")
  print(f"  Computer's final hand: {computer}, final score: {calculate_score(computer)}")

  if has_blackjack(computer):
    print("\nYou lose! Computer has BlackJack!") #Checked
  elif has_blackjack(user):
    print("\nBlackJack! You win!") #Checked
  elif calculate_score(user) > 21:
    print("\nYou went over! You lose!") #Checked
  elif calculate_score(computer) > 21:
    print("\nComputer went over! You win!") #Checked
  elif calculate_score(user) == calculate_score(computer):
    print("\nDraw") #Checked
  elif calculate_score(user) > calculate_score(computer):
    print("\nYou win!") #Checked
  elif calculate_score(user) < calculate_score(computer):
    print("\nYou lose!") #Checked

while input("\nDo you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  clear()
  play()
