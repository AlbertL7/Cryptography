import secrets
import random

class UniqueCipher:
    def __init__(self, key):
        self.key = key

    def encrypt(self, message):
        encrypted_message = ""
        key_index = 0

        for char in message:
            substituted = chr(ord(char) ^ ord(self.key[key_index]))
            encrypted_message += substituted
            key_index = (key_index + 1) % len(self.key)

        padding_length = len(self.key) - len(message)
        padding = ''.join(chr(secrets.randbelow(256)) for _ in range(padding_length))
        encrypted_message += padding

        encrypted_binary = ''.join(format(ord(char), '08b') for char in encrypted_message)

        random_shift_up = secrets.randbelow(random.randint(1, 100))
        random_shift_down = secrets.randbelow(random.randint(1, 100))
        print(f"Shift Up: {random_shift_up}\nShift Down: {random_shift_down}")
        encrypted_binary_shifted_up = encrypted_binary[random_shift_up:] + encrypted_binary[:random_shift_up]
        encrypted_binary_shifted_down = encrypted_binary_shifted_up[-random_shift_down:] + encrypted_binary_shifted_up[:-random_shift_down]

        return encrypted_binary_shifted_down, random_shift_up, random_shift_down

# Example usage
key = input("Choose your key: ")
cipher = UniqueCipher(key)

plaintext = input("Enter Plaintext you want to encrypt: ")
encrypted_message, shift_up, shift_down = cipher.encrypt(plaintext)
print("Encrypted Message:", encrypted_message)
print("Original Message Length:", len(plaintext))
