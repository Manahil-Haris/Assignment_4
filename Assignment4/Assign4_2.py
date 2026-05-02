# Task 2: Digital Signature with RSA
# Objective: Understand how digital signatures work

import hashlib   # Import hashlib for SHA256 hashing

# --- RSA Key Generation (reuse from Task 1) ---
p = 61
q = 53
n = p * q
phi = (p - 1) * (q - 1)
e = 17

# Extended Euclidean Algorithm to compute modular inverse
def modinv(a, m):
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

# Define public and private keys
public_key = (e, n)
private_key = (d, n)

print("Public Key:", public_key)
print("Private Key:", private_key)

# --- Step 1: Create a message and compute its hash ---
message = "Manahil"
hash_val = int(hashlib.sha256(message.encode()).hexdigest(), 16)  # Convert hash to integer

print("\nOriginal Message:", message)
print("SHA256 Hash (integer):", hash_val)

# --- Step 2: Sign the hash using the private key ---
signature = pow(hash_val, d, n)  # Signature = hash^d mod n
print("Digital Signature:", signature)

# --- Step 3: Verify the signature using the public key ---
verified_hash = pow(signature, e, n)  # Recover hash using public key
print("Signature Valid?", verified_hash == hash_val % n)

# --- Step 4: Tampering demonstration ---
tampered_message = "Manahil "  # Slightly modified message
tampered_hash = int(hashlib.sha256(tampered_message.encode()).hexdigest(), 16)

print("\nTampered Message:", tampered_message)
print("Tampered Hash (integer):", tampered_hash)
print("Signature Valid After Tampering?", pow(signature, e, n) == tampered_hash % n)
