def main():
	answer = 0; n = input("Enter n: "); m = input("Enter m: ")
	for x in xrange(0, m):
		answer += (((input("Enter b: ") - input("Enter a: ")) + 1) * input("Enter k: "))
	print (answer / n)

main()