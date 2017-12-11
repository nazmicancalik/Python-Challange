#!/usr/bin/python
import sys
import re

def main(argv):
	counter = 90052
	file = sys.argv[1] + '.txt'
	f_2 = open('result.txt','w')
	while True:
		index = extract_info(file)
		file = index + '.txt'
		counter = counter + int(index)
		f_2.write(str(counter) + '\n')
def extract_info(fileName):
	f = open(fileName,'r')
	line = f.readline()
	print (line)
	m = re.search(r'(\d+)$', line)
	return m.group()

if __name__ == '__main__':
	main(sys.argv)
