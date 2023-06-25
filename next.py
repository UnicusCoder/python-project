'''

import random

def generate_code(length):
	code = ""
	for i in range(length):
		code += random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
	return code


def main():
	length = int(input("Enter a length of code: "))
	code = generate_code(length)
	print("The generate code is :", code)

if __name__ == "__main__":
	main()



def add(a, b):
	return a + b

def substract(a, b):
	return a - b

def multiply(a, b):
	return a * b

def divide(a, b):
	return a / b


print("Select operation.")
print("1. Add")
print("2. Substract")
print("3. Multiply")
print("4. Divide")

while True:
	operation = input("Select operation(1-4): ")

	if operation in ('1', '2', '3', '4'):
		
		number_1 = float(input("Enter first number: "))
		number_2 = float(input("Enter second number: "))

		if operation == "1":
			print(number_1, "+", number_2, "=", add(number_1, number_2) )
		elif operation == "2":
			print("number_1", "-", number_2, "=", substract(number_1, number_2))
		elif operation == "3":
			print("number_1", "*", number_2, "=", multiply(number_1, number_2))
		elif operation == "4":
			print("number_1", "/", number_2, "=", divide(number_1, number_2))
	
		next_calculation = input("Continue calculation?(Y/N): ")
		if next_calculation == "N":
			break

		else:
			print("Invalid input! Please choose (1-4). ")
			


# mad lib story

adjective = input("Enter an adjective: ")
noun = input("Enter a noun: ")
verb = input("Enter a verb(past tense): ")
adverb = input("Enter an adverb: ")

story = f"Once upon a time, there was a {adjective} {noun}, who {verb} {adverb}"

print("\nMad Lib Story")
print(story)

'''


celsius = input('Enter temperature in celsius: ')
fahrenheit = (1.8 * celsius)

print("Temperature in Fahrenheit: ", celsius)

