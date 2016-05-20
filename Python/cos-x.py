from factorial import factorial

def main():
	print("\t\t\t10th degree of Maclaurin series, cos(x)")

	x = float(input("Enter value of x (in Radians): "))
	answer = 1; i = 1; j = 2
	while(i < 10 and j <= 10):
		if (i % 2 == 0):
			answer += (x ** j) / factorial(j)
		elif (i % 2 != 0):
			answer -= (x ** j) /factorial(j)
		i += 1; j += 2
	print(answer)

main()
