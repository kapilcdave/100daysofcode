print("Bill Calculator")
print()
bill = float(input("what was the total cost?"))
party = int(input("how many people?"))
while party <= 0:
    print("Number of people must be greater than zero.")
    party = int(input("how many people?"))

tip = float(input("what percent tip?"))
billtip = (bill+(bill * (tip/100)))
individual = (billtip/party)

print("If the total was", bill, "and", party, "people ordered, and the tip percent is",
      tip, ", each person pays", individual)