# from file, read 2 characters at a time into a list
def cipher(file_name):
	file_obj = open(file_name, "r")

	file_chars = [] # list to hold chars from file
	char_holder = file_obj.read(2) # read 2 chars at a time

	# read entire contents of file
	while len(char_holder) > 0:
		file_chars.append(char_holder)
		char_holder = file_obj.read(2)

	file_obj.close()

	return file_chars

# main exeuction
def main():
	file_name = input("Enter the name of the ciphertext file: ")

	cipher_text = cipher(file_name)

	for i in cipher_text:
		print(i)
	print("\nProgram ended\n\n")

# execute program
if __name__ == "__main__":
	main()
