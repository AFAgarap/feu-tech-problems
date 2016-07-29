#!/usr/bin/env python
# Maclaurin series for e^x
from factorial import factorial

def main():
	print("\t\t\t10th degree of Maclaurin Series, e^x")

	x = float(input("Enter value of x: "))
	answer = 1; i = 1
	while(i <= 10):
		answer += (x ** i) / factorial(i)
		i += 1
	print(answer)

main()
