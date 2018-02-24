#!/usr/bin/python

import urllib.request
import urllib
import re
number = 12345

def get_number(html):
	match_obj = re.search(r'[0-9]+',str(html))
	return str(match_obj.group(0));
for i in range(1,400):
	with urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='+str(number)) as response:
   		html = response.read()
   		print (html)
   		number = get_number(html)

