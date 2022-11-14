#!/usr/bin/env python3
import binascii		# for binascii.unhexlify()
SPACE = 32
LINE_LENGTH = 60

# main exeuction
def main():
	file_name = "a.txt"
	#file_name = input("Enter the name of the ciphertext file: ")
	encrypted_text = get_cipher(file_name)
	print(encrypted_text)

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



# execute program
if __name__ == "__main__":
	main()
