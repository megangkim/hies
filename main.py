"""
1) Megan Kim
2) 251431752
3) mkim945
4) 2025-03-20
5) This file provides a command-line interface for encrypting, decrypting, and analyzing text files using the Caesar and Vigenère ciphers.
"""

from cipher import *
import os

def frequency_analysis(ciphertext):
    """Performs frequency analysis on a given text and returns a dictionary with letter counts."""
    freq_dict = {chr(i): 0 for i in range(ord('A'), ord('Z') + 1)}
    total_count = 0

    for char in ciphertext.upper():
        if char.isalpha():
            freq_dict[char] += 1
            total_count += 1

    return {k: v for k, v in freq_dict.items() if v > 0}


def print_frequency_graph(frequency_dict):
    """Prints a frequency analysis graph for letter occurrence."""
    total = sum(frequency_dict.values())
    
    for letter in sorted(frequency_dict.keys()):
        percentage = round((frequency_dict[letter] / total) * 100) if total > 0 else 0
        print(f"{letter}: {'*' * percentage}")


def print_menu():
    """Displays the encryption menu and ensures valid user input."""
    while True:
        print("\nEncryption options:")
        print("1) Caesar Cipher")
        print("2) Vigenere Cipher")
        print("3) Frequency Analysis")
        print("4) Exit")

        choice = input("Input menu option (1 to 4): ").strip()
        
        if choice.isdigit() and 1 <= int(choice) <= 4:
            return int(choice)
        
        print("Invalid input!")


def main():
    """Handles user input and performs encryption, decryption, or frequency analysis."""
    while True:
        choice = print_menu()

        if choice == 1:  # Caesar Cipher
            action = input("Are you encrypting or decrypting (e/d)? ").strip().lower()
            input_file = input("Enter the input file name: ").strip()
            output_file = input("Enter the output file name: ").strip()
            key = int(input("Enter the key (integer): ").strip())

            try:
                if action == "e":
                    count = encrypt_caesar(input_file, output_file, key)
                elif action == "d":
                    count = decrypt_caesar(input_file, output_file, key)
                else:
                    print("Invalid action!")
                    continue
                
                print(f"Number of characters processed: {count}")

            except Exception as e:
                print(f"Error: {e}")

        elif choice == 2:  # Vigenere Cipher
            action = input("Are you encrypting or decrypting (e/d)? ").strip().lower()
            input_file = input("Enter the input file name: ").strip()
            output_file = input("Enter the output file name: ").strip()
            key = input("Enter the key (a string): ").strip()

            try:
                if action == "e":
                    count = encrypt_vigenere(input_file, output_file, key)
                elif action == "d":
                    count = decrypt_vigenere(input_file, output_file, key)
                else:
                    print("Invalid action!")
                    continue
                
                print(f"Number of characters processed: {count}")

            except Exception as e:
                print(f"Error: {e}")

        elif choice == 3:  # Frequency Analysis
            input_file = input("Enter the cipher text file name: ").strip()

            try:
                with open(input_file, "r", encoding="utf-8") as f:
                    text = f.read()

                freq_dict = frequency_analysis(text)
                print_frequency_graph(freq_dict)

            except Exception as e:
                print(f"Error: {e}")

        elif choice == 4:  # Exit
            print("Exiting the program.")
            break


if __name__ == "__main__":
    main()
