# Task 1: Simple RSA Implementation
# Objective: Understand the math behind RSA

# Step 1: Choose two small prime numbers
p = 61
q = 53

# Step 2: Compute modulus n and Euler's totient phi
n = p * q
phi = (p - 1) * (q - 1)

# Step 3: Choose public exponent e (must be coprime with phi)
e = 17

# Step 4: Compute private exponent d using modular inverse
def modinv(a, m):
    # Extended Euclidean Algorithm
    def egcd(a, b):
        if a == 0:
            return (b, 0, 1)
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('No modular inverse')
    return x % m

d = modinv(e, phi)

print("Public Key (e, n):", (e, n))
print("Private Key (d, n):", (d, n))

# Step 5: Encryption function
def encrypt(msg, e, n):
    return [pow(ord(c), e, n) for c in msg]

# Step 6: Decryption function
def decrypt(cipher, d, n):
    return ''.join([chr(pow(c, d, n)) for c in cipher])

# Step 7: Test with a short string (your name)
message = "Manahil"
cipher = encrypt(message, e, n)
print("Ciphertext:", cipher)

decrypted = decrypt(cipher, d, n)
print("Decrypted:", decrypted)
