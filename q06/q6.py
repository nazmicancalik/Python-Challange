#!/usr/bin/python

import zipfile,re

findnothing =  re.compile(r"Next nothing is (\d+)").match
zf = zipfile.ZipFile('channel.zip','r')
comments = []
seed = "90052"
while True:
	fname = seed + ".txt"
	comments.append(zf.getinfo(fname).comment)
	guts = zf.read(fname)
	m = findnothing(guts)
	if m:
		seed = m.group(1)
	else:
		break

message = ''.join(comments)
print (message)


