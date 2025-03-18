# Caesar Cipher Project


# Date
August 6, 2022

# Description
This program implements a simple encoder-decoder using the Caesar cipher technique. It allows users to encrypt and decrypt messages using a shift-based substitution cipher. The program reads input from files, processes the text, and writes the output back to a file.

# Features
- Encrypts text using a Caesar cipher with a default shift of 3.

- Decrypts text using a shift of -3.

- Reads input from a file and writes the output to another file.

- Handles uppercase letters while preserving non-alphabetic characters.
 
- Provides a simple user interface for selecting encoding or decoding.

# Usage

1. Run the program and follow the prompts:
2. Choose to encode (E), decode (D), or quit (Q).
3. Enter the input file name.
4. Enter the output file name.
5. The encrypted or decrypted message will be written to the specified output file.

# Functions

readfile(): Reads and returns the contents of a specified file.

writefile(message): Writes a given message to a specified file.

encode(plaintext, shift=3): Encrypts the text using a Caesar cipher.

decode(cipherText, shift=-3): Decrypts the text using a Caesar cipher.

to_string(text): Converts a list of characters to a string.

to_list(string): Converts a string into a list of characters.


