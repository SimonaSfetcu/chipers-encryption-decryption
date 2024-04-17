# chipers-encryption-decryption
Cipher GUI Application

# Overview

The Cipher GUI Application is a Python-based graphical user interface (GUI) program that allows users to encrypt and decrypt text using various ciphers. It provides a user-friendly interface for selecting different ciphers, entering text and encryption keys, and viewing the encrypted/decrypted results.

# Features

Supports multiple ciphers, including Caesar, Vigenere, Atbash, Keyword, and Playfair.
Provides options for both encryption and decryption.
Allows customization of encryption parameters such as shift value for the Caesar cipher and keyword for the Keyword cipher.
Includes error handling and input validation to ensure smooth operation.

# Usage

### Installation
Ensure you have Python installed on your system.
Clone or download the project repository from GitHub to your local machine.
### Running the Application
Navigate to the project directory in the terminal/command prompt.
Run the cipher.py script using Python.

The Cipher Selection window will appear, allowing you to choose the desired cipher.
Enter the text and encryption key (if required) in the respective input fields.
Click the "Encrypt" or "Decrypt" button to perform the operation.
The result will be displayed in the text area below.

# Documentation Structure

* CipherWindow Class: Represents the main window of the application and handles cipher selection.
* select_cipher Method: Handles the selection of a cipher and opens a new window for it.
* display_cipher_window Method: Displays a window for the selected cipher with input fields and buttons.
* on_close Method: Handles closing of the cipher window.
* back Method: Allows users to go back to the cipher selection window.
* encrypt Method: Encrypts the entered text based on the selected cipher.
* decrypt Method: Decrypts the entered text based on the selected cipher.
  
## Dependencies

* Python 3.x
* tkinter library (built-in with Python)
## Known Issues

None at the moment.
## Future Enhancements

* Addition of more ciphers such as Rail Fence, Transposition, etc.
* Improvement of user interface design and layout.
* Implementation of more advanced encryption techniques.
* Support for file encryption and decryption.

## Authors

Simona Sfetcu

# License

This project is licensed under the MIT License.


