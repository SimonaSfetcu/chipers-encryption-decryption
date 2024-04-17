def atbash_cipher(text):
    """
    Encrypts the given text using the Atbash cipher.

    Parameters:
        text (str): The text to be encrypted.

    Returns:
        str: The encrypted text.
    """
    if not text:
        raise ValueError("Text must not be empty.")

    result = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr(90 - (ord(char) - 65))
            else:
                result += chr(122 - (ord(char) - 97))
        else:
            result += char
    return result

# Decryption function is the same as encryption function for Atbash Cipher
atbash_decipher = atbash_cipher
