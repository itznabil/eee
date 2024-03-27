message = input("Enter the message : ")
shift = int(input("Shift : "))

encrypted_message = ""
for char in message:
    if char.isupper():
        encrypted_char = chr((ord(char) - 65 + shift) % 26 + 65)
    elif char.islower():
        encrypted_char = chr((ord(char) - 97 + shift) % 26 + 97)
    else:
        encrypted_char = char
        
    encrypted_message += encrypted_char

print(encrypted_message)


decrypted_message = ""
for char in encrypted_message:
    if char.isupper():
        decrypted_char = chr((ord(char) - 65 - shift) % 26 + 65)
    elif char.islower():
        decrypted_char = chr((ord(char) - 97 - shift) % 26 + 97)
    else:
        decrypted_char = char
    decrypted_message += decrypted_char
    
print(decrypted_message)