import sys
from random import randint
import copy



def find_rand_node(input_array):
	first_node = input_array.keys()[randint(0, len(input_array) - 1)]
	second_node = input_array[first_node][randint(0, len(input_array[first_node]) - 1)]

	return first_node, second_node

def karger_min_cut(input_array):
	input_copy = copy.deepcopy(input_array)
	while len(input_copy) > 2: #base case
		first_node, second_node = find_rand_node(input_copy)
		input_copy[first_node] += input_copy[second_node]
		for i in input_copy[second_node]:
			check = input_copy[i]
			for j in range(0, len(check)):
				if check[j] == second_node:
						check[j] = first_node

		while first_node in input_copy[first_node]:
				input_copy[first_node].remove(first_node)

		del input_copy[second_node]

	return len(input_copy[input_copy.keys()[0]])

def main():

	import_file = {}
	f = open('kargerAdj.txt')
	while True:
		line = f.readline()
		if line == '':
			break
		else:
			row = line.split()
			import_file[int(row[0])] = [int(x) for x in row[1:]]
	
	min_cut = karger_min_cut(import_file)

	for i in range(0, 1000):
		j = karger_min_cut(import_file)
		if j < min_cut:
			min_cut = j

	print "min cuts: %d" % min_cut

if __name__ == '__main__':
	main()


