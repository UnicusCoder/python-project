
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

		if operation == '1':
			print(number_1, "+", number_2, "=", add(number_1, number_2))
		elif operation == '2':
			print(number_1, "-", number_2, "=", substract(number_1, number_2))
		elif operation == '3':
			print(number_1, "*", number_2, "=", multiply(number_1, number_2))
		elif operation == '4':
			print(number_1, "/", number_2, "=", divide(number_1, number_2))

		next_calculation = input("Continue calculation? (Y/N): ")
		if next_calculation == "N":
			break
		else:
			print("Invalid input! Please enter a valid operation (1-4).")



			