# Single Key Exploit

This program demonstrates the single key exploit by way of ciphertext decryption

## Table of Contents

1. [Description](#description)
2. [Program Output](#output)
3. [Execution](#exe)
4. [Function Headers](#function)
5. [Resources](#resources)

## Description <a name="description"></a>

Single Key Exploit is a python script that decrypts ciphertext. This ciphertext has been encrypted using a single key for each message, leading to the single key exploit.


## Program Output <a name="output"></a>


## Execution <a name="exe"></a>

To execute run the command `python3 main.py`


## Function Headers <a name="function"></a>

``` python
display_info()
```

- Description:

	Outputs plain text to be encrypted

- Parameters:

	None

- Return:

	`msgs` List containing strings to be encrypted

	`key` List of bytes representing the encryption key

---

``` python
get_cipher(file_name)
```

- Description:

	Reads ciphertext from file

- Parameters:

	`file_name` String representing name of file to read from

- Return:

	`hex` List containing ciphertext from file

---

``` python
init_text(encrypted_text)
```

- Description:

	Initializes a list of dashes acting as placeholders

- Parameters:

	`encryped_text` List containing ciphertext

- Return:

	`place_holders` List containing dashes -

---

``` python
break_encryption(encrypted_text, decrypted_text)
```

- Description:

	Attempts to break encryption by utilizing XOR operations

- Parameters:

	`encrypted_text` List containing the ciphertext

	`decrypted_text` List of placeholders

- Return:

	`cracked_cipher` List of decrypted text

---

``` python
ascii_space(not_cracked, current_char, columns)
```

- Description:

	Checks a character to determine if it is a space

- Parameters:

	`not_cracked` List containing text that has not been decrypted

	`current_char` Char representing the current character that is being test to determine if it is a space

	`columns` Int representing the index of the current character we are testing

- Return:

	`Bool` True if a space is found, False otherwise

---

``` python
output_text(solved)
```

- Description:

	Outputs the decrypted text

- Parameters:

	`solved` List containing decrypted text

- Return:

	None


## Resources <a name="resources"></a>
