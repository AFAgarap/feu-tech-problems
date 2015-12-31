# FEU Tech -- Cigarette problem
testCase = input('Enter number of test cases:')

for x in xrange(0,testCase):
	number = input('Enter number of cigarettes:')
	butts = input('Enter number of butts:')
	count = number
	while number >= butts:
		count += number / butts
		number /= butts
	print count