def main():
	print("\t\t\t10th degree of Maclaurin series, sin(x)")
	x = float(input("Enter value of x: "))
	answer = x; i = 1; j = 1
	while(i <= 10):
		if(i == 1):
			answer -= (x ** (j + 2)) / factorial(j + 2)
		elif(i % 2 == 0):
			answer += (x ** (j + 2)) / factorial(j + 2)
		elif(i % 2 != 0):
			answer -= (x ** (j + 2)) / factorial(j + 2)
		i += 1; j += 2
	print(answer)

def factorial(number):
	return 1 if (number == 0) else number * factorial(number - 1)

main()
