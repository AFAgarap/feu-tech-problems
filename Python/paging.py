#!/usr/bin/env python3

def main():
	page_mapping = []
	physical_frame_table = []
	virtual_page_table = []

	size = int(input("How many words will you enter? "))
	word_size = int(input("Enter word size: "))
	
	virtual_page_table = set_virtual_page_table(virtual_page_table=virtual_page_table, size=size, word_size=word_size)
	page_mapping = set_page_mapping(page_mapping=page_mapping, size=size)

	sorted_mapping = list(page_mapping)
	sorted_mapping.sort()

	physical_frame_table = get_physical_frame_table(page_mapping, physical_frame_table, virtual_page_table, sorted_mapping[-1], word_size)
	
	print("Virtual Page Table[] : {}".format(virtual_page_table))
	print("Page Mapping[] : {}".format(page_mapping))
	print("Physical Frame Table[] : {}".format(physical_frame_table))

def set_virtual_page_table(virtual_page_table=[], size=0, word_size=0):
	temp = []
	for offset in range(0, size):
		for elem in range(0, word_size):
			temp.append(input("Enter value for offset #{}[{}]: ".format(offset, elem)))
		virtual_page_table.append(temp)
		temp = []
	return virtual_page_table

def set_page_mapping(page_mapping=[], size=0):
	for offset in range(0, size):
		page_mapping.append(int(input("Enter page number for offset #{}: ".format(offset))))
	return page_mapping

def get_physical_frame_table(page_mapping=[], physical_frame_table=[], virtual_page_table=[], upperbound=0, word_size=0):
	for frame_number in range(0, upperbound + 1):
		physical_frame_table.append([
			frame_number * word_size,
			virtual_page_table[page_mapping.index(frame_number)] if frame_number in page_mapping else None
		])
	return physical_frame_table

if __name__ == '__main__':
	import os; os.system('clear')
	main()