#!/usr/bin/env python
# Prints the given letter n times
# Where n is the preceding number to the letter
def main():
	line = raw_input("Enter a string like 1a2b3c: ")
	for x in range(len(line)):
		if (line[x].isdigit()) and (not line[x + 1].isdigit()):
			for y in range(0, int(line[x])):
				print line[x + 1]

main()
