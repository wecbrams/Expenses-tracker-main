import random

# Ask user for password length
length = int(input("Enter password length: "))

# Manually define characters
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "0123456789"
symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?"

# Combine all characters
all_chars = letters + digits + symbols

# Generate password
password = ''.join(random.choice(all_chars) for i in range(length))

print("Your password is:", password)