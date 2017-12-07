#!/usr/bin/python

# We need to extract letters that are followed on left and right with 3 capital letters.
# Apply this code to text in source and you get 'linkedlist'

import sys
import re

def main(argv):
	file = sys.argv[1]
	result = extract_groups(file)
	print (result)

def extract_groups(file):
	data = []
	with open(file) as fileobj:
		for line in fileobj:
			data.append(line) 

	str = ''.join(data)
	output = re.findall(r'[a-z][A-Z]{3}([a-z])[A-Z]{3}[a-z]', str)
	return ''.join(output)

if __name__ == main(sys.argv):
	main(sys.argv)
