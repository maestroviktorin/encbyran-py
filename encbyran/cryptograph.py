from random import randint, choice
from typing import TextIO

from .actions import action_plus, action_minus, new_line
from .cleared import cleared


def cryptograph(file_to_encrypt: str,
                to_lower: bool = False,
                rm_punctuation: bool = False,
                shift: tuple[int, int] = (1, 200),
                encrypted_new_line_length: tuple[int, int] = (1, 15)) -> None:
    """
    ### Parameters

    `file_to_encrypt`: Name of (path to) the file to be encrypted.\n
    `to_lower`: The need to convert uppercase letters to lowercase.\n
    `rm_punctuation`: The need to remove punctuation characters on the edges of the words.\n
    `shift`: Tuple of 2 integers with the range of random shift of ASCII-numbers.

    ### Actions

    Creates 2 files in the current directory:
    1. Encrypted text in the `.txt` format with one encrypted word on each line\n
    2. Decryptor with keys that can be used in Decryptograph function ONLY for received encrypted file.
    """
    with open(file_to_encrypt, 'rt', encoding="utf-8") as file, \
            open(f"encrypted-{file_to_encrypt.strip('.txt')}.txt", 'w+', encoding="utf-8") as encrypted, \
            open(f"decryptor-for-{file_to_encrypt.strip('.txt')}.txt", 'w+', encoding="utf-8") as decryptor:

        origin_lines: tuple[tuple[str, ...], ...] = \
            tuple(map(lambda line: tuple(line.split()), file.readlines()))

        if to_lower:
            origin_lines = (tuple(map(lambda word: word.lower(), line))
                            for line in origin_lines)

        if rm_punctuation:
            origin_lines = (tuple(map(lambda word: cleared(word), line))
                            for line in origin_lines)

        min_shift, max_shift = shift
        try:
            randint(min_shift, max_shift)
        except ValueError:
            print(
                "Invalid `min_shift` and `max_shift` values were passed. They have been to the default values 1 and 200 respectively."
            )
            min_shift, max_shift = 1, 200

        decryptor.write(f"{action_plus}\n{action_minus}\n")

        for line in origin_lines:
            _encrypt_line(line, encrypted, decryptor,
                          shift, encrypted_new_line_length)


def _encrypt_line(line: tuple[str, ...],
                  encrypted: TextIO,
                  decryptor: TextIO,
                  shift: tuple[int, int],
                  encrypted_new_line_length: tuple[int, int]) -> None:
    """
    ### Parameters

    `line`: Line of the file represented as a tuple of words.\n
    `encrypted`: File in which encrypted data is being written.\n
    `decryptor`: File in which decryption keys are being written.\n
    `shift`: Range between minimum and maximum random shift of the ASCII letter number.\n
    `encrypted_new_line_length`: Range between minimum and maximum random length of an encrypted new line in so-called units.

    ### Actions

    Calls `_encrypt_word` for each word in `line` and encrypts switch to a new line.
    """
    for word in line:
        _encrypt_word(word, encrypted, decryptor, shift)

    encrypted_new_line = _get_encrypted_new_line(
        encrypted_new_line_length, shift)

    encrypted.write(encrypted_new_line + '\n')
    decryptor.write('0\n')


def _encrypt_word(word: str,
                  encrypted: TextIO,
                  decryptor: TextIO,
                  shift: tuple[int, int]) -> None:
    """
    ### Parameters

    `word`: Single word to be encrypted.\n
    `encrypted`: File in which encrypted data is being written.\n
    `decryptor`: File in which decryption keys are being written.\n
    `shift`: Range between minimum and maximum random shift of the ASCII letter number.

    ### Actions

    Encrypts the given `word`.
    """
    for char in word:
        key, action = randint(*shift), randint(0, 1)
        decryptor.write(str(key) + ' ')

        if action:
            encrypted.write(choice(tuple(action_plus)) +
                            str(ord(char) + key) + ' ')
        else:
            encrypted.write(choice(tuple(action_minus)) +
                            str(ord(char) - key) + ' ')

    encrypted.write('\n')
    decryptor.write('\n')


def _get_encrypted_new_line(encrypted_new_line_length: tuple[int, int], shift: tuple[int, int]) -> str:
    """
    ### Parameters

    `encrypted_new_line_length`: Range between minimum and maximum random length of an encrypted new line in so-called units.\n
    `shift`: Range between minimum and maximum random shift of a phantom ASCII letter number.

    ### Returns

    Random notation of an encrypted new line as `{special letter combination}{randomly changed ASCII-number of a phantom letter}`
    random number of times which is in the `encrypted_new_line_length` range.

    E.g. `ljnTfghHJGjn-42 oiiTjjGD1337 mzlff89` consisting of 3 units (so-called encrypted letters) in which no unit represents a real letter in the file being encrypting.
    """
    new_line_units_amount = randint(*encrypted_new_line_length)
    return ' '.join(_get_encrypted_new_line_unit(shift) for _ in range(new_line_units_amount))


def _get_encrypted_new_line_unit(shift: tuple[int, int]) -> str:
    """
    ### Parameters

    `shift`: Range between minimum and maximum random shift of a phantom ASCII letter number.

    ### Returns

    Randomly generated unit of an encrypted new line.
    """
    _shift = randint(*shift)
    _shift = _shift if randint(0, 1) else -_shift
    return (new_line_notation := choice(tuple(new_line))) + str(ord(new_line_notation[randint(0, len(new_line_notation) - 1)]) + _shift)
