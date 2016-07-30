#!/usr/bin/env python
# If n is odd or if n is even and in between 6 and 20 (inclusive), print "Weird"
# If n is even and in between 2 and 5 (inclusive) or if n is even and > 20, print "Not Weird"
number = input('Enter a number:')
print "Weird" if (number % 2 != 0 or number >= 5 and number <= 20) else "Not Weird"
