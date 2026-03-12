# ----- Manual RSA Implementation -----


# 1. Choose two prime numbers
p = 61
q = 53


# 2. Compute n = p * q
n = p * q
print("n =", n)


# 3. Compute Euler's Totient φ(n) = (p-1)(q-1)
phi = (p - 1) * (q - 1)
print("phi =", phi)


# 4. Choose public key exponent e (must be coprime with phi)
e = 17
print("Public exponent e =", e)


# 5. Compute private key exponent d (modular inverse of e mod phi)
def mod_inverse(e, phi):
    for d in range(1, phi):
        if (d * e) % phi == 1:
            return d
    return None


d = mod_inverse(e, phi)
print("Private exponent d =", d)


# 6. Message (as number)
message = 65
print("\nOriginal Message =", message)


# 7. Encrypt:  ciphertext = message^e mod n
ciphertext = pow(message, e, n)
print("Encrypted =", ciphertext)


# 8. Decrypt: plaintext = ciphertext^d mod n
plaintext = pow(ciphertext, d, n)
print("Decrypted =", plaintext)
