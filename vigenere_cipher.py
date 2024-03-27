def extend_keyword(keyword, length):
    repeats = length // len(keyword)
    remainder = length % len(keyword)
    extended_keyword = keyword * repeats + keyword[:remainder]
    return extended_keyword

def vigenere_encrypt(plaintext, keyword):
    encrypted_text = ""
    if len(plaintext) != len(keyword):
        keyword = extend_keyword(keyword, len(plaintext))
    for i in range(len(plaintext)):
        if plaintext[i].isalpha():
            shift = ord(keyword[i].upper()) - 65
            if plaintext[i].islower():
                encrypted_text += chr((ord(plaintext[i]) - 97 + shift) % 26 + 97)
            else:
                encrypted_text += chr((ord(plaintext[i]) - 65 + shift) % 26 + 65)
        else:
            encrypted_text += plaintext[i]
    return encrypted_text

def vigenere_decrypt(ciphertext, keyword):
    decrypted_text = ""
    keyword = extend_keyword(keyword, len(ciphertext))
    for i in range(len(ciphertext)):
        if ciphertext[i].isalpha():
            shift = ord(keyword[i].upper()) - 65
            if ciphertext[i].islower():
                decrypted_text += chr((ord(ciphertext[i]) - 97 - shift) % 26 + 97)
            else:
                decrypted_text += chr((ord(ciphertext[i]) - 65 - shift) % 26 + 65)
        else:
            decrypted_text += ciphertext[i]
    return decrypted_text

# Example usage: key and plaintext will be same length
plaintext = input("enter your message:")
keyword = input("enter your key:")

encrypted_text = vigenere_encrypt(plaintext, keyword)
print("Encrypted:", encrypted_text)

decrypted_text = vigenere_decrypt(encrypted_text, keyword)
print("Decrypted:", decrypted_text)
