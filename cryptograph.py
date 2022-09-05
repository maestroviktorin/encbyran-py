from random import randint, choice
from string import punctuation

from actions import *


def cleared(word: str) -> str:
    """
    :param word: The word that needs to be cleared of punctuation characters at the edges.

    :return: Word without punctuation characters at the edges.
    """
    for sym in (word[0], word[-1]):
        if sym in punctuation:
            word = word.replace(sym, '')
    return word


def cryptograph(file_name: str, to_lower: bool = False, rmpunctuation: bool = True) -> object:
    """
    :param file_name: Name of the file to be encrypted.
    :param to_lower: The need to convert uppercase letters to lowercase.
    :param rmpunctuation: The need to remove punctuation characters on the edges of the words.

    :return: Creates 2 files in the current directory:
    1) Encrypted text in the format .txt with one encrypted word on each line;
    2) Decryptor with keys that can be used in Decryptograph function ONLY for received encrypted file.
    """
    with open(file_name, 'rt', encoding="utf-8") as file, open(f"encrypted-{file_name.strip('.txt')}.txt", 'w+', encoding="utf-8") as result, open(
            f"decryptor-for-{file_name.strip('.txt')}.txt", 'w+', encoding="utf-8") as decryptor:

        # origin_text: list[str] = list(map(lambda x: cleared(x), file.read().lower().split()))
        origin_text: list[str] = file.read().split()

        if to_lower:
            origin_text = list(map(lambda x: x.lower(), origin_text))

        if rmpunctuation:
            origin_text = list(map(lambda x: cleared(x), origin_text))

        for word in origin_text:
            for symbol in word:
                key, action = randint(1, 200), randint(0, 1)
                decryptor.write(str(key) + ' ')
                if action:
                    result.write(choice(action_plus) + str(ord(symbol) + key) + ' ')
                else:
                    result.write(choice(action_minus) + str(ord(symbol) - key) + ' ')
            result.write('\n')
            decryptor.write('\n')


if __name__ == '__main__':
    help(cryptograph)
    cryptograph('sample.txt', rmpunctuation=False)
else:
    print('Module "cryptograph.py" is not a library by default')
