from art import logo
from random import randint

EASY_ATTEMPTS = 10
HARD_ATTEMPTS = 5

def check_answer(guess, number, attempts):
  if guess > number:
    print("Too high.")
    return attempts - 1
  elif guess < number:
    print("Too low.")
    return attempts - 1
  elif guess == number:
    print(f"You got it! The answer was {number}.")

def difficulty():
  choice = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
  if choice == "easy":
    return EASY_ATTEMPTS
  elif choice == "hard":
    return HARD_ATTEMPTS

def game():

  print(logo)
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100") 
  number = randint(1,100)
  attempts = difficulty()
  guess = 0
  
  while guess != number:

    print(f"You have {attempts} attempts remaining to guess the number.")
  
    guess = int(input("Make a guess: "))
    attempts = check_answer(guess, number, attempts)
    if attempts == 0:
      print("You've run out of guesses, you lose.")
      return
    elif guess != number:
      print("Guess again.")

game()