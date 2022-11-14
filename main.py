def decryption(bin_list, cipher_text):
	for i in range(0, len(bin_list), 60):
		print(i, ": ", bin_list[i])

# convert hex to binary
def hex_to_bin(cipher_text):
	pairs = []
	binary = []

	for line in cipher_text:
		for i in range(0, len(line), 2):
			pairs.append(line[i:i+2])	# get every 2 chars from list
	for i in pairs:
		convert_bin = bin(int(i, 16))	# convert hex to binary
		prefix_bin = convert_bin[2:]	# remove prefix 0b from binary
		long_bin = prefix_bin.zfill(8)	# ensure all binaries are length 8
		binary.append(long_bin)			# add binaries to list

	return binary


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

	bin_list = hex_to_bin(cipher_text)

	decryption(bin_list, cipher_text)

	print("\nProgram ended\n\n")

# execute program
if __name__ == "__main__":
	main()
