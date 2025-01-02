# password_generator.py
import random
import string

def generate_password(length=12):
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

print("Welcome to the Password Generator!")
length = int(input("Enter password length (default is 12): ") or 12)
print(f"Your generated password: {generate_password(length)}")
