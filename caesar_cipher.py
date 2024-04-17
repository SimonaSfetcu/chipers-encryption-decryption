def caesar_cipher(text, shift):
    """
    Encrypts the given text using the Caesar cipher with the provided shift.

    Parameters:
        text (str): The text to be encrypted.
        shift (int): The shift value for encryption.

    Returns:
        str: The encrypted text.
    """
    if not text:
        raise ValueError("Text must not be empty.")

    result = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - 65 - shift) % 26 + 65)
            else:
                result += chr((ord(char) - 97 - shift) % 26 + 97)
        else:
            result += char
    return result

def caesar_decipher(text, shift):
    """
    Decrypts the given text using the Caesar cipher with the provided shift.

    Parameters:
        text (str): The text to be decrypted.
        shift (int): The shift value for decryption.

    Returns:
        str: The decrypted text.
    """
    return caesar_cipher(text, -shift)
