def generate_key_matrix(key):
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    matrix = []
    for char in key.upper():
        if char not in matrix and char in alphabet:
            matrix.append(char)

    for char in alphabet:
        if char not in matrix:
            matrix.append(char)

    matrix_5x5 = [matrix[i:i + 5] for i in range(0, len(matrix), 5)]
    print("\nKey Matrix:")
    for row in matrix_5x5:
        print(row)
    return matrix_5x5

def preprocess_text(text):
    text = text.upper().replace("J", "I").replace(" ", "")
    processed_text = ""
    i = 0
    while i < len(text):
        a = text[i]
        processed_text += a
        if i + 1 < len(text) and a == text[i + 1]:
            processed_text += 'X'
            i += 1  # Skip the next character as it's a duplicate
        i += 1
    if len(processed_text) % 2 != 0:
        processed_text += 'X'
    print("\nPreprocessed Text:", processed_text)
    return processed_text

def find_position(letter, matrix):
    for i, row in enumerate(matrix):
        for j, char in enumerate(row):
            if char == letter:
                return i, j
    return None, None

def encrypt_bigram(bigram, matrix):
    a, b = bigram
    a_row, a_col = find_position(a, matrix)
    b_row, b_col = find_position(b, matrix)

    encrypted_bigram = ''
    if a_row == b_row:
        encrypted_bigram = matrix[a_row][(a_col + 1) % 5] + matrix[b_row][(b_col + 1) % 5]
    elif a_col == b_col:
        encrypted_bigram = matrix[(a_row + 1) % 5][a_col] + matrix[(b_row + 1) % 5][b_col]
    else:
        encrypted_bigram = matrix[a_row][b_col] + matrix[b_row][a_col]

    print(f"\nEncrypting Bigram: {bigram} -> {encrypted_bigram}")
    return encrypted_bigram

def encrypt_playfair(text, key):
    matrix = generate_key_matrix(key)
    processed_text = preprocess_text(text)
    encrypted_text = ""

    for i in range(0, len(processed_text), 2):
        bigram = processed_text[i:i + 2]
        encrypted_text += encrypt_bigram(bigram, matrix)

    return encrypted_text

# Example usage
plaintext = input("Type the text you want to encrypt: ")
key = input("Enter the key you wish to use: ")
encrypted = encrypt_playfair(plaintext, key)
print("\n@@@@@@ Encrypted Text:", encrypted, " @@@@@@\n")
