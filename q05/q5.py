
#!/usr/bin/python

import sys
import pickle
from urllib.request import urlopen

def main(argv):
	file = open(sys.argv[1],'rb')
	with open(sys.argv[1], 'rb') as pickle_file:
		content = pickle.load(pickle_file)
	for i in content:
		print ("".join([k * v for k, v in i]))
if __name__ == '__main__':
	main(sys.argv)
