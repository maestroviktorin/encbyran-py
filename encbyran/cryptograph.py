from .actions import *
from .cleared import cleared


def cryptograph(file_to_encrypt: str, to_lower: bool = False, rm_punctuation: bool = False,
                shift: tuple[int, int] = (1, 200)) -> None:
    """
    :param file_to_encrypt: Name of (path to) the file to be encrypted.
    :param to_lower: The need to convert uppercase letters to lowercase.
    :param rm_punctuation: The need to remove punctuation characters on the edges of the words.
    :param shift: Tuple of 2 integers with the range of random shift of ASCII-numbers.

    :return: Creates 2 files in the current directory:
    1) Encrypted text in the .txt format with one encrypted word on each line;
    2) Decryptor with keys that can be used in Decryptograph function ONLY for received encrypted file.
    """
    with open(file_to_encrypt, 'rt', encoding="utf-8") as file, open(f"encrypted-{file_to_encrypt.strip('.txt')}.txt",
                                                                     'w+', encoding="utf-8") as result, \
            open(f"decryptor-for-{file_to_encrypt.strip('.txt')}.txt", 'w+', encoding="utf-8") as decryptor:

        origin_text: list[str] = file.read().split()

        if to_lower:
            origin_text = list(map(lambda line: line.lower(), origin_text))

        if rm_punctuation:
            origin_text = list(map(lambda word_to_clear: cleared(word_to_clear), origin_text))

        minshift, maxshift = shift
        try:
            randint(minshift, maxshift)
        except ValueError:
            print(
                "Invalid `minshift` and `maxshift` values were passed. They are reset to the default values 1 and 200 respectively."
            )
            minshift, maxshift = 1, 200

        decryptor.write(f"{action_plus}\n{action_minus}\n")

        for word in origin_text:
            for symbol in word:
                key, action = randint(minshift, maxshift), randint(0, 1)
                decryptor.write(str(key) + ' ')
                if action:
                    result.write(choice(action_plus) + str(ord(symbol) + key) + ' ')
                else:
                    result.write(choice(action_minus) + str(ord(symbol) - key) + ' ')
            result.write('\n')
            decryptor.write('\n')
