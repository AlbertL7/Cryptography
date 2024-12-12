def generate_key_matrix(key):
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    matrix = []
    for char in key.upper():
        if char not in matrix and char in alphabet:
            matrix.append(char)

    for char in alphabet:
        if char not in matrix:
            matrix.append(char)

    return [matrix[i:i + 5] for i in range(0, len(matrix), 5)]

def find_position(letter, matrix):
    for i, row in enumerate(matrix):
        for j, char in enumerate(row):
            if char == letter:
                return i, j
    return None, None

def decrypt_bigram(bigram, matrix):
    a, b = bigram
    a_row, a_col = find_position(a, matrix)
    b_row, b_col = find_position(b, matrix)

    if a_row == b_row:
        return matrix[a_row][(a_col - 1) % 5] + matrix[b_row][(b_col - 1) % 5]
    elif a_col == b_col:
        return matrix[(a_row - 1) % 5][a_col] + matrix[(b_row - 1) % 5][b_col]
    else:
        return matrix[a_row][b_col] + matrix[b_row][a_col]

def decrypt_playfair(text, key):
    matrix = generate_key_matrix(key)
    decrypted_text = ""

    for i in range(0, len(text), 2):
        bigram = text[i:i + 2]
        decrypted_text += decrypt_bigram(bigram, matrix)

    return decrypted_text

# Example usage
key = input("Cipher Key: ")
encrypted_text = input("Encrypted Text: ")  # Example encrypted text
decrypted = decrypt_playfair(encrypted_text, key)
print("Decrypted Text:", decrypted)