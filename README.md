# :game_die::closed_lock_with_key:Encryption by Random
`Developed at ViktorInTech`
## Whitepaper
***
### Cryptograph
The presented open source software is used to encrypt text files by the special method

The encryption method is based on the Caesar Cipher  
The program code reads the words from the file, rid them from punctuation characters at the edges and then
represents each letter of the word in the following format:

`{special word}{randomly changed ASCII-number of the letter}`

In the resulting encrypted file, each word is written in one line

***The program also creates a special decryption key, applicable *ONLY* to the received file***  
***You should save it for the possibility to decrypt the received file in the future***

> Don't forget to change this part of the code:
> 
> ```python
> ...
> if __name__ == '__main__':
>    help(cryptograph)
>    cryptograph('[YOUR FILE TO BE ENCRYPTED]')
> ...
> ```
> **It is best if *[YOUR FILE TO BE ENCRYPTED]* is located in the same directory with `cryptograph.py`**
***
### Decryptograph
It is software to decrypt file encrypted using the utility shown above

The program takes in the encrypted file and decryptor file to it

In the resulting decrypted file all words are translated to lowercase and written in one line

> Don't forget to change this part of the code:
> 
> ```python
> ...
> if __name__ == '__main__':
>    help(decryptograph)
>    decryptograph('[YOUR FILE TO BE DECRYPTED], [DECRYPTOR FOR YOUR FILE]')
> ...
> ```
> **It is best if *[YOUR FILE TO BE DECRYPTED]* and *[DECRYPTOR FOR YOUR FILE]* are located in the same directory with `decryptograph.py`**
***
### Actions
**This file is NECESSARY for the execution of the two programs presented above**

It contains default special words used in the en/decryption algorithm  
You can reconfigure this at your discretion

**Bear in mind:**
* The encryption algorithm will not work without a file with special words
* If you changed the configuration of special words for encryption, then the decryption algorithm of the received file
will work correctly only with this configuration
***
*If you have ideas for improving the code (and someone will definitely have them),*  
*be sure to write them in the `Issues` section on the **[project's GitHub](https://github.com/ViktorInTech/encrypting_by_random)***
