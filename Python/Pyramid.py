for x in range(1, 11):
	for y in range(10, -1, -1):
		print(" " if (y + x <= 10) else "", end="")
	for z in range(1, x):
		print(z," ", end="")

	print("\n")
