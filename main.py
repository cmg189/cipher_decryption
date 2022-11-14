#!/usr/bin/env python3
import binascii		# for binascii.unhexlify()
SPACE = 32
LINE_LENGTH = 60

# main exeuction
def main():
	file_name = "a.txt"#file_name = input("Enter the name of the ciphertext file: ")

	encrypted_text = get_cipher(file_name)	# get text from file and convert to hex

	decrypted_text = init_text(encrypted_text)	# initalized to all -

	#break_encryption(encrypted_text, decrypted_text)	# attempts to decrypt cipher

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
			if is_ascii_space(not_cracked, cipher[columns], columns):
				break

def is_ascii_space(not_cracked, current_char, columns):
	# itterate through the current columns
	for row in not_cracked:
		xor_result = row[columns] ^ current_char	# XOR together
		# we know any char XORed with a space will be >= 65
		# or if space is XORed with another space it will be 0
		if (chr(xor_result) >= 65 or xor_result == 0):
			return True
	return False

# execute program
if __name__ == "__main__":
	main()
