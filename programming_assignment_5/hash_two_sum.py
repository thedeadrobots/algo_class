import sys

def main():
	inputfile = {}
	f = open('HashInt.txt')
	while True:
		line = f.readline()
		if line == '':
			break
		else:
			inputfile[int(line)] = True

	target_sums = [231552,234756,596873,648219,726312,981237,988331,1277361,1283379]
	result = [0,0,0,0,0,0,0,0,0]

	for k in inputfile.iterkeys():
		for idx, tsum in enumerate(target_sums):
			try:
				if inputfile[tsum - k]:
					result[idx] = 1
				else:
					result[idx] = 0
			except KeyError:
					False
	
	print result


if __name__ == '__main__':
	main()
