class UniqueCipher:
    def __init__(self, key):
        self.key = key

    def decrypt(self, encrypted_binary_shifted_down, random_shift_up, random_shift_down, message_length):
        encrypted_binary_shifted_up = encrypted_binary_shifted_down[random_shift_down:] + encrypted_binary_shifted_down[:random_shift_down]
        encrypted_binary = encrypted_binary_shifted_up[-random_shift_up:] + encrypted_binary_shifted_up[:-random_shift_up]

        decrypted_message_with_padding = ''.join(chr(int(encrypted_binary[i:i+8], 2)) for i in range(0, len(encrypted_binary), 8))

        decrypted_message = ""
        key_index = 0
        for char in decrypted_message_with_padding[:message_length]:
            original_char = chr(ord(char) ^ ord(self.key[key_index]))
            decrypted_message += original_char
            key_index = (key_index + 1) % len(self.key)

        return decrypted_message

# Example usage
key = input("Enter your key: ")
cipher = UniqueCipher(key)

encrypted_message = input("Enter Encrypted Message: ")
shift_up = int(input("Enter shift up value: "))
shift_down = int(input("Enter shift down value: "))
message_length = int(input("Enter original message length: "))

decrypted_message = cipher.decrypt(encrypted_message, shift_up, shift_down, message_length)
print("Decrypted Message:", decrypted_message)