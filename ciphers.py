import tkinter as tk
from tkinter import simpledialog
import caesar_cipher
import vigenere_cipher
import atbash_cipher
import keyword_cipher
import playfair_cipher as playfair

class CipherWindow:
    def __init__(self, root):
        # Initialize the main window
        self.root = root
        self.root.title("Cipher Selection")
        self.root.geometry("800x500")

        # Create a label for selecting a cipher
        self.cipher_label = tk.Label(root, text="Select a cipher:", font=("Arial", 24))
        self.cipher_label.pack(pady=20)

        # Create buttons for each cipher
        self.caesar_button = tk.Button(root, text="Caesar", command=lambda: self.select_cipher("Caesar"), font=("Arial", 20))
        self.caesar_button.pack(pady=10)

        self.vigenere_button = tk.Button(root, text="Vigenere", command=lambda: self.select_cipher("Vigenere"), font=("Arial", 20))
        self.vigenere_button.pack(pady=10)

        self.atbash_button = tk.Button(root, text="Atbash", command=lambda: self.select_cipher("Atbash"), font=("Arial", 20))
        self.atbash_button.pack(pady=10)

        self.keyword_button = tk.Button(root, text="Keyword", command=lambda: self.select_cipher("Keyword"), font=("Arial", 20))
        self.keyword_button.pack(pady=10)

        self.playfair_button = tk.Button(root, text="Playfair", command=lambda: self.select_cipher("Playfair"), font=("Arial", 20))
        self.playfair_button.pack(pady=10)

    def select_cipher(self, cipher_type):
        # Method to select a cipher and open a new window for it
        self.cipher_type = cipher_type
        self.root.withdraw()  # Hide the selection window
        self.display_cipher_window(cipher_type)

    def display_cipher_window(self, cipher_type):
        # Method to display a window for the selected cipher
        self.cipher_window = tk.Toplevel(self.root)
        self.cipher_window.title(f"{cipher_type} Cipher")
        self.cipher_window.geometry("800x500")
        self.cipher_window.protocol("WM_DELETE_WINDOW", self.on_close)

        # Create input fields for text and key
        input_label = tk.Label(self.cipher_window, text="Enter text:", font=("Arial", 24))
        input_label.pack()
        self.input_text = tk.Text(self.cipher_window, height=4, width=60, font=("Arial", 20))
        self.input_text.pack()

        key_label = tk.Label(self.cipher_window, text="Enter key:", font=("Arial", 24))
        key_label.pack()
        self.key_entry = tk.Entry(self.cipher_window, font=("Arial", 20))
        self.key_entry.pack()

        # Create buttons for encryption, decryption, and going back
        self.encrypt_button = tk.Button(self.cipher_window, text=f"{cipher_type} Encrypt", command=self.encrypt, bg="lightgreen", font=("Arial", 20, "bold"))
        self.encrypt_button.pack(side=tk.TOP, padx=10, pady=10)

        self.decrypt_button = tk.Button(self.cipher_window, text=f"{cipher_type} Decrypt", command=self.decrypt, bg="lightcoral", font=("Arial", 20, "bold"))
        self.decrypt_button.pack(side=tk.TOP, padx=10, pady=10)

        self.back_button = tk.Button(self.cipher_window, text="Back", command=self.back, bg="lightgrey", font=("Arial", 20, "bold"))
        self.back_button.pack(side=tk.TOP, padx=10, pady=10)

        # Create a text area to display the result
        self.result_text = tk.Text(self.cipher_window, height=4, width=80, font=("Arial", 18))
        self.result_text.pack(pady=20)

    def on_close(self):
        # Method to handle closing of the cipher window
        self.root.destroy()

    def back(self):
        # Method to go back to the selection window
        self.cipher_window.destroy()  # Close the cipher window
        self.root.deiconify()  # Show the selection window again

    def encrypt(self):
        # Method to encrypt the text
        text = self.input_text.get("1.0", "end-1c")
        key = self.key_entry.get()
        shift = None  # Initialize shift variable
        
        # Check which cipher is selected and perform encryption accordingly
        if self.cipher_type == "Caesar":
            shift = simpledialog.askinteger("Caesar Cipher", "Enter shift value for Caesar Cipher:")
        if shift is not None:
            encrypted_text = caesar_cipher.caesar_cipher(text, shift)
            self.result_text.delete("1.0", tk.END)
            self.result_text.insert(tk.END, f"Encrypted Text: {encrypted_text}, Key: {shift}")
        elif self.cipher_type == "Vigenere":
            encrypted_text = vigenere_cipher.vigenere_cipher(text, key)
            self.result_text.delete("1.0", tk.END)
            self.result_text.insert(tk.END, f"Encrypted Text: {encrypted_text}, Key: {key}")
        elif self.cipher_type == "Atbash":
            encrypted_text = atbash_cipher.atbash_cipher(text)
            self.result_text.delete("1.0", tk.END)
            self.result_text.insert(tk.END, f"Encrypted Text: {encrypted_text}")
        elif self.cipher_type == "Keyword":
            encrypted_text = keyword_cipher.keyword_cipher(text, key)
            self.result_text.delete("1.0", tk.END)
            self.result_text.insert(tk.END, f"Encrypted Text: {encrypted_text}, Key: {key}")
        elif self.cipher_type == "Playfair":
            encrypted_text = playfair.encrypt(text, key)
            self.result_text.delete("1.0", tk.END)
            self.result_text.insert(tk.END, f"Encrypted Text: {encrypted_text}, Key: {key}")

    def decrypt(self):
        # Method to decrypt the text
        text = self.input_text.get("1.0", "end-1c")
        key = self.key_entry.get()
        
        # Check which cipher is selected and perform decryption accordingly
        if self.cipher_type == "Caesar":
            shift = simpledialog.askinteger("Caesar Cipher", "Enter shift value for Caesar Cipher:")
            if shift is not None:
                decrypted_text = caesar_cipher.caesar_decipher(text, shift)
                self.result_text.delete("1.0", tk.END)
                self.result_text.insert(tk.END, f"Decrypted Text: {decrypted_text}, Key: {shift}")
        elif self.cipher_type == "Vigenere":
            decrypted_text = vigenere_cipher.vigenere_decipher(text, key)
            self.result_text.delete("1.0", tk.END)
            self.result_text.insert(tk.END, f"Decrypted Text: {decrypted_text}, Key: {key}")
        elif self.cipher_type == "Atbash":
            decrypted_text = atbash_cipher.atbash_cipher(text)
            self.result_text.delete("1.0", tk.END)
            self.result_text.insert(tk.END, f"Decrypted Text: {decrypted_text}")
        elif self.cipher_type == "Keyword":
            decrypted_text = keyword_cipher.keyword_decipher(text, key)
            self.result_text.delete("1.0", tk.END)
            self.result_text.insert(tk.END, f"Decrypted Text: {decrypted_text}, Key: {key}")
        elif self.cipher_type == "Playfair":
            decrypted_text = playfair.decryptByPlayfairCipher(text, key)
            self.result_text.delete("1.0", tk.END)
            self.result_text.insert(tk.END, f"Decrypted Text: {decrypted_text}, Key: {key}")

if __name__ == "__main__":
    root = tk.Tk()
    app = CipherWindow(root)
    root.mainloop()
