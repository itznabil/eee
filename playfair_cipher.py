def prepare_input(text):
    # Make sure the input text is all uppercase
    text = text.upper()
    # Remove any non-alphabetic characters
    text = ''.join(filter(str.isalpha, text))
    # Replace 'J' with 'I'
    text = text.replace('J', 'I')
    return text

def generate_table(key):
    # Create a matrix (5x5) to hold the Playfair cipher table
    table = [['' for _ in range(5)] for _ in range(5)]
    # Initialize variables
    alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'  # Note: 'J' is removed
    key = prepare_input(key)
    key_index = 0
    # Fill the table with the keyword
    for i in range(5):
        for j in range(5):
            if key_index < len(key):
                table[i][j] = key[key_index]
                alphabet = alphabet.replace(key[key_index], '')
                key_index += 1
            else:
                break
    # Fill the remaining cells with the remaining alphabet
    for i in range(5):
        for j in range(5):
            if table[i][j] == '':
                table[i][j] = alphabet[0]
                alphabet = alphabet[1:]
    return table

def get_char_positions(table, char):
    # Find the positions of a given character in the table
    positions = []
    for i in range(5):
        for j in range(5):
            if table[i][j] == char:
                positions.append((i, j))
    return positions

def encrypt(text, key):
    table = generate_table(key)
    text = prepare_input(text)
    # Handle double letters by inserting 'X' between them
    for i in range(0, len(text)-1, 2):
        if text[i] == text[i+1]:
            text = text[:i+1] + 'X' + text[i+1:]
    # If the text length is odd, append 'X' to make it even
    if len(text) % 2 != 0:
        text += 'X'
    # Encrypt the text
    cipher = ''
    for i in range(0, len(text), 2):
        char1, char2 = text[i], text[i+1]
        row1, col1 = get_char_positions(table, char1)[0]
        row2, col2 = get_char_positions(table, char2)[0]
        # Handle the cases when the letters are in the same row or column
        if row1 == row2:
            cipher += table[row1][(col1 + 1) % 5]
            cipher += table[row2][(col2 + 1) % 5]
        elif col1 == col2:
            cipher += table[(row1 + 1) % 5][col1]
            cipher += table[(row2 + 1) % 5][col2]
        else:
            cipher += table[row1][col2]
            cipher += table[row2][col1]
    return cipher

def decrypt(cipher, key):
    table = generate_table(key)
    # Decrypt the text
    plain_text = ''
    for i in range(0, len(cipher), 2):
        char1, char2 = cipher[i], cipher[i+1]
        row1, col1 = get_char_positions(table, char1)[0]
        row2, col2 = get_char_positions(table, char2)[0]
        # Handle the cases when the letters are in the same row or column
        if row1 == row2:
            plain_text += table[row1][(col1 - 1) % 5]
            plain_text += table[row2][(col2 - 1) % 5]
        elif col1 == col2:
            plain_text += table[(row1 - 1) % 5][col1]
            plain_text += table[(row2 - 1) % 5][col2]
        else:
            plain_text += table[row1][col2]
            plain_text += table[row2][col1]
    return plain_text

# Example usage:
key = "computer"
plaintext = "communication"

encrypted_text = encrypt(plaintext, key)
print("Encrypted:", encrypted_text)

decrypted_text_filler = decrypt(encrypted_text, key)
decrypted_text = decrypted_text_filler.replace("X", "")
print("Decrypted:", decrypted_text)
