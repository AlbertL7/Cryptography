# Import necessary functions from other scripts if required
# from key_generation import generate_keypair

def decrypt(ciphertext, private_key):
    d, n = private_key
    ciphertext = int(ciphertext)
    message_as_int = pow(ciphertext, d, n)
    message = message_as_int.to_bytes((message_as_int.bit_length() + 7) // 8, 'big').decode('utf-8')
    return message

# Example usage
if __name__ == "__main__":
    # Assuming you have a way to get or generate a private key
    # _, private_key = generate_keypair(100)
   d_value = int(input("Enter the Private Key Value for 'd': "))
   n_value = int(input("Enter the Private Key Value for 'n': "))
   
   private_key = (d_value, n_value)  # Replace with actual values
   

    # You will need the ciphertext from the encryption process
   ciphertext = input("Enter the Encrypted Message to Decode: ")
   decrypted_message = decrypt(ciphertext, private_key)
   print("Decrypted:", decrypted_message)

   