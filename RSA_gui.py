import tkinter as tk
from tkinter import messagebox, filedialog, scrolledtext
import random
import pyperclip
from sympy import isprime

def generate_prime_candidate(length):
    p = random.getrandbits(length)
    p |= (1 << length - 1) | 1
    return p

def generate_prime_number(length=1024):
    p = 4
    while not isprime(p):
        p = generate_prime_candidate(length)
    return p 

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def multiplicative_inverse(e, phi):
    d, x1, x2, y1 = 0, 0, 1, 1
    temp_phi = phi
    
    while e > 0:
        temp1 = temp_phi // e
        temp2 = temp_phi - temp1 * e
        temp_phi, e = e, temp2
        
        x = x2 - temp1 * x1
        y = d - temp1 * y1
        
        x2, x1, d, y1 = x1, x, y1, y
    
    if temp_phi == 1:
        return d + phi
    return None

def generate_keypair(keysize):
    p = generate_prime_number(keysize)
    q = generate_prime_number(keysize)
    
    n = p * q
    phi = (p-1) * (q-1)

    e = random.randrange(1, phi)
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)
    
    d = multiplicative_inverse(e, phi)
    
    return ((e, n), (d, n))

class RSAApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("RSA Encryption/Decryption")
        
        # Set window size and make it resizable
        self.geometry("800x1000")
        self.resizable(True, True)

        # Main frame with vertical scrollbar
        main_frame = tk.Frame(self)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Scrollbar
        scrollbar = tk.Scrollbar(main_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Canvas
        canvas = tk.Canvas(main_frame, yscrollcommand=scrollbar.set)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar.config(command=canvas.yview)

        # Frame inside canvas
        inner_frame = tk.Frame(canvas)
        canvas.create_window((0, 0), window=inner_frame, anchor='nw')

        # Key Generation Section
        key_gen_frame = tk.LabelFrame(inner_frame, text="Key Generation")
        key_gen_frame.pack(padx=10, pady=10, fill=tk.X)

        generate_key_button = tk.Button(key_gen_frame, text="Generate Keys", command=self.generate_keys)
        generate_key_button.pack(pady=5)

        # Public Key Display
        public_key_label = tk.Label(key_gen_frame, text="Public Key (e, n):")
        public_key_label.pack()
        self.public_key_text = scrolledtext.ScrolledText(key_gen_frame, height=5, width=90, wrap=tk.WORD)
        self.public_key_text.pack(padx=5, pady=5)

        # Save Public Key Button
        save_public_key_button = tk.Button(key_gen_frame, text="Save Public Key", command=self.save_public_key)
        save_public_key_button.pack(pady=5)

        # Private Key Display
        private_key_label = tk.Label(key_gen_frame, text="Private Key (d, n):")
        private_key_label.pack()
        self.private_key_text = scrolledtext.ScrolledText(key_gen_frame, height=5, width=90, wrap=tk.WORD)
        self.private_key_text.pack(padx=5, pady=5)

        # Save Private Key Button
        save_private_key_button = tk.Button(key_gen_frame, text="Save Private Key", command=self.save_private_key)
        save_private_key_button.pack(pady=5)

        # Encryption Section
        encrypt_frame = tk.LabelFrame(inner_frame, text="Encryption")
        encrypt_frame.pack(padx=10, pady=10, fill=tk.X)

        # Public Key Input for Encryption
        e_label = tk.Label(encrypt_frame, text="Public Key 'e':")
        e_label.pack()
        self.e_entry = tk.Entry(encrypt_frame, width=90)
        self.e_entry.pack(padx=5, pady=5)

        n_label = tk.Label(encrypt_frame, text="Public Key 'n':")
        n_label.pack()
        self.n_entry = tk.Entry(encrypt_frame, width=90)
        self.n_entry.pack(padx=5, pady=5)

        message_label = tk.Label(encrypt_frame, text="Message to Encrypt:")
        message_label.pack()
        self.message_entry = tk.Entry(encrypt_frame, width=90)
        self.message_entry.pack(padx=5, pady=5)

        encrypt_button = tk.Button(encrypt_frame, text="Encrypt", command=self.encrypt_message)
        encrypt_button.pack(pady=5)

        # Encrypted Message Display
        self.encrypted_message_text = scrolledtext.ScrolledText(encrypt_frame, height=5, width=90, wrap=tk.WORD)
        self.encrypted_message_text.pack(padx=5, pady=5)

        # Save Encrypted Message Button
        save_encrypted_button = tk.Button(encrypt_frame, text="Save Encrypted Message", command=self.save_encrypted_message)
        save_encrypted_button.pack(pady=5)

        # Decryption Section
        decrypt_frame = tk.LabelFrame(inner_frame, text="Decryption")
        decrypt_frame.pack(padx=10, pady=10, fill=tk.X)

        # Private Key Input for Decryption
        d_label = tk.Label(decrypt_frame, text="Private Key 'd':")
        d_label.pack()
        self.d_entry = tk.Entry(decrypt_frame, width=90)
        self.d_entry.pack(padx=5, pady=5)

        n_decrypt_label = tk.Label(decrypt_frame, text="Private Key 'n':")
        n_decrypt_label.pack()
        self.n_decrypt_entry = tk.Entry(decrypt_frame, width=90)
        self.n_decrypt_entry.pack(padx=5, pady=5)

        ciphertext_label = tk.Label(decrypt_frame, text="Ciphertext to Decrypt:")
        ciphertext_label.pack()
        self.ciphertext_entry = tk.Entry(decrypt_frame, width=90)
        self.ciphertext_entry.pack(padx=5, pady=5)

        decrypt_button = tk.Button(decrypt_frame, text="Decrypt", command=self.decrypt_message)
        decrypt_button.pack(pady=5)

        # Decrypted Message Display
        self.decrypted_message_text = scrolledtext.ScrolledText(decrypt_frame, height=5, width=90, wrap=tk.WORD)
        self.decrypted_message_text.pack(padx=5, pady=5)

        # Save Decrypted Message Button
        save_decrypted_button = tk.Button(decrypt_frame, text="Save Decrypted Message", command=self.save_decrypted_message)
        save_decrypted_button.pack(pady=5)

        # Update scroll region
        inner_frame.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))

    def generate_keys(self):
        public, private = generate_keypair(1024)
        self.public_key_text.delete('1.0', tk.END)
        self.private_key_text.delete('1.0', tk.END)
        
        public_key_str = f"Public Key:\n  e: {public[0]}\n  n: {public[1]}"
        self.public_key_text.insert(tk.END, public_key_str)

        private_key_str = f"Private Key:\n  d: {private[0]}\n  n: {private[1]}"
        self.private_key_text.insert(tk.END, private_key_str)

    def save_public_key(self):
        file = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
        if file:
            public_key = self.public_key_text.get('1.0', tk.END)
            file.write(public_key)
            file.close()

    def save_private_key(self):
        file = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
        if file:
            private_key = self.private_key_text.get('1.0', tk.END)
            file.write(private_key)
            file.close()

    def encrypt_message(self):
        try:
            e = int(self.e_entry.get())
            n = int(self.n_entry.get())
            message = self.message_entry.get()
            encrypted_message = self.encrypt(message, (e, n))
            
            # Clear previous content
            self.encrypted_message_text.delete('1.0', tk.END)
            # Insert encrypted message
            self.encrypted_message_text.insert(tk.END, str(encrypted_message))
            
            # Copy to clipboard
            pyperclip.copy(str(encrypted_message))
            messagebox.showinfo("Success", "Encrypted message copied to clipboard!")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid public key and message")

    def decrypt_message(self):
        try:
            d = int(self.d_entry.get())
            n = int(self.n_decrypt_entry.get())
            ciphertext = self.ciphertext_entry.get()
            decrypted_message = self.decrypt(ciphertext, (d, n))
            
            # Clear previous content
            self.decrypted_message_text.delete('1.0', tk.END)
            # Insert decrypted message
            self.decrypted_message_text.insert(tk.END, decrypted_message)
        except ValueError:
            messagebox.showerror("Error", "Please enter valid private key and ciphertext")

    @staticmethod
    def encrypt(message, public_key):
        e, n = public_key
        message_as_int = int.from_bytes(message.encode('utf-8'), 'big')
        ciphertext = pow(message_as_int, e, n)
        return ciphertext

    @staticmethod
    def decrypt(ciphertext, private_key):
        d, n = private_key
        ciphertext = int(ciphertext)
        message_as_int = pow(ciphertext, d, n)
        message = message_as_int.to_bytes((message_as_int.bit_length() + 7) // 8, 'big').decode('utf-8')
        return message

    def save_encrypted_message(self):
        file = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
        if file:
            encrypted_message = self.encrypted_message_text.get('1.0', tk.END).strip()
            file.write(encrypted_message)
            file.close()

    def save_decrypted_message(self):
        file = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
        if file:
            decrypted_message = self.decrypted_message_text.get('1.0', tk.END).strip()
            file.write(decrypted_message)
            file.close()

# Run the application
if __name__ == "__main__":
    app = RSAApp()
    app.mainloop()