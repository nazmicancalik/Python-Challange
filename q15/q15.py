#!/usr/bin/python

import datetime
day = 26
year = 0
month = 1

for i in range(90,99):
	year = '1' + str(i) + '6'
	if(datetime.date(int(year),month,day).weekday() == 0):
		print (year)
