import random

myNumber = random.randint(1, 100)
score = 0
while True:
    guess = input(f"Guess a number between 1 and 100 (or type 'exit' to quit): ")
    if guess.lower() == 'exit':
        print("Exiting the game. Goodbye!")
        break
    if not guess.isdigit():
        print("Please enter a valid number.")
        continue
    guess = int(guess)
    if guess < 1 or guess > 100:
        print("Your guess is out of range. Please try again.")
        continue
    elif guess < myNumber:
        print("Too low! Try again.")
    elif guess > myNumber:
        print("Too high! Try again.")
    elif guess == myNumber:
        score += 1
        print(f"Congratulations! You guessed the number {myNumber}. Your score is now {score}.")
        break
    else:
        print("Keep guessing!")

for i in range(10):
    myNumber = random.randint(1, 100)