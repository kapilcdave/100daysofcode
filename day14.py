from getpass import getpass as input

print("Rock Paper Scissors 🪨📄✂️")
print("") 
player1move = input("Player1 please select your move (R,P,S)")
player2move = input("Player2 please select your move (R,P,S)")
if player1move == player2move:
    print("It's a tie! 🤝")
elif (player1move == "R" and player2move == "S"):
    print("Player 1 wins! 🥇 Rock crushes Scissors!")
elif (player1move == "S" and player2move == "P"):
    print("Player 1 wins! 🥇 Scissors cut Paper!")
elif (player1move == "P" and player2move == "R"):
    print("Player 1 wins! 🥇 Paper covers Rock!") 
elif (player2move == "R" and player1move == "S"):
    print("Player 2 wins! 🥈 Rock crushes Scissors!")
elif (player2move == "S" and player1move == "P"):
    print("Player 2 wins! 🥈 Scissors cut Paper!")
elif (player2move == "P" and player1move == "R"):
    print("Player 2 wins! 🥈 Paper covers Rock!")
else:
    print("Invalid move! Please select R, P, or S.")

print("Thank you for playing Rock Paper Scissors! 🎉")