print("Statement Generator")
print("====================")
name = input("what is your name?")
if name == "dave" or name == "Dave" or name == "dong":
    print("Hello")
else:
    print("that's not your name")
achieve = input("what do you want to do? Eat, Sleep, or Learn?")
if achieve == "sleep" or achieve == "learn":
    print("loading...")
    print("those are good choices")
elif achieve == "eat":
    print("maybe exercise instead")
else:
    print("answer the question lil bro")

print("To summarize, your name is", name, "you want to", achieve, "today, but you really should get a job!")