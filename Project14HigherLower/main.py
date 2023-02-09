from art import logo, vs
from game_data import data
import random

def get_random_account():
  return random.choice(data)

def format_data(account):
  name = account['name']
  description = account['description']
  country = account['country']
  return f"{name}, a {description}, from {country}"

def check_answer(guess, a_followers, b_followers):
  if a_followers > b_followers:
    return guess == 'a'
  else:
    return guess == 'b'

def game():
  print(logo)
  score = 0
  game_is_over = False

  accounta = get_random_account()
  accountb = get_random_account()

  while game_is_over == False:
    accounta = accountb
    accountb = get_random_account()

    while accounta == accountb:    
      accountb = get_random_account()
      
    print(f"Compare A: {format_data(accounta)}")
    print(vs)
    print(f"Against B: {format_data(accountb)}")
    guess = input("\nWho was more followers? Type 'A' or 'B': ")
    a_follower_count = accounta["follower_count"]
    b_follower_count = accountb["follower_count"]
    is_right = check_answer(guess, a_follower_count, b_follower_count)

    if is_right:
      score += 1
      print(f"You're right! Current score: {score}\n")
    else:
      game_is_over = True 
      print(f"Sorry, that's wrong. Final score {score}")

game()
