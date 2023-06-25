

import random

def generate_code(length):
	'''generate a random code/password for a specified length.'''
	# password = ""
	code = ""
	for i in range(length):
		code += random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
	return code

def main():
	length = int(input("Enter the length of code: "))
	code = generate_code(length)
	print("The generate code is :", code)


if __name__ == "__main__":
	main()
