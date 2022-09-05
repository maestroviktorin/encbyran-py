from actions import *


def decryptograph(file_name: str, decryptor_file_name: str) -> object:
    """
    :param file_name: Name of the file to be decrypted according to unique standards.
    :param decryptor_file_name: Name of the file with decryption keys.

    :return: The file decrypted using the provided keys.
    """
    with open(file_name, 'rt', encoding='utf-8') as encrypted, open(decryptor_file_name, 'rt', encoding='utf-8') as decryptor, open(f"decrypted-{file_name.rstrip('.txt').lstrip('encrypted-')}.txt", 'w+', encoding='utf-8') as decrypted:
        encrypted_text = list(map(lambda line: line.strip(), encrypted.readlines()))
        decryptor_keys = [list(map(int, i)) for i in [y.strip().split() for y in decryptor.readlines()]]

        encrypted_words = []
        for word in encrypted_text:
            encrypted_words.append([])
            for symbol in word.split():
                encrypted_words[-1].append([symbol[:4], int(symbol[4:])])

        for word in range(len(decryptor_keys)):
            for symbol in range(len(decryptor_keys[word])):
                if encrypted_words[word][symbol][0] in action_plus:
                    decrypted.write(chr(encrypted_words[word][symbol][1] - decryptor_keys[word][symbol]))
                elif encrypted_words[word][symbol][0] in action_minus:
                    decrypted.write(chr(encrypted_words[word][symbol][1] + decryptor_keys[word][symbol]))
            decrypted.write(' ')


if __name__ == '__main__':
    help(decryptograph)
    decryptograph('encrypted-sample.txt', 'decryptor-for-sample.txt')
else:
    print('Module "decryptograph.py" is not a library by default')
