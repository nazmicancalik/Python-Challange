#!/usr/bin/python
import urllib.request

data = ['1','11','21','1211']
def process(line):
	last_character = line[0]
	freq = 0
	element = ""
	for character in line[:-1]:
		if last_character == character:
			freq +=1
		else:
			element = element + str(freq) + last_character
			freq = 1
		last_character = character
	if(line[-1] == line[-2]):
		freq +=1
	element = element + str(freq) + last_character
	if(line[-1] != line[-2]):
		element = element + '1' + line[-1]
	data.append(element)

while len(data) < 31:
	process(data[-1])

#print (data[-1])
#print (data)
print ('The answer is : ' + str(len(data[30])))
