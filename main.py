#!/usr/bin/env python3
import binascii		# for binascii.unhexlify()
SPACE = 32
LINE_LENGTH = 60

# main exeuction
def main():
	file_name = "a.txt"#file_name = input("Enter the name of the ciphertext file: ")

	encrypted_text = get_cipher(file_name)	# get text from file and convert to hex

	decrypted_text = init_text(encrypted_text)	# initalized to all -

	solved = break_encryption(encrypted_text, decrypted_text)	# attempts to decrypt cipher

	for line in solved:
		print(line)

	print("\nProgram ended\n\n")



# from file, read each line into list and remove any "\n"
def get_cipher(file_name):
	hex = []

	# read all lines from file
	file_obj = open(file_name, "r")
	for line in file_obj:
		temp = binascii.unhexlify(line.strip())	# remove \n and convert to hex
		hex.append(temp)
	file_obj.close()

	return hex

# make list of all -
def init_text(encrypted_text):
	place_holders = []
	for line in encrypted_text:
		# bytearray because array must be mutable
		temp = bytearray('-' * LINE_LENGTH, 'ascii')	# all - because we have not solved any text yet
		place_holders.append(temp)

	return place_holders

# attempts to decrypt cipher
def break_encryption(encrypted_text, decrypted_text):

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


def ascii_space(not_cracked, current_char, columns):
	# itterate through the current columns
	for row in not_cracked:
		xor_result = row[columns] ^ current_char	# XOR together
		# we know any char XORed with a space will be >= 65
		# or if space is XORed with another space it will be 0
		if not (chr(xor_result).isalpha() or xor_result == 0):
			return False
	return True

# execute program
if __name__ == "__main__":
	main()
