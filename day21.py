print("Math Game!")
score = 0
multiples = int(input("Name your multiples:"))

for i in range(0, 10, 1):
    question = input(f"What is {i} times {multiples}? ")
    if question == str(i * int(multiples)):
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! The answer is {i * int(multiples)}")
print(f"Your score is {score} out of 10.")
exit()

