import random
import string

# All printable ASCII characters except whitespace
all_chars = string.ascii_letters + string.digits + string.punctuation

password = ''.join(random.choices(all_chars, k=19))
print(password)