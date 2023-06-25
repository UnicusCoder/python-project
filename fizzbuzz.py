
def fizzbuzz(n):
	if n % 3 == 0 and n % 5 == 0:
		return "FizzBuzz"
	if n % 3 == 0:
		return "Fizz"

	if n % 5 == 0:
		return "Buzz"

	return n 

print(fizzbuzz(15))

n = int(input().strip())

fizzbuzz(n)

