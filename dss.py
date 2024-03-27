# if needed, the gcd function with math libary
import math

# gcd function without math libary

# def gcd(a, b):
#     while b != 0:
#         a, b = b, a % b
#     return a

# gcd function with math libary

# if needed, check GCD number

def gcd(a, b):
    return math.gcd(a, b)

def mod_inverse(a, m):
    return pow(a, -1, m)


# if needed, check prime number

def is_prime(n):
    return n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))

def generate_keypair(p, q, e):

    # validation of p q if needed, check prime number

    if not is_prime(p):
        raise ValueError("p must be a prime number.")
    elif not is_prime(q):
        raise ValueError("q must be a prime number.")
    elif p == q:
        raise ValueError("p and q cannot be equal.")

    n = p * q
    phi = (p - 1) * (q - 1)

    # if needed, check coprime number

    if gcd(e, phi) != 1:
        raise ValueError("e is not coprime with phi.")

    d = mod_inverse(e, phi)
    return ((e, n), (d, n))

def sign(message, private_key):
    d, n = private_key
    signature = pow(message, d, n) 
    return signature

def verify(signature, message, public_key):
    e, n = public_key
    decrypted_signature = pow(signature, e, n)

    print("Decrypted message:", decrypted_signature)
    return decrypted_signature == message

# Example usage
p = int(input("Enter first prime number: ")) # It must be a prime number. 
q = 53 # It must be a prime number. 
e = 65537 # It must be a coprime number with phi. 

public_key, private_key = generate_keypair(p, q, e) 

message = 12

signature = sign(message, private_key)
print("Message:", message)
print("Signature:", signature)

verified = verify(signature, message, public_key)
print("Signature verified status:", verified)
