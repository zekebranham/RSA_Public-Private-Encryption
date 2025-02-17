import random
import math
import sympy  # Import sympy for prime checking
"""Marlon Branham"""

def generate_prime(bits=512):
    """Generate a random prime number of the specified bit length."""
    while True:
        num = random.getrandbits(bits) | 1  # Ensure it's odd
        if sympy.isprime(num):  # Verify it's prime
            return num

def generate_rsa_keys(bit_size=1024):
    """Generate RSA key components p, q, n, z, e, and d."""
    p = generate_prime(bit_size // 2)
    q = generate_prime(bit_size // 2)
    while q == p:  # Ensure p and q are different
        q = generate_prime(bit_size // 2)
    n = p * q
    z = (p - 1) * (q - 1)
    # Choose e such that 1 < e < z and gcd(e, z) = 1
    e = random.randint(2, z - 1)
    while math.gcd(e, z) != 1:
        e = random.randint(2, z - 1)
    # Compute d as modular inverse of e mod z
    d = pow(e, -1, z)
    return p, q, n, z, e, d

def encrypt(Message, PubK):
    max_block_size = (PubK[1].bit_length() // 8) - 1
    message_bytes = Message.encode()
    # Split into blocks
    blocks = [message_bytes[i:i + max_block_size] for i in range(0, len(message_bytes), max_block_size)]
    # Convert each block to an integer and encrypt it
    encrypted_blocks = [pow(int.from_bytes(block, 'big'), PubK[0], PubK[1]) for block in blocks]
    return encrypted_blocks

def decrypt(encrypted_blocks, PrivK):
    #Decrypts blocks and reconstructs the original message.
    decrypted_blocks = [pow(block, PrivK[0], PrivK[1]) for block in encrypted_blocks]
    # Convert decrypted integers back to bytes
    message_bytes = b''.join(block.to_bytes((block.bit_length() + 7) // 8, 'big') for block in decrypted_blocks)    
    #convert bytes back to string
    return message_bytes.decode()


# Generate RSA key components
p, q, n, z, e, d = generate_rsa_keys()
PubK = [e,n]
PrivK = [d,n]

Message = input("Input alphabetic message to encrypt with RSA: ") #you can input anything you want really, but for the Lab, I have this label
encrypted_blocks = encrypt(Message, PubK)
Plaintext = decrypt(encrypted_blocks, PrivK)

# Print results
print(f"p: {p}")
print(f"q: {q}")
print(f"n: {n}")
print(f"z: {z}")
print(f"e: {e}")
print(f"d: {d}")
print(f"Message: {Message}")
for i in range (0, len(encrypted_blocks)):
    print(f"Ciphertext: {encrypted_blocks[i]}")
print(f"Plaintext: {Plaintext}")