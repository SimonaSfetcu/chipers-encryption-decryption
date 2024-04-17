def toLowerCase(text):
    """Converts the given text to lowercase."""
    return text.lower()

def removeSpaces(text):
    """Removes spaces from the given text."""
    newText = ""
    for i in text:
        if i == " ":
            continue
        else:
            newText = newText + i
    return newText

def Diagraph(text):
    """Generates digraphs from the given text."""
    Diagraph = []
    group = 0
    for i in range(2, len(text), 2):
        Diagraph.append(text[group:i])
        group = i
    Diagraph.append(text[group:])
    return Diagraph

def FillerLetter(text):
    """Adds filler letters ('x') to the text to ensure even number of characters."""
    k = len(text)
    if k % 2 == 0:
        for i in range(0, k, 2):
            if text[i] == text[i+1]:
                new_word = text[0:i+1] + str('x') + text[i+1:]
                new_word = FillerLetter(new_word)
                break
            else:
                new_word = text
    else:
        for i in range(0, k-1, 2):
            if text[i] == text[i+1]:
                new_word = text[0:i+1] + str('x') + text[i+1:]
                new_word = FillerLetter(new_word)
                break
            else:
                new_word = text
    return new_word

def generateKeyTable(word, list1):
    """Generates the key table for the Playfair cipher."""
    key_letters = []
    for i in word:
        if i not in key_letters:
            key_letters.append(i)

    compElements = []
    for i in key_letters:
        if i not in compElements:
            compElements.append(i)
    for i in list1:
        if i not in compElements:
            compElements.append(i)

    matrix = []
    while compElements != []:
        matrix.append(compElements[:5])
        compElements = compElements[5:]

    return matrix

list1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'l', 'm',
         'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def search(mat, element1, element2=None):
    """
    Searches for elements in the key table of the Playfair cipher.

    If only one element is provided, it searches for that element.
    If two elements are provided, it searches for both elements.
    """
    # If element2 is not provided, assume we're searching for a single character
    if element2 is None:
        for i in range(5):
            for j in range(5):
                if mat[i][j] == element1:
                    return i, j
    else:
        # If element2 is provided, search for both elements in the matrix
        ele1_x, ele1_y = search(mat, element1)
        ele2_x, ele2_y = search(mat, element2)
        return ele1_x, ele1_y, ele2_x, ele2_y

def encrypt_RowRule(matr, e1r, e1c, e2r, e2c):
    """Applies encryption rule for characters in the same row."""
    char1 = ''
    if e1c == 4:
        char1 = matr[e1r][0]
    else:
        char1 = matr[e1r][e1c+1]

    char2 = ''
    if e2c == 4:
        char2 = matr[e2r][0]
    else:
        char2 = matr[e2r][e2c+1]

    return char1, char2

def encrypt_ColumnRule(matr, e1r, e1c, e2r, e2c):
    """Applies encryption rule for characters in the same column."""
    char1 = ''
    if e1r == 4:
        char1 = matr[0][e1c]
    else:
        char1 = matr[e1r+1][e1c]

    char2 = ''
    if e2r == 4:
        char2 = matr[0][e2c]
    else:
        char2 = matr[e2r+1][e2c]

    return char1, char2

def encrypt_RectangleRule(matr, e1r, e1c, e2r, e2c):
    """Applies encryption rule for characters forming a rectangle."""
    char1 = ''
    char1 = matr[e1r][e2c]

    char2 = ''
    char2 = matr[e2r][e1c]

    return char1, char2

def encryptByPlayfairCipher(Matrix, plainList):
    """Encrypts plaintext using the Playfair cipher."""
    CipherText = []
    for i in range(0, len(plainList)):
        
        if len(plainList[i]) < 2:
            continue
        # Proceed with encryption

        c1 = 0
        c2 = 0
        ele1_x, ele1_y = search(Matrix, plainList[i][0])
        ele2_x, ele2_y = search(Matrix, plainList[i][1])

        if ele1_x == ele2_x:
            c1, c2 = encrypt_RowRule(Matrix, ele1_x, ele1_y, ele2_x, ele2_y)
        elif ele1_y == ele2_y:
            c1, c2 = encrypt_ColumnRule(Matrix, ele1_x, ele1_y, ele2_x, ele2_y)
        else:
            c1, c2 = encrypt_RectangleRule(Matrix, ele1_x, ele1_y, ele2_x, ele2_y)

        cipher = c1 + c2
        CipherText.append(cipher)
    return CipherText

def decrypt(str, keyT):
    """Decrypts ciphertext using the Playfair cipher."""
    ps = len(str)
    i = 0
    while i < ps:
        a = search(keyT, str[i], str[i+1])
        if a[0] == a[2]:
            str = str[:i] + keyT[a[0]][(a[1]-1) % 5] + keyT[a[0]][(a[3]-1) % 5] + str[i+2:]
        elif a[1] == a[3]:
            str = str[:i] + keyT[(a[0]-1) % 5][a[1]] + keyT[(a[2]-1) % 5][a[1]] + str[i+2:]
        else:
            str = str[:i] + keyT[a[0]][a[3]] + keyT[a[2]][a[1]] + str[i+2:]
        i += 2

    return str

def decryptByPlayfairCipher(str, key):
    """Decrypts ciphertext using the Playfair cipher."""
    ks = len(key)
    key = removeSpaces(toLowerCase(key))
    str = removeSpaces(toLowerCase(str))
    keyT = generateKeyTable(key, list1)
    return decrypt(str, keyT)

def encrypt(text, key):
    """
    Encrypts the given text using the Playfair cipher with the provided key.

    Parameters:
        text (str): The text to be encrypted.
        key (str): The encryption key.

    Returns:
        str: The encrypted text.
    """
    if not text or not key:
        raise ValueError("Text and key must not be empty.")

    # Implementation of the encryption algorithm
    plain_text = removeSpaces(toLowerCase(text))
    PlainTextList = Diagraph(FillerLetter(plain_text))
    if len(PlainTextList[-1]) != 2:
        PlainTextList[-1] = PlainTextList[-1]+'z'

    key = toLowerCase(key)
    Matrix = generateKeyTable(key, list1)

    CipherList = encryptByPlayfairCipher(Matrix, PlainTextList)
 
    CipherText = ""
    for i in CipherList:
        CipherText += i
    return CipherText
