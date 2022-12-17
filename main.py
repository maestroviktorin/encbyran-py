from encbyran import *
from config import *


if __name__ == '__main__':
    match mode:
        case 0:
            help(cryptograph)
            cryptograph(file_to_encrypt, to_lower, rm_punctuation, shift)
        case 1:
            help(decryptograph)
            decryptograph(file_to_decrypt, decryptor)
        case _:
            raise RuntimeError(f'There is no mode {mode}.')
