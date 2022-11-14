#!/usr/bin/env python3
import binascii		# for binascii.unhexlify()
SPACE = 32
LINE_LENGTH = 60

# main exeuction
def main():
	file_name = "a.txt"#file_name = input("Enter the name of the ciphertext file: ")

	encrypted_text = get_cipher(file_name)	# get text from file and convert to hex

	decrypted_text = init_text(encrypted_text)	# initalized to all -


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

def init_text(encrypted_text):
	place_holders = []
	for line in encrypted_text:
		# bytearray because array must be mutable
		temp = bytearray('-' * LINE_LENGTH, 'ascii')	# all - because we have not solved any text yet
		place_holders.append(temp)

	return place_holders

# execute program
if __name__ == "__main__":
	main()
