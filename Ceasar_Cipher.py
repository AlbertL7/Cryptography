import tkinter as tk
from collections import Counter
import string
import pyperclip

def caesar_cipher(text, shift):
    encrypted_text = ''
    details = ''
    original_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    shifted_alphabet = original_alphabet[shift:] + original_alphabet[:shift]

    for char in text:
        if char.isalpha():
            alphabet_index = ord(char.lower()) - ord('a')
            original_char = char
            encrypted_char = shifted_alphabet[alphabet_index] if char.islower() else shifted_alphabet[alphabet_index].upper()
            encrypted_text += encrypted_char
            details += f"{original_char} ({alphabet_index}, {original_alphabet[alphabet_index]}) -> {encrypted_char} ({alphabet_index}, {shifted_alphabet[alphabet_index]})\n"
        else:
            encrypted_text += char
    return encrypted_text, details, shift

def update_alphabets():
    input_text = entry.get().lower()
    for i in range(26):
        original_label = original_labels[i]
        shifted_label = shifted_labels[i]
        if original_alphabet[i].lower() in input_text:
            original_label.config(bg="light yellow")
        else:
            original_label.config(bg=None)
        if shifted_alphabet[i].lower() in encrypt_text().lower():
            shifted_label.config(bg="light blue")
        else:
            shifted_label.config(bg=None)

def encrypt_text():
    plaintext = entry.get()
    encrypted_message, details, shift = caesar_cipher(plaintext, 5)  # Shift changed to 5
    output_label.delete(1.0, tk.END)  # Clear previous content
    output_label.insert(tk.END, f"Encrypted Text: {encrypted_message}\n\nDetails (Shift={shift}):\n{details}")
    return encrypted_message  # Return encrypted text

def decrypt_text():
    ciphertext = entry_decrypt.get()
    decrypted_message, details, shift = caesar_cipher(ciphertext, -5)  # Decrypting by shifting back 5 positions
    output_decrypt_label.delete(1.0, tk.END)  # Clear previous content
    output_decrypt_label.insert(tk.END, f"Decrypted Text: {decrypted_message}\n\nDetails (Shift={shift}):\n{details}")
    return decrypted_message  # Return decrypted text

def reset_alphabets():
    for label in original_labels + shifted_labels:
        label.destroy()  # Delete existing labels
    
    # Recreate original alphabet labels
    for i in range(5):
        for j in range(6):
            index = i * 6 + j
            if index < 26:
                letter = original_alphabet[index]
                label = tk.Label(original_box, text=f"{letter}\n{index}", font=("Arial", 10), borderwidth=1, relief="solid", padx=10, pady=10)
                label.grid(row=i, column=j)
                original_labels.append(label)
    
    # Recreate shifted alphabet labels
    for i in range(5):
        for j in range(6):
            index = i * 6 + j
            if index < 26:
                letter = shifted_alphabet[index]
                label_shifted = tk.Label(shifted_box, text=f"{letter}\n{index}", font=("Arial", 10), borderwidth=1, relief="solid", padx=10, pady=10)
                label_shifted.grid(row=i, column=j)
                shifted_labels.append(label_shifted)

def reset_data():
    entry.delete(0, tk.END)
    entry_decrypt.delete(0, tk.END)
    output_label.delete(1.0, tk.END)
    output_decrypt_label.delete(1.0, tk.END)
    reset_alphabets()  # Reset the alphabets

def copy_text():
    encrypted_text = output_label.get(1.0, tk.END).split("Encrypted Text: ")[1].split("\n\n")[0]
    pyperclip.copy(encrypted_text)


# Function for Frequency Analysis
def frequency_analysis_gui():
    def perform_frequency_analysis():
        text = input_text.get("1.0", "end-1c")  # Get text from input field
        text = ''.join(filter(lambda x: x in string.ascii_letters, text)).lower()  # Remove non-letter characters
        letter_count = Counter(text)
        total_letters = sum(letter_count.values())
        sorted_letters = sorted(letter_count.items(), key=lambda x: x[1], reverse=True)
        
        # Display frequency analysis in the output text field
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, "Letter\t\tFrequency\tPercentage\n-----------------------------------\n")
        for letter, count in sorted_letters:
            percentage = (count / total_letters) * 100
            output_text.insert(tk.END, f"{letter}\t\t{count}\t\t{percentage:.2f}%\n")

    # Create a new window for frequency analysis
    freq_window = tk.Toplevel(root)
    freq_window.title("Frequency Analysis")

    input_label = tk.Label(freq_window, text="Enter text for Frequency Analysis:")
    input_label.pack()

    input_text = tk.Text(freq_window, wrap=tk.WORD, width=40, height=5)
    input_text.pack()

    perform_button = tk.Button(freq_window, text="Perform Analysis", command=perform_frequency_analysis)
    perform_button.pack()

    output_text = tk.Text(freq_window, wrap=tk.WORD, width=40, height=10)
    output_text.pack()

# GUI setup
root = tk.Tk()
root.title("Caesar Cipher Encryption")

frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

label = tk.Label(frame, text="Enter text to encrypt:")
label.pack()

entry = tk.Entry(frame, width=40)
entry.pack()

encrypt_button = tk.Button(frame, text="Encrypt", command=update_alphabets)
encrypt_button.pack()

# Scrollbar and scrollable text widget for output_label
output_scrollbar = tk.Scrollbar(frame)
output_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

output_label = tk.Text(frame, wrap=tk.WORD, width=40, height=10, yscrollcommand=output_scrollbar.set)
output_label.pack()

output_scrollbar.config(command=output_label.yview)

alphabet_frame = tk.Frame(root)
alphabet_frame.pack()

original_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
shifted_alphabet = 'FGHIJKLMNOPQRSTUVWXYZABCDE'  # Shifted alphabet starts at 'F'

original_title = tk.Label(alphabet_frame, text="Original Alphabet", font=("Arial", 12, "bold"))
original_title.grid(row=0, column=0, columnspan=6)

shifted_title = tk.Label(alphabet_frame, text="Shifted Alphabet", font=("Arial", 12, "bold"))
shifted_title.grid(row=0, column=8, columnspan=6)

divider = tk.Frame(alphabet_frame, width=2, bd=1, relief="sunken")
divider.grid(row=1, column=7, rowspan=6, sticky="ns", padx=5, pady=5)

original_box = tk.Frame(alphabet_frame, bd=2, relief="solid")
original_box.grid(row=2, column=0, columnspan=6, padx=5, pady=5)

shifted_box = tk.Frame(alphabet_frame, bd=2, relief="solid")
shifted_box.grid(row=2, column=8, columnspan=6, padx=5, pady=5)

original_labels = []
shifted_labels = []

for i in range(5):
    for j in range(6):
        index = i * 6 + j
        if index < 26:
            letter = original_alphabet[index]
            label = tk.Label(original_box, text=f"{letter}\n{index}", font=("Arial", 10), borderwidth=1, relief="solid", padx=10, pady=10)
            label.grid(row=i, column=j)
            original_labels.append(label)

            letter = shifted_alphabet[index]
            label_shifted = tk.Label(shifted_box, text=f"{letter}\n{index}", font=("Arial", 10), borderwidth=1, relief="solid", padx=10, pady=10)
            label_shifted.grid(row=i, column=j)
            shifted_labels.append(label_shifted)

label_decrypt = tk.Label(root, text="Enter text to decrypt:")
label_decrypt.pack()

entry_decrypt = tk.Entry(root, width=40)
entry_decrypt.pack()

decrypt_button = tk.Button(root, text="Decrypt", command=decrypt_text)
decrypt_button.pack()

output_decrypt_scrollbar = tk.Scrollbar(root)
output_decrypt_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

output_decrypt_label = tk.Text(root, wrap=tk.WORD, width=40, height=10, yscrollcommand=output_decrypt_scrollbar.set)
output_decrypt_label.pack()

output_decrypt_scrollbar.config(command=output_decrypt_label.yview)

copy_button = tk.Button(root, text="Copy Encrypted Text", command=copy_text)
copy_button.pack()

reset_button = tk.Button(root, text="Reset", command=reset_data)
reset_button.pack()

frequency_button = tk.Button(root, text="Frequency Analysis", command=frequency_analysis_gui)
frequency_button.pack()

root.mainloop()
