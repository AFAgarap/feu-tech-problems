x = input("Enter number of seconds: ")
total = 0
i = 1
j = 0

while j < x:
    if j % 2 != 0:
        i += 1
    total += i
    j += 1

print total
