def vigenere_cipher(text, key):
    """
    Encrypts the given text using the Vigenère cipher with the provided key.

    Parameters:
        text (str): The text to be encrypted.
        key (str): The encryption key.

    Returns:
        str: The encrypted text.
    """
    if not text or not key:
        raise ValueError("Text and key must not be empty.")
    
    result = ""
    key_length = len(key)
    for i, char in enumerate(text):
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - 65 + ord(key[i % key_length].upper()) - 65) % 26 + 65)
            else:
                result += chr((ord(char) - 97 + ord(key[i % key_length].lower()) - 97) % 26 + 97)
        else:
            result += char
    return result

def vigenere_decipher(text, key):
    """
    Decrypts the given text using the Vigenère cipher with the provided key.

    Parameters:
        text (str): The text to be decrypted.
        key (str): The decryption key.

    Returns:
        str: The decrypted text.
    """
    if not text or not key:
        raise ValueError("Text and key must not be empty.")
    
    result = ""
    key_length = len(key)
    for i, char in enumerate(text):
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - 65 - (ord(key[i % key_length].upper()) - 65)) % 26 + 65)
            else:
                result += chr((ord(char) - 97 - (ord(key[i % key_length].lower()) - 97)) % 26 + 97)
        else:
            result += char
    return result
