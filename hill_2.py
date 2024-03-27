# Function to generate key matrix
def generate_key_matrix(key, n):
    key_matrix = [[0] * n for _ in range(n)]
    k = 0
    for i in range(n):
        for j in range(n):
            key_matrix[i][j] = ord(key[k]) % 65
            k += 1
    return key_matrix

# Function to encrypt plaintext
def encrypt(plaintext, key_matrix, n):
    plaintext = plaintext.upper().replace(" ", "")
    if len(plaintext) % n != 0:
        plaintext += 'X' * (n - (len(plaintext) % n))

    ciphertext = ""
    for i in range(0, len(plaintext), n):
        block = [ord(char) % 65 for char in plaintext[i:i+n]]

        encrypted_block = []
        for row in key_matrix:
            encrypted_char = sum(row[j] * block[j] for j in range(n)) % 26
            encrypted_block.append(encrypted_char)

        ciphertext += ''.join(chr(char + 65) for char in encrypted_block)
    return ciphertext

# Function to decrypt ciphertext
def decrypt(ciphertext, key_matrix, n):
    det = key_matrix[0][0] * key_matrix[1][1] - key_matrix[0][1] * key_matrix[1][0]
    det %= 26
    mul_inv = None
    for i in range(26):
        if (det * i) % 26 == 1:
            mul_inv = i
            break

    if mul_inv is None:
        return "Invalid key, inverse does not exist!"

    inv_key_matrix = [[0] * n for _ in range(n)]
    inv_key_matrix[0][0] = mul_inv * key_matrix[1][1] % 26
    inv_key_matrix[0][1] = -mul_inv * key_matrix[0][1] % 26
    inv_key_matrix[1][0] = -mul_inv * key_matrix[1][0] % 26
    inv_key_matrix[1][1] = mul_inv * key_matrix[0][0] % 26

    plaintext = ""
    for i in range(0, len(ciphertext), n):
        block = [ord(char) % 65 for char in ciphertext[i:i+n]]

        decrypted_block = []
        for row in inv_key_matrix:
            decrypted_char = sum(row[j] * block[j] for j in range(n)) % 26
            decrypted_block.append(decrypted_char)

        plaintext += ''.join(chr(char + 65) for char in decrypted_block)
    return plaintext

# Example usage
key = "HILL"
plaintext = "APADJTFTWLFJ"
n = 2  # As key length is 9, matrix size will be 2x2
key_matrix = generate_key_matrix(key, n)

# Encryption
encrypted_text = encrypt(plaintext, key_matrix, n)
print("Encrypted text:", encrypted_text)

# Decryption
decrypted_text = decrypt(plaintext, key_matrix, n)
print("Decrypted text:", decrypted_text)
