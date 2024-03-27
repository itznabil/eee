def mod_inverse(a, m):
    return pow(a, -1, m)

def encrypt(message, e, n):
    return pow(message, e, n)

def decrypt(ciphertext, d, n):
    return pow(ciphertext, d, n)

# Given parameters
p = 17
q = 31
e = 7
m = 2

# Calculate n and phi(n)
n = p * q
phi_n = (p - 1) * (q - 1)


# Calculate d
#d = mod_inverse(e, phi_n)
d = mod_inverse(e, phi_n)

# Encryption
ciphertext = encrypt(m, e, n)
print("Encrypted:", ciphertext)

# Decryption
plaintext = decrypt(ciphertext, d, n)
print("Decrypted:", plaintext)


