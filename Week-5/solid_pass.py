import random
import string

chars = string.ascii_letters + string.digits + "!@#$%^&*"
password = random.sample(string.ascii_uppercase, 2) + \
           random.sample(string.digits, 1) + \
           random.sample("!@#$%^&*", 1) + \
           random.choices(chars, k=6)

random.shuffle(password)
print("Password:", ''.join(password))
