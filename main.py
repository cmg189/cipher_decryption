# from file, read each line into list
def cipher(file_name):
	file_obj = open(file_name, "r")

	lines = file_obj.readlines()

	file_obj.close()

	return lines

# main exeuction
def main():
	file_name = input("Enter the name of the ciphertext file: ")

	cipher_text = cipher(file_name)
	
	print("\nProgram ended\n\n")

# execute program
if __name__ == "__main__":
	main()
