from replit import clear
from art import logo
print(logo)

print("Welcome to the silent bid.")

auction_entries = {}
auction_in_progress = True

def find_highest_bidder(bids):
  winner_name = ""
  winning_bid = 0
  for bidder in bids:
    if bids[bidder] > winning_bid:
      winning_bid = bids[bidder]
      winner_name = bidder
  print(f"The winner is {winner_name} with a bid of ${winning_bid}")

while auction_in_progress:
  name = input("What is your name: ")
  bid = int(input("What is your bid? $"))
  auction_entries[name] = bid

  # if auction_entries[name] > winning_bid:
  #   winning_bid = auction_entries[name]
  #   winner_name = name

  more_bidders = input("Are there any other bidders? Type 'yes' or 'no'.")

  if more_bidders == "no":
    auction_in_progress = False
    find_highest_bidder(auction_entries)
  elif more_bidders == "yes":
    clear()
