#!/usr/bin/env python3
import binascii
import os

# main exeuction
def main():

	plain_text, key = display_info()	# output text to be encrypted

	encrypted_text = encrypt(plain_text, key)	# encrypt text

	encrypted_hex, place_holder = preprocess(encrypted_text)	# convert to hex and make place holders

	decrypted_text = break_encryption(encrypted_text, place_holder)	# attempts to decrypt cipher

	output_text(decrypted_text)	# output decrypted text

	print("\nProgram ended\n\n")
	sys.exit()

# inform user of text
def display_info():
	# message to be encrypted and encryption key
	msgs = [ "One time pad is really a completely unbreakable cryptosystem",
	         "Encrypt and decrypt functions are each just an XOR operation",
	         "Key needs to be random bitstring with same length as message",
	         "A many time pad is very insecure and can be broken with ease",
	         "If you can decipher this you can see just how insecure it is" ]
	key = os.urandom(60)

	# output plaintext to user
	print("\n\n\t\tSingle Key Exploit\n\n")
	print("The following messages will be encrypted using the same single encryption key\n")
	print("Messages:\n")
	for line in msgs:
		print(line)

	# return plaintext and encryption key
	return msgs, key

# encrypt plain text with single key
def encrypt(text, key):
	# encrypt every message using the same key
	cipher = []
	for message in text:
		cipher.append(bytes([x ^ ord(y) for (x, y) in zip(key, message)]).hex())
	return cipher

# convert encrypted text into hex and make placeholder
def preprocess(text):
	# convert to hex
	hex = []
	for line in text:
		temp = binascii.unhexlify(line)
		hex.append(temp)

	# make list of - to act as placeholders to store decrypted text
	place_holders = []
	for i in range(len(text)):
		temp = bytearray('-' * LINE_LENGTH, 'ascii')
		place_holders.append(temp)

	return hex, place_holders

# attempts to decrypt cipher
def break_encryption(encrypted_text, decrypted_text):
	SPACE = 32	# ascii
	LINE_LENGTH = 60	# number of chars per line
	key_list = bytearray(LINE_LENGTH)	# list to hold keys, all 00 for now
	key_flags = [False] * LINE_LENGTH	# list of bools acting as flag for when key is found

	# begin itterating through all encrypted text
	for columns in range(LINE_LENGTH):
		# copy of encrypted text
		not_cracked = [line for line in encrypted_text if LINE_LENGTH > columns]
		# itterate through encrypted text
		for cipher in not_cracked:
			# determine if there is a space in the encrypted text
			if ascii_space(not_cracked, cipher[columns], columns):
				key_list[columns] = cipher[columns] ^ SPACE		# if it is a space record the key in that place
				key_flags[columns] = True						# record that we found the key
				# begin itterating through rows
				current_row = 0
				for rows in range(len(decrypted_text)):
					if len(decrypted_text[rows]) != 0 and columns < len(decrypted_text[rows]):
						xor_result = cipher[columns] ^ not_cracked[current_row][columns]	# determine if there is a space
						if xor_result == 0:
							decrypted_text[rows][columns] = SPACE 	# record the decrypted space
						# determine if result if A-Z
						elif chr(xor_result).isupper():
							decrypted_text[rows][columns] = ord(chr(xor_result).lower()) # swap
						# determine if result if a-z
						elif chr(xor_result).islower():
							decrypted_text[rows][columns] = ord(chr(xor_result).upper()) # swap
						current_row = current_row +1 # update itterating value
				break;
	cracked_cipher = []
	for line in decrypted_text:
		temp = line.decode('ascii')
		cracked_cipher.append(temp)
	return cracked_cipher

# detects if there is a space found in text
def ascii_space(not_cracked, current_char, columns):
	# itterate through the current columns
	for row in not_cracked:
		xor_result = row[columns] ^ current_char	# XOR together
		# we know any char XORed with a space will be >= 65
		# or if space is XORed with another space it will be 0
		if not (chr(xor_result).isalpha() or xor_result == 0):
			return False
	return True

# output results
def output_text(text):
	for line in text:
		print(line)
	return

# execute program
if __name__ == "__main__":
	main()
