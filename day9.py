print("Generation Guesser")
print()
age = int(input("what is your birth year?"))
if age >= 1925 and age <= 1946:
    print("Traditionalist")
elif age >= 1947 and age <= 1964:
    print("Baby Boomer")
elif age >= 1965 and age <= 1981:
    print("Generation X")
elif age >= 1982 and age <= 1995:
    print("Millenials")
elif age >= 1996 and age <= 2015:
    print("Generation Z")
else:
    print("I don't have a name for your generation")