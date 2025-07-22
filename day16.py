print("Name the lyrics of the song:")
#nested loops to guess lyrics
while True:
    #first lyric loop
    while True:
        lyrics = input("Police steady ______ me:")
        if lyrics == "watching":
            print("Correct! The next line is:")
            break
        elif lyrics == "clocking":
            print("Close, but not quite. Try again!")
        elif lyrics == "stalking":
            print("Not quite, but you're getting there!")
        elif lyrics == "following":
            print("Not even close, the flow is different!")
        else:
            print("Retry! Hint: King Von")
    #second lyric loop
    while True:
          lyrics2 = input("Everyday they _____ me: ")
          if lyrics2 == "clocking":
              print("Correct! You got it!")
              print("Thank you for playing! The song is 'Crazy Story' by King Von.")
              exit()
          else:
              print("Try again! Hint: King Von")




