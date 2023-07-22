from encbyran import *
from config import *


if __name__ == '__main__':
    match mode:
        case 0:
            help(cryptograph)
            cryptograph(file_to_encrypt, to_lower, rm_punctuation,
                        shift, encrypted_new_line_length)
            print(
                f'Do not forget to save your brand new `decryptor-for-{file_to_encrypt}` in a very secure place!')
        case 1:
            help(decryptograph)
            decryptograph(file_to_decrypt, decryptor)
        case _:
            raise RuntimeError(f'There is no mode {mode}.')
