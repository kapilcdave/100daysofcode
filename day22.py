import random

score = 0
while True:
    myNumber = random.randint(1, 100)
    while True:
        guess = input(f"Guess a number between 1 and 100 (or type 'exit' to quit): ")
        if guess.lower() == 'exit':
            print("Exiting the game. Goodbye!")
            print(f"Your final score is {score}.")
            exit()
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
    play_again = input("Do you want to play again? (y/n): ").strip().lower()
    if play_again != 'y':
        print(f"Thanks for playing! Your final score is {score}.")
        break