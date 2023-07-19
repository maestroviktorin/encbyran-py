# Main------------------------------------------------------------------------

# 0 - Encryption mode.
# 1 - Decryption mode.
mode: int = 0


# Cryptograph-----------------------------------------------------------------

file_to_encrypt: str = 'sample.txt'  # Name of (path to) the file you want to encrypt.

to_lower: bool = False  # Should the text be converted to lowercase?
rm_punctuation: bool = False  # Should the punctuation characters be deleted from the edges of the words?
shift: tuple[int, int] = (1, 200)  # Range between `min` and `max` random shift of the ASCII letter number.


# Decryptograph---------------------------------------------------------------

file_to_decrypt: str = '...'  # Name of (path to) the file you want to decrypt.
decryptor: str = '...'  # Name of (path to) the decryptor for the encrypted file.


# Actions---------------------------------------------------------------------

length: tuple[int, int] = (1, 20)  # Range of random length of a random combination of letters.
amount_of_words: int = 20  # APPROXIMATE amount of the `plus` and `minus` words.
