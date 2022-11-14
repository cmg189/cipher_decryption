# convert hex to binary
def hex_to_bin(cipher_text):
	pairs = []
	temp = cipher_text[0]
	for i in range(0, len(temp), 2):
		pairs.append(temp[i:i+2])		# get every 2 chars from list

	binary = []
	for i in pairs:
		short_bin = bin(int(i, 16))		# convert hex to binary
		temp_bin = short_bin[2:]		# remove prefix 0b from binary
		long_bin = temp_bin.zfill(8)	# ensure all binaries are length 8
		binary.append(long_bin)			# add binaries to list

	for i in binary:
		print(i)


# from file, read each line into list and remove any "\n"
def get_cipher(file_name):
	file_obj = open(file_name, "r")
	lines = file_obj.readlines()	# read all lines from file
	file_obj.close()

	clean_lines = []
	for i in lines:
		clean_lines.append(i.strip())	# remove any "\n"

	return clean_lines

# main exeuction
def main():
	file_name = "c.txt"
	#file_name = input("Enter the name of the ciphertext file: ")
	cipher_text = get_cipher(file_name)

	hex_to_bin(cipher_text)

	print("\nProgram ended\n\n")

# execute program
if __name__ == "__main__":
