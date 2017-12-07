#!/usr/bin/python

# I think we need to find the rare alphabetic characters in the text.
# This code extracts the characters that occurs in the mess text to the sunshine.
# WORKS!

import sys

def main(argv):
	file = sys.argv[1]
	result = extract_text(file)
	print (result)

def extract_text(file):
	extracted_text = []
	with open(file) as fileobj:
		for line in fileobj:
			for ch in line:
				if ch.isalnum():
					extracted_text.append(ch)

	return ''.join(extracted_text)

if __name__ == '__main__':
	main(sys.argv)