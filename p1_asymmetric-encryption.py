from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
#pip install pycryptodome

# Generate RSA key pair
key = RSA.generate(2048)

private_key = key
public_key = key.publickey()

# Create cipher objects
encryptor = PKCS1_OAEP.new(public_key)
decryptor = PKCS1_OAEP.new(private_key)

# Message to encrypt
message = b"Hello RSA!"

# Encrypt
encrypted = encryptor.encrypt(message)
print("Encrypted:", encrypted)

# Decrypt
decrypted = decryptor.decrypt(encrypted)
print("Decrypted:", decrypted.decode())
