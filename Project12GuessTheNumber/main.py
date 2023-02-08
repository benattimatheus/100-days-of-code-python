from art import logo
from random import randint

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

if difficulty == "easy":
  print("You have 10 attempts remaining to guess the number.")
  attempts = 10
elif difficulty == "hard":
  print("You have 5 attempts remaining to guess the number.")
  attempts = 5

number = randint(1,100)
not_end_of_game = True

while not_end_of_game:

  guess = int(input("Make a guess: "))
  
  if guess == number:
    not_end_of_game = False
    print(f"You got it! The answer was {number}.")
  elif attempts == 1:
    not_end_of_game = False
    print(f"You've run out of guesses, you lose. The answer was {number}")
  elif guess > number:
    attempts -= 1
    print("Too high.")
    print(f"You have {attempts} attempts remaining to guess the number.")
  elif guess < number:
    attempts -= 1
    print("Too low.")
    print(f"You have {attempts} attempts remaining to guess the number.")
