print("TV Show Check")
print("-------------")
tvshow = input("what is your favorite tv show?")
if tvshow == "peppa pig":
    print("why?")
    favcharacter = input("who is your favorite character?")
    if favcharacter == "daddy pig":
        print("correct!")
    else:
        print("thanks for sharing")
elif tvshow == ("Thomas the Tank Engine"):
    print("good choice")
else:
    print("I've never heard of that show")
    tvshowlength = input("can you spell the tv show's name?")
    if len(tvshowlength) <= 11:
        print("If you can't spell it then it doesn't exist")