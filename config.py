# Main------------------------------------------------------------------------

# 0 - Encryption mode.
# 1 - Decryption mode.
mode: int = ...


# Cryptograph-----------------------------------------------------------------

# Name of (path to) the file you want to encrypt.
file_to_encrypt: str = '...'

# Should the text be converted to lowercase?
to_lower: bool = False

# Should the punctuation characters be deleted from the edges of the words?
rm_punctuation: bool = False

# Range between `min` and `max` random shift of the ASCII letter number.
shift: tuple[int, int] = (1, 200)

# Range of length of a pseudo-word representing a new line.
encrypted_new_line_length: tuple[int, int] = (1, 15)


# Decryptograph---------------------------------------------------------------

# Name of (path to) the file you want to decrypt.
file_to_decrypt: str = '...'

# Name of (path to) the decryptor for the encrypted file.
decryptor: str = '...'


# Actions---------------------------------------------------------------------

# Range of random length of a random combination of letters.
length: tuple[int, int] = (1, 20)

# APPROXIMATE amount of the `plus` and `minus` words.
amount_of_words: int = 20
