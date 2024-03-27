def generate_private_keys(primitive_root, private_key, prime):
    return pow(primitive_root, private_key, prime)

def generate_shared_secret_keys(private_key, public_key, prime):
    return pow(public_key, private_key, prime)

# Example usage:
prime = 353  # Example prime number
primitive_root = 3  # Example primitive root

alice_generate_private_key = 97
bob_generate_private_key = 233

# Alice's side
alice_public_key = generate_private_keys(primitive_root, alice_generate_private_key, prime)
print("Alice's public key:", alice_public_key)

# Bob's side
bob_public_key = generate_private_keys(primitive_root, bob_generate_private_key, prime)
print("Bob's public key:", bob_public_key)

# Shared secret computation
alice_shared_secret = generate_shared_secret_keys(alice_generate_private_key, bob_public_key, prime)
bob_shared_secret = generate_shared_secret_keys(bob_generate_private_key, alice_public_key, prime)

# Both should have the same shared secret
print("Shared secret computed by Alice:", alice_shared_secret)
print("Shared secret computed by Bob:", bob_shared_secret)