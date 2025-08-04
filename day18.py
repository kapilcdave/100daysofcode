print("Number Guessing Game")
from random import randint
print("----------------------")
print("Guess a number between 1 and 111")
numberguess = randint(1, 111)
attempts = 0
while True:
    guess = int(input("Enter your guess: "))
    attempts += 1
    if guess < numberguess:
        print("Too low! Try again.")
    elif guess > numberguess:
        print("Too high! Try again.")
    elif guess == 1 or guess == 111:
        print("So close! 🎉")
    else:
        print("Congratulations! You've guessed the number!")
        break
        print("Exiting the game.")
print(f"It took you", attempts, "tries to guess the number.")
print("Thanks for playing!")