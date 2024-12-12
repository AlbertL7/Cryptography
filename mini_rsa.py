import random
from sympy import isprime

def generate_prime_candidate(length):
    # Generate a random integer of the specified bit length
    p = random.getrandbits(length)
    # Ensure the most significant bit (MSB) and least significant bit (LSB) are set to 1
    # This makes the number odd and ensures it's of the correct bit length
    p |= (1 << length - 1) | 1
    print("Generate a random integer of the specified bit length\n", p, "\n")
    return p

def generate_prime_number(length=1024):
    p = 4
    # Loop until a prime number is found
    while not isprime(p):
        # Generate a prime candidate and check if it's prime
        p = generate_prime_candidate(length)
    print("Found Prime Number\n", p, "\n")
    return  p 

def gcd(a, b):
    # Euclidean Algorithm for finding greatest common divisor
    while b != 0:
        a, b = b, a % b
    print("Greatest Common Devisor Found!\n", a, b, "\n")
    return a

def multiplicative_inverse(e, phi):
    # Extended Euclidean Algorithm for finding the multiplicative inverse
    d, x1, x2, y1 = 0, 0, 1, 1
    temp_phi = phi
    
    while e > 0:
        temp1 = temp_phi // e
        temp2 = temp_phi - temp1 * e
        temp_phi, e = e, temp2
        
        x = x2 - temp1 * x1
        y = d - temp1 * y1
        
        x2, x1, d, y1 = x1, x, y1, y
    
    # Check if the algorithm found a result
    if temp_phi == 1:
        
        return d + phi
    print("Euclidean Algorythm, finding the multiplicative inverse\n", d + phi, "\n")
# Function to generate RSA key pairs
def generate_keypair(keysize):
    # Generate two large prime numbers p and q
    p = generate_prime_number(keysize)
    q = generate_prime_number(keysize)
    print(f"Generate Two large prime numbers\nP:{p}\nQ:{q}\n")
    # Calculate n = p * q
    n = p * q
    print("Caluculate N\n", n, "\n")
    # Calculate Euler's totient function phi(n)
    phi = (p-1) * (q-1)
    print("Calculate Euler's totient function ph\n", phi, "\n")

    # Choose an integer e such that e and phi(n) are coprime
    e = random.randrange(1, phi)
    print(e, "\n")
    g = gcd(e, phi)
    print(g, "\n")
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)
    
    # Calculate the private key d, the multiplicative inverse of e modulo phi(n)
    d = multiplicative_inverse(e, phi)
    
    # Return the public and private key pairs
    print(f"Choose an integer e such that e and phi(n) are coprime\n(E:{e},N:{n})\n(D:{d},N:{n})\n")
    return ((e, n), (d, n))

# Generate RSA key pairs
public, private = generate_keypair(100)
print("Public key:", public)
print("Private key:", private)