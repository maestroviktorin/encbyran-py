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
        encrypted_words_origin = tuple(
            map(lambda line: line.strip(), encrypted.readlines()))

        action_plus = eval(decryptor.readline())
        action_minus = eval(decryptor.readline())

        decryptor_keys: tuple[tuple[int, ...]] = \
            tuple(tuple(map(int, n)) for n in map(
                lambda line: line.strip().split(), decryptor.readlines()))

        encrypted_words: tuple[tuple[tuple[str, str], ...], ...] = \
            tuple(tuple((re.findall(r'[a-zA-Z]+', char)[0], re.findall(r'-?\d+', char)[0])
                  for char in word.split()) for word in encrypted_words_origin)

        for word in range(len(decryptor_keys)):

            if decryptor_keys[word][0] == 0:
                decrypted.write('\n')
                continue

            for char in range(len(decryptor_keys[word])):

                if encrypted_words[word][char][0] in action_plus:
                    decrypted.write(
                        chr(int(encrypted_words[word][char][1]) - decryptor_keys[word][char]))

                elif encrypted_words[word][char][0] in action_minus:
                    decrypted.write(
                        chr(int(encrypted_words[word][char][1]) + decryptor_keys[word][char]))

            decrypted.write(' ')
