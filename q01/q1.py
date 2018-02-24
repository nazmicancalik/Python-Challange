#!/usr/bin/python

# We need to convert the given text to a meaningful text.
# We should do that by incrementing the letters by two.
# As can be seen from the image K becomes M
# Like ceasar cipher.


encyripted_text = 'g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr\'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'
alphabet = 'abcdefghijklmnopqrstuvwxyz'
ALPHABET_SIZE = 26

url = 'http://www.pythonchallenge.com/pc/def/map.html'
# Jvon files is a misleading tip. We have to take only ocr and go to ocr.html
second_encriptioned_text = 'Have you ever heard of jvon files !?'

def shift_text(str,shift):
	data = []
	for i in str:
		if i.strip() and i in alphabet:
			data.append(alphabet[(alphabet.index(i) + shift) % ALPHABET_SIZE])
		else:
			data.append(i)
	output = ''.join(data)
	return output

output = shift_text(encyripted_text,2)
print (output)

#Apply on the url.
print (url[:-8] + shift_text('map',2) + '.html' )
