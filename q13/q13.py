#!/usr/bin/python

import xmlrpclib

proxy = xmlrpclib.ServerProxy('http://www.pythonchallenge.com/pc/phonebook.php')

methods = proxy.system.listMethods()
print ('Methods: ' + str(methods))

phone = proxy.system.methodSignature('phone')
print ('Phone method signature: ' + str(phone))

'''
#After looking at the methods we understand we have a phone method. 'Phone that evil'
call = proxy.phone('Evil')
print ('Call result: ' + str(call))
'''

#After looking at the methods we understand we have a phone method. 'Phone that evil'
call = proxy.phone('Bert')
print ('Call result: ' + str(call))

#See the result for yourself , italy