def main():
	print("\t\t\t10th degree of Maclaurin Series, e^x")

	x = float(input("Enter value of x: "))
	answer = 1; i = 1
	while(i <= 10):
		answer += (x ** i) / factorial(i)
		i += 1
	print(answer)

def factorial(number):
	return 1 if (number == 0) else number * factorial(number - 1)

main()
