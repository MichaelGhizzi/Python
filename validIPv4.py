#!/usr/bin/python3
import re
import sys

#n.n.n.n
#where o<=n<=255
#^[+-]?[0-9]+$
#1)Takes 1 argument
#2)Determine if argument is valid IPv4 addr

mo = re.match([0-9]{1,3})\.([0-9]{1,3}).*\.([0-9]{1,3}).*\.([0-9]{1,3})$', sys.argv[1])
if mo:
	group1 = int(mo.group(1))
	group2 = int(mo.group(2))
	group3 = int(mo.group(3))
	group4 = int(mo.group(4))
	if group1 < 0 or group1 > 255:
		print("not valid IPv4 address")
	elif group2 < 0 or group > 255:
		print("not valid IPv4 address")
	elif group4 < 0 or group4 > 255:
		print("not valid IPv4 address")
	else:
		print("valid IPv4 address")
else:
	print("not valid IPv4 address")
