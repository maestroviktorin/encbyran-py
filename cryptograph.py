from random import randint, choice
from string import punctuation

from actions_for_encryption import *


def cleared(word: str) -> str:
    """
    :param word: Takes in a word.

    :return: Word without punctuation-symbols at the edges.
    """
    for sym in (word[0], word[-1]):
        if sym in punctuation:
            word = word.replace(sym, '')
    return word


def cryptograph(file_name: str) -> object:
    """
    :param file_name: Name of the file to be encrypted (all the words in the file are converted to lower case and get rid of any punctuation characters at the edges)

    :return: Creating 2 files:
    1) Encrypted text in the format .txt with one encrypted word on each line;
    2) Decryptor with keys that can be used in Decryptograph function ONLY for received encrypted file
    """
    with open(file_name, 'rt', encoding="utf-8") as file, open("encrypted.txt", 'w+', encoding="utf-8") as result, open(
            "decryptor.txt", 'w+', encoding="utf-8") as decryptor:

        origin_text: list[str] = list(map(lambda x: cleared(x), file.read().lower().split()))

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
    cryptograph('sample.txt')
else:
    print('Module is not a library by default')
