import numpy as np

# Function to generate key matrix
def generate_key(key):
    key = key.replace(" ", "").upper()
    n = int(np.sqrt(len(key)))
    key_matrix = np.zeros((n, n), dtype=int)
    idx = 0
    for i in range(n):
        for j in range(n):
            key_matrix[i][j] = ord(key[idx]) - ord('A')
            idx += 1
    return key_matrix

# Function to encrypt plaintext
def encrypt(plaintext, key):
    key_matrix = generate_key(key)
    n = len(key_matrix)
    plaintext = plaintext.replace(" ", "").upper()
    while len(plaintext) % n != 0:
        plaintext += 'X'  # padding if necessary
    ciphertext = ""
    for i in range(0, len(plaintext), n):
        block = np.zeros((n, 1), dtype=int)
        for j in range(n):
            block[j][0] = ord(plaintext[i + j]) - ord('A')
        encrypted_block = np.dot(key_matrix, block) % 26
        for j in range(n):
            ciphertext += chr(encrypted_block[j][0] + ord('A'))
    return ciphertext

# Function to find multiplicative inverse of a number
def multiplicative_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None

# Function to decrypt ciphertext
def decrypt(ciphertext, key):
    key_matrix = generate_key(key)
    n = len(key_matrix)
    det = int(np.round(np.linalg.det(key_matrix)))
    det_inv = multiplicative_inverse(det, 26)
    if det_inv is None:
        return "Inverse does not exist. Key is not invertible."
    inverse_matrix = np.round(det_inv * np.linalg.inv(key_matrix) * det) % 26
    inverse_matrix = inverse_matrix.astype(int)  # Convert to integers
    decrypted_text = ""
    for i in range(0, len(ciphertext), n):
        block = np.zeros((n, 1), dtype=int)
        for j in range(n):
            block[j][0] = ord(ciphertext[i + j]) - ord('A')
        decrypted_block = np.dot(inverse_matrix, block) % 26
        for j in range(n):
            decrypted_text += chr(decrypted_block[j][0] + ord('A'))
    return decrypted_text

# Example usage
key = "HILL"
plaintext = "APADJTFTWLFJ"
encrypted_text = encrypt(plaintext, key)
print("Encrypted:", encrypted_text)

decrypted_text = decrypt(plaintext, key)
print("Decrypted:", decrypted_text)
