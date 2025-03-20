"""
1) Megan Kim
2) 251431752
3) mkim945
4) 2025-03-20
5) This file contains functions to encrypt and decrypt text files using the Caesar and Vigenère ciphers.
"""

import os

def encrypt_caesar(input_file, output_file, key):
    """Encrypts a file using the Caesar cipher."""
    if not isinstance(key, int):
        raise TypeError("The given key value is the wrong type!")
    
    if not os.path.isfile(input_file):
        raise FileNotFoundError(f"The input file {input_file} does not exist.")
    
    if os.path.isfile(output_file):
        raise FileExistsError(f"The output file {output_file} already exists.")

    with open(input_file, "r", encoding="utf-8") as f_in, open(output_file, "w", encoding="utf-8") as f_out:
        text = f_in.read()
        encrypted_text = []
        char_count = 0

        for char in text:
            if char.isalpha():
                shift = (ord(char.upper()) - ord('A') + key) % 26
                encrypted_text.append(chr(ord('A') + shift))
            else:
                encrypted_text.append(char)
            char_count += 1

        f_out.write("".join(encrypted_text))
    
    return char_count


def decrypt_caesar(input_file, output_file, key):
    """Decrypts a file using the Caesar cipher."""
    return encrypt_caesar(input_file, output_file, -key)


def encrypt_vigenere(input_file, output_file, key):
    """Encrypts a file using the Vigenère cipher."""
    if not isinstance(key, str):
        raise TypeError("The given key value is the wrong type!")
    
    if not os.path.isfile(input_file):
        raise FileNotFoundError(f"The input file {input_file} does not exist.")
    
    if os.path.isfile(output_file):
        raise FileExistsError(f"The output file {output_file} already exists.")
    
    key = key.upper()
    with open(input_file, "r", encoding="utf-8") as f_in, open(output_file, "w", encoding="utf-8") as f_out:
        text = f_in.read()
        encrypted_text = []
        key_index = 0
        char_count = 0

        for char in text:
            if char.isalpha():
                shift = ord(key[key_index % len(key)]) - ord('A')
                new_char = chr(((ord(char.upper()) - ord('A') + shift) % 26) + ord('A'))
                encrypted_text.append(new_char)
                key_index += 1
            else:
                encrypted_text.append(char)
            char_count += 1

        f_out.write("".join(encrypted_text))
    
    return char_count


def decrypt_vigenere(input_file, output_file, key):
    """Decrypts a file using the Vigenère cipher."""
    if not isinstance(key, str):
        raise TypeError("The given key value is the wrong type!")
    
    if not os.path.isfile(input_file):
        raise FileNotFoundError(f"The input file {input_file} does not exist.")
    
    if os.path.isfile(output_file):
        raise FileExistsError(f"The output file {output_file} already exists.")

    key = key.upper()
    with open(input_file, "r", encoding="utf-8") as f_in, open(output_file, "w", encoding="utf-8") as f_out:
        text = f_in.read()
        decrypted_text = []
        key_index = 0
        char_count = 0

        for char in text:
            if char.isalpha():
                shift = ord(key[key_index % len(key)]) - ord('A')
                new_char = chr(((ord(char.upper()) - ord('A') - shift) % 26) + ord('A'))
                decrypted_text.append(new_char)
                key_index += 1
            else:
                decrypted_text.append(char)
            char_count += 1

        f_out.write("".join(decrypted_text))
    
    return char_count
