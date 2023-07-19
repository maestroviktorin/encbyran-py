from .actions import *
from .cleared import cleared


def cryptograph(file_to_encrypt: str, to_lower: bool = False, rm_punctuation: bool = False,
                shift: tuple[int, int] = (1, 200)) -> None:
    """
    :param file_to_encrypt: Name of (path to) the file to be encrypted.
    :param to_lower: The need to convert uppercase letters to lowercase.
    :param rm_punctuation: The need to remove punctuation characters on the edges of the words.
    :param shift: Tuple of 2 integers with the range of random shift of ASCII-numbers.

    Creates 2 files in the current directory:
    1) Encrypted text in the .txt format with one encrypted word on each line;
    2) Decryptor with keys that can be used in Decryptograph function ONLY for received encrypted file.
    """
    with open(file_to_encrypt, 'rt', encoding="utf-8") as file, \
         open(f"encrypted-{file_to_encrypt.strip('.txt')}.txt", 'w+', encoding="utf-8") as encrypted, \
         open(f"decryptor-for-{file_to_encrypt.strip('.txt')}.txt", 'w+', encoding="utf-8") as decryptor:

        origin_lines: tuple[tuple[str, ...], ...] = \
            tuple(map(lambda line: tuple(line.split()), file.readlines()))

        if to_lower:
            origin_lines = (tuple(map(lambda word: word.lower(), line)) for line in origin_lines)

        if rm_punctuation:
            origin_lines = (tuple(map(lambda word: cleared(word), line)) for line in origin_lines)

        min_shift, max_shift = shift
        try:
            randint(min_shift, max_shift)
        except ValueError:
            print(
                "Invalid `min_shift` and `max_shift` values were passed. They are reset to the default values 1 and 200 respectively."
            )
            min_shift, max_shift = 1, 200

        decryptor.write(f"{action_plus}\n{action_minus}\n{new_line}")

        for line in origin_lines:
            
            for word in line:
                
                for symbol in word:
                    
                    key, action = randint(min_shift, max_shift), randint(0, 1)
                    decryptor.write(str(key) + ' ')
                    
                    if action:
                        encrypted.write(choice(action_plus) + str(ord(symbol) + key) + ' ')
                    else:
                        encrypted.write(choice(action_minus) + str(ord(symbol) - key) + ' ')
                
                encrypted.write('\n')
                decryptor.write('\n')
        
        '''
        for line in origin_lines:
            encrypt_line(line)
        '''


def encrypt_word(word: str, encrypted: str, decryptor: str) -> None:
    pass


def encrypt_line(line: tuple[str, ...], encrypted: str, decryptor: str) -> None:
    '''
    for word in line:
        encrypt_word(word, encrypted, decryptor)
    encrypted.write(choice(new_line))
    '''
    pass
