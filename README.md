# :game_die::closed_lock_with_key:Encryption by Random

The presented open source software is used to encrypt and decrypt text files using the special method.

The encryption method is based on the Caesar Cipher.  
The program code reads the words from the file and represents each letter of the word in the following format:

`{special letter combination}{randomly changed ASCII-number of the letter}`

**Make sure you have Python 3.10 or higher installed, and then you can watch this guide.**

[<img src=".\assets\thumbnail.jpg" title="Guide on YouTube" width="250"/>](https://www.youtube.com/watch?v=gHZ-ZxnX0ZM)

## Usage

A user is supposed to interact with two files:

* `config.py`
* `main.py`

In `config.py` you can configure all the parameters of the program.

Most of the parameters are set by default, you need to configure the following ones:

* `mode` - `0` is `Encryption mode`, `1` is `Decryption mode`.
* `file_to_encrypt` - name of (path to) the file you are going to encrypt.
* `file_to_decrypt` - name of (path to) the file you are going to decrypt.
* `decryptor` - name of (path to) the file that is decryptor to the file you are going to decrypt.

You can configure other parameters if you want, but it is unnecessary.

**Keep in mind that it is easier if all the files are located in the same directory with `config.py` and `main.py`.**

Steps:

1. Adjust these parameters in `config.py` as you need or leave them undefined if there is not, for example, a file to decrypt.
2. Head to `main.py` and run it.
3. Check received files and save them in an incredibly safe place!

***
All details for further maintenance and modernization of the code,  
as far as possible, are provided in the `__doc__` of functions and modules.
***
If you have any proposals or questions, be sure to ping [me](https://github.com/maestroviktorin).

[<img height="35" src=".\assets\telegram.png" title="Telegram" width="35"/>](https://maestroviktorin.t.me)
[<img height="35" src=".\assets\discord.png" title="Discord" width="35"/>](https://discordapp.com/users/531105058864103435/)
