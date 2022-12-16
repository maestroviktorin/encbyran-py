# Cryptograph.

file_to_encrypt: str = '../ ...'  # Path to the file you want to encrypt.

to_lower: bool = False  # Should the text be converted to lowercase?
rm_punctuation: bool = True  # Should the punctuation characters be deleted from the edges of the words?
shift: tuple[int, int] = (1, 200)  # Range between `min` and `max` random shift of the ASCII letter number.


# Decryptograph.

# TODO: Implement configuration for decryptograph.


# Actions.

length: tuple[int, int] = (1, 20)
amount_of_words: int = 20  # APPROXIMATE amount of the `plus` and `minus` words.
