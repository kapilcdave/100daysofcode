import random
import string

# All printable ASCII characters except whitespace
all_chars = string.ascii_letters + string.digits + string.punctuation

password = ''.join(random.choices(all_chars, k=19))
print(password)

while True:
    user_input = input("Enter the password: ")
    if user_input == password:
        print("Password is correct")
        break
    if user_input == "help":
        print("Password is", password)
        continue
    else:
        print("Password is incorrect")
        continue