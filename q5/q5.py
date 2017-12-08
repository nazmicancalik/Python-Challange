#!/usr/bin/python

import sys

def main(argv):
	file = sys.argv[1]
	data = []
	with open(file) as fileobj:
		for line in fileobj:
			data.append(line.strip())
	print (''.join(data))

if __name__ == '__main__':
	main(sys.argv)