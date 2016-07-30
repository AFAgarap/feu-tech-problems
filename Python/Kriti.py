#!/usr/bin/env python
# Problem from https://www.hackerearth.com/problem/algorithm/kriti-and-her-birthday-gift/
number_string = int(input())

strings = []

for x in range(0, number_string):
	strings.append(raw_input())

number_query = int(input())

count = []

for x in range(0, number_query):
	lrs = raw_input()
	l, r, s = lrs.split()
	l = int(l); r = int(r)
	
	counter = 0

	for y in range((int(l) - 1), int(r)):
		if (s == str(strings[y])):
			counter += 1
	count.append(counter)

for x in range(len(count)):
	print count[x]
