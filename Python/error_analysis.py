# Homework for Numerical Analysis course
# Summer Semester, AY 2015-2016 Adamson University
# Author: A.F. Agarap

# re is the Python package for Regular Expressions
# os is the Python package for OS commands
import re
import os

def get_input():
	'''
	Returns the values of x and y, and operation
	x = get_input[0], y = get_input[1], operation = get_input[2]
	'''
	try:
		x = eval(input("Enter value for x: "))
		y = eval(input("Enter value for y: "))
		operation = int(input("Which arithmetic operation to do:\n[1] Addition (+)\n[2] Subtraction (-)\n[3] Multiplication (*)\n[4] Division (/)\nEnter choice >> "))
	except:
		print("An unexpected error had occurred.")
	return x, y, operation

def get_value(x, y, opt):
	'''
	Solves for the result of x and y
	based on the chosen arithmetic operation
	'''
	if (opt == 1):
		return x + y
	elif (opt == 2):
		return x - y
	elif (opt == 3):
		return x * y
	elif (opt == 4):
		return -1

def get_approximate_value(x, y, opt):
	'''
	Solves for the result of x and y
	if they are restricted to four
	floating point digits only
	'''
	regular_expression = r'[\d]+[.][\d][\d][\d][\d]'
	x = re.findall(regular_expression, str(x))
	y = re.findall(regular_expression, str(y))
	approximate_value = get_value(float(x[0]), float(y[0]), opt)
	return approximate_value

def get_error(true_value, approximate_value):
	'''
	Gets the error value
	'''
	error = abs(true_value - approximate_value)
	return error

def get_relative_error(true_value, approximate_value):
	'''
	Gets the relative error
	'''
	relative_error = (abs(true_value - approximate_value) / abs(true_value))
	return relative_error

def main():
	expression = get_input()
	x = expression[0]; y = expression[1]; opt = expression[2]

	# for chop() value
	approximate_value = get_approximate_value(x, y, opt)
	
	# for true value
	true_value = get_value(x, y, opt)
	
	# for round() value
	round_approximate_value = get_approximate_value(round(x, 4), round(y, 4), opt)

	# for chop() and true value
	error = get_error(true_value, approximate_value)
	relative_error = get_relative_error(true_value, approximate_value)

	# for round() and true value
	round_error = get_error(true_value, round_approximate_value)
	round_relative_error = get_relative_error(true_value, round_approximate_value)

	print("Error for chop():\n\tError: ",error,"\tRelative Error:",relative_error)
	print("Error for round():\n\tError: ",round_error,"\tRelative Error",round_relative_error)
	os.system('pause')

main()	# Call the main method
