import secrets
import math

code = secrets.randbelow(900000) + 100000
print("Random OTP:", code)

# choose two prime numbers
p = int(input("Input a p value: "))
q = int(input("Input a q value: "))

# calculate n
n = p * q
 
# calculate phi(n)
phi = (p - 1) * (q - 1)
print("phi value",phi)


e =2
while 1 < phi:
    if 1 < e < phi and math.gcd(e, phi) == 1:
        break
    e += 1

print("Selected e:", e)

# d = modular inverse
d = pow(e, -1, phi)

print("Public key:", (e, n))
print("Private key:", (d, n))

if code >= n:
    print("Message must be smaller than n")
else:
    ciphertext = pow(code, e, n)
    print("Encrypted Message:", ciphertext)

    decrypt_message = pow(ciphertext, d, n)
    print("Decrypted Message:", decrypt_message)