from replit import clear

from art import logo

bid = {}

more = True

highest = 0

def highest_bidder(bidding_record):
  highest = 0
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest:
      highest = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest}")

while more == True:
  print(logo)
  print("Welcome to the secret auction program")
  name = input("What is your name?\n")
  bidprice = float(input("What is your bid?: $"))
  bid[name] = bidprice

  again = input("Are there any other bidders? Type Yes or No:\n").lower()

  if again == "no":
    more = False
    clear()
  else:
    clear() 

highest_bidder(bid)

