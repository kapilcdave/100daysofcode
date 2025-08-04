print("Loan Calculator")

loan = int(input("Loan amount: "))
if loan < 0:
    print("Please enter a positive number.")
  
year = int(input("Number of years: "))
if year < 0:
    print("Please enter a positive number.")
  
rate = int(input("Interest rate: "))
if rate < 0:
    print("Please enter a positive number.")
 
original_loan = loan
for i in range(year):
    interest = loan * (rate / 100)
    loan += interest
    print("Year", i + 1, ":", loan)

interest = loan - original_loan
print("You payed", interest, "in interest")