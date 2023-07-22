# The `decryptograph` algorithm is deprecated.
# TODO: Update `decryptograph`.

import re


def decryptograph(file_to_decrypt: str, decryptor: str) -> None:
    """
    :param file_to_decrypt: Name of (path to) the file to be decrypted according to unique standards.
    :param decryptor: Name of (path to) the file with decryption keys.

    Creates a file decrypted using the provided keys.
    """
    with open(file_to_decrypt, 'rt', encoding='utf-8') as encrypted, \
         open(decryptor, 'rt', encoding='utf-8') as decryptor, \
         open(f"decrypted-{file_to_decrypt.rstrip('.txt').lstrip('encrypted-')}.txt", 'w+', encoding='utf-8') as decrypted:
        encrypted_text = tuple(map(lambda line: line.strip(), encrypted.readlines()))

        action_plus = eval(decryptor.readline())
        action_minus = eval(decryptor.readline())
        decryptor_keys = tuple(tuple(map(int, n)) for n in [line.strip().split() for line in decryptor.readlines()])

        encrypted_words: list[list[tuple[str, str]]] = []
        for word in encrypted_text:
            encrypted_words.append([])
            
            for symbol in word.split():
                encrypted_words[-1].append((re.findall(r'[a-zA-Z]+', symbol)[0], re.findall(r'-?\d+', symbol)[0]))

        for word in range(len(decryptor_keys)):
            
            for symbol in range(len(decryptor_keys[word])):
                
                if encrypted_words[word][symbol][0] in action_plus:
                    decrypted.write(chr(int(encrypted_words[word][symbol][1]) - decryptor_keys[word][symbol]))
                
                elif encrypted_words[word][symbol][0] in action_minus:
                    decrypted.write(chr(int(encrypted_words[word][symbol][1]) + decryptor_keys[word][symbol]))
            
            decrypted.write(' ')
