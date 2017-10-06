#!/usr/bin/env python3
# caesar cipher program

from string import ascii_uppercase


# This is a list of all alphabet letters in uppercase
letter_set = list(ascii_uppercase)

# variable for storage of cipher text
cipher_text = ""

# get user input for text to be encrypted
# then convert it to uppercase (cryptology convention)
plain_text = input("Enter plain text: ").upper()

# get user input for caesar cipher key
key = int(input("Enter key: "))

# loop through the plain_text string
for index in range(len(plain_text)):
	# loop through the list of alphabet letters
	for letter_index in range(len(letter_set)):
		# checks if letter in plain_text
		# matches the letter in the alphabet list
		if plain_text[index] == letter_set[letter_index]:
			# implement the key for encryption
			cipher_text += letter_set[(letter_index + key) % len(letter_set)]

# print the cipher text
print(cipher_text)
