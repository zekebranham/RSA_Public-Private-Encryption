RSA Cryptosystem (Python Implementation)
Author: Marlon Branham

This project is a from-scratch Python implementation of the RSA encryption algorithm, demonstrating how to:

    Generate large prime numbers
    Construct public and private RSA keys
    Encrypt and decrypt text messages using those keys

It uses the sympy library for primality testing and supports variable-length inputs, broken into encryptable blocks.
# How It Works

RSA (Rivest–Shamir–Adleman) is a widely-used asymmetric cryptosystem that relies on the difficulty of factoring large composite numbers.
🔑 Key Generation:

    Two large primes p and q are generated using sympy.isprime()
    n = p * q is the modulus
    z = (p-1)(q-1) is Euler’s totient
    e is a public exponent chosen such that gcd(e, z) = 1
    d is the modular inverse of e mod z, making it the private key

🔐 Encryption:

    Message is split into blocks of bytes
    Each block is converted to an integer
    Each integer is encrypted using cipher = block^e mod n

🔓 Decryption:

    Each encrypted block is decrypted using plaintext = cipher^d mod n
    Blocks are converted back to bytes and decoded into a string
# Why This Implementation Matters

This is a conceptual lab-style implementation meant to:

    Deepen your understanding of public-key cryptography
    Practice modular arithmetic and number theory in code
    Show real encryption/decryption cycles, not just theory

Unlike libraries like PyCrypto, this version:

    Manually implements key generation using raw math
    Shows all components (p, q, n, z, e, d) for learning and debugging
    Encrypts variable-length input using block chunking

⚠️ Security Note

This implementation is not meant for real-world secure use. It lacks:

    Padding schemes (e.g., OAEP)
    Side-channel protections
    Cryptographic key management

It’s perfect for labs, learning, and demonstrations.
