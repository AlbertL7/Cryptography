# Import necessary functions from other scripts if required
# from key_generation import generate_keypair

def encrypt(message, public_key):
    e, n = public_key
    message_as_int = int.from_bytes(message.encode('utf-8'), 'big')
    ciphertext = pow(message_as_int, e, n)
    return ciphertext

# Example usage
if __name__ == "__main__":
    # Assuming you have a way to get or generate a public key
    # public_key, _ = generate_keypair(100)
    e_value = int(input("Input Public Key Value for 'e': "))
    n_value = int(input("Input public Key Value for 'n': "))

    message = input("Enter the plaintext you want to encode: ")
    public_key = (e_value, n_value)  # Replace with actual values
    encrypted_message = encrypt(message, public_key)
    print("Encrypted:", encrypted_message)

