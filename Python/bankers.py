#!/usr/bin/env python3

def main():
	process = []
	total_resources = int(input("Enter the amount of total resources: "))
	size = int(input("How many processes will you enter? "))
	
	for index in range(0, size):
		process.append([input("Enter maximum allocation for process #{}: ".format(index + 1)), input("Enter current allocation for process #{}: ".format(index + 1))])

	difference = ""
	for index in range(0, len(process)):
		for char in range(0, len(process[index][0])):
			difference += str(abs(int(process[index][0][char]) - int(process[index][1][char])))
		process[index].append(difference)
		difference = ""
		
	total_allocation = get_total_allocation(process=process)

	origin_available_instance = get_available_instance(total_resources=total_resources, total_allocation=total_allocation)
	available_instance = origin_available_instance

	print("-----------------------------------------------------")
	print("Max. Allocation\t\tAllocated Resource\tNeed")
	for index in range(0, len(process)):
		print("{}\t\t\t{}\t\t\t{}".format(process[index][0], process[index][1], process[index][2]))
	print("-----------------------------------------------------")
	
	while (len(process) != 0):
		queue, process = compare_available_instance(process=process, available_instance=available_instance)
		for index in range(0, len(queue)):
			available_instance = (available_instance - int(queue[index][0])) + int(queue[index][1])

	available_instance = available_instance - total_allocation

	print("Safe state" if (available_instance == origin_available_instance) else "Not-safe state")

def compare_available_instance(process=[], available_instance=0):
	queue = []; forRemoval = []
	for index in range(0, len(process)):
		if (int(process[index][2]) < available_instance):
			queue.append([process[index][2], process[index][0]])
			forRemoval.append(process[index])
	queue.sort()
	for index in range(0, len(forRemoval)):
		process.remove(forRemoval[index])
	return queue, process

def get_available_instance(total_resources=0, total_allocation=0):
	return total_resources - total_allocation

def get_total_allocation(process=[]):
	total_allocation = 0
	for index in range(0, len(process)):
		total_allocation += int(process[index][1])
	return total_allocation

main()