#!/usr/bin/env python
# Generates all the possible passcodes of an iPhone device
# With a four-digit passcode
def main():
	keys = open("pass.txt", "w")
	for w in range(0, 10):
		for x in range(0, 10):
			for y in range(0, 10):
				for z in range(0, 10):
					keys.write(str(w) + str(x) + str(y) + str(z) + "\n")
	keys.close()

main()
