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


	print("\nProgram ended\n\n")

# execute program
if __name__ == "__main__":
	main()
