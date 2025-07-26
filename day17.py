print("Rock Paper Scissors Infinite")

from getpass import getpass as input

player1score = 0
player2score = 0
while True:
    player1move = input("Player1 please select your move (R,P,S): ")
    player2move = input("Player2 please select your move (R,P,S): ")

    if player1move == player2move:
        print("It's a tie! 🤝")
    elif (player1move == "R" and player2move == "S"):
        print("Player 1 wins! 🥇 Rock crushes Scissors!")
        player1score += 1
    elif (player1move == "S" and player2move == "P"):
        print("Player 1 wins! 🥇 Scissors cut Paper!")
        player1score += 1
    elif (player1move == "P" and player2move == "R"):
        print("Player 1 wins! 🥇 Paper covers Rock!")
        player1score += 1
    elif (player2move == "R" and player1move == "S"):
        print("Player 2 wins! 🥈 Rock crushes Scissors!")
        player2score += 1
    elif (player2move == "S" and player1move == "P"):
        print("Player 2 wins! 🥈 Scissors cut Paper!")
        player2score += 1
    elif (player2move == "P" and player1move == "R"):
        print("Player 2 wins! 🥈 Paper covers Rock!")
        player2score += 1
    else:
        print("Invalid move! Please select R, P, or S.")
        continue
    print(f"Player 1: {player1score}, Player 2: {player2score}")

