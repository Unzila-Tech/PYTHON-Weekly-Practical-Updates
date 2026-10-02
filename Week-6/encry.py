main = input("Enter a string: ")
symbol = "@#"
# Encryption
encrypted = ""
for ch in main:
    encrypted = encrypted + ch + symbol

print("Encrypted string:", encrypted)

# Decryption
decrypted = ""
i = 0
while i < len(encrypted):
    decrypted = decrypted + encrypted[i]
    i = i + 3

print("Decrypted string:", decrypted)