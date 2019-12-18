n = "0"

for i in range(1, 11):
    print("{} * 9 + {} = {}".format(int(n), i, (int(n) * 9 + i)))
    n += str(i)
