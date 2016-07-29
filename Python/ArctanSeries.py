#!/usr/bin/env python
# Maclaurin Series for Arctan
# arctan(x) = x - x ** 3 / 3 + x ** 5 / 5 ...
def main():
	x = input("Enter x: ")
	k = input("Enter k: ")
	answer = x; i = 1; j = 1
	while(i < k):
		if (i == 1):
			answer -= (x ** (j + 2)) / (j + 2)
		elif (i % 2 == 0):
			answer += (x ** (j + 2)) / (j + 2)
		elif (i % 2 != 0):
			answer -= (x ** (j + 2)) / (j + 2)
		i += 1; j += 2
	print "Answer:", answer
main()
