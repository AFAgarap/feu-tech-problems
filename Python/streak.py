number = [];

t = int(input())

for index in range(0, t):
	number.append(input())

# print(number)
for i in range(len(number)):
	if (int(number[i]) % 21 == 0 or "21" in number[i]):
		print("The streak is broken!")
	elif (int(number[i]) % 21 != 0):
		print("The streak lives still in our heart!")	
