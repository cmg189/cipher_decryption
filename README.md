# Single Key Exploit

This program demonstrates the single key exploit by way of ciphertext decryption. The single key exploit has also been know to go by other names including one-time pad and many-time pad.

## Table of Contents

1. [Description](#description)
2. [Program Output](#output)
3. [Execution](#exe)
4. [Function Headers](#function)
5. [Resources](#resources)

## Description <a name="description"></a>

Single Key Exploit is a python program that decrypts ciphertext. This ciphertext has been encrypted using a single key for each message, leading to the single key exploit.
Upon execution, the program will display the plaintext message that will be encrypted. Then it will try to decrypt as much of the encrypted text as possible. The resulting decrypted text will be output to the user.


## Program Output <a name="output"></a>

<img src="output.PNG" width="450" height="400">


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
make_cipher(text, key)
```

- Description:

	Creates a list of strings representing ciphertext

- Parameters:

	`text` List representing plaintext

	`key` List of bytes representing the encryption key

- Return:

	`cipher` List containing ciphertext

---

``` python
encrypt(msg, key)
```

- Description:

	Encrypts plain text using an encryption key

- Parameters:

	`mag` String to be encrypted

	`key` List representing encryption key

- Return:

	`bytes` String representing encrypted text in hexadecimal

---

``` python
preprocess(text)
```

- Description:

	Turns encrypted text into hexadecimal and initializes a list of dashes acting as placeholders

- Parameters:

	`text` List containing ciphertext

- Return:

	`hex` List representing hexadecimal representation of encrypted text

	`place_holders` List containing dashes -

---

``` python
break_encryption(encrypted_text, decrypted_text)
```

- Description:

	Attempts to break encryption by utilizing XOR operations

- Parameters:

	`encrypted_text` List containing the ciphertext

	`decrypted_text` List of placeholders to store decrypted text

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
output_text(text)
```

- Description:

	Outputs the decrypted text

- Parameters:

	`text` List containing decrypted text

- Return:

	None


## Resources <a name="resources"></a>

To learn more about this encryption vulnerability refer to this article: [One-time Pad](https://www.ciphermachinesandcryptology.com/en/onetimepad.htm)
