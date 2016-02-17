#!/usr/bin/python3
#----------------------------
# Name: Michael Ghizzi
# CPSC 254 8:00pm T/Th
# isValidPhoneNumber.py
# This program identifies if a phone number is valid or not by matching the number with a regular expression, a valid or invalid phone number is then outputted.
# --------------------------
import sys
import re

# Assigns argument to a variable
phoneNumberString=sys.argv[1]
phoneNumberString2=sys.argv[1]

# Checks if there is more than one argument, if there is, an error occurs and the program exits.
if len(sys.argv) < 1:
	print('usage: ./isValidPhoneNumber.py "phone number"')
	exit(1)

# Prints the Phone number string
print(phoneNumberString)

# Regular expression for the phone number pattern
# phonePattern = r'[1|(]?[-]?\d{3}[)|\s]?[-|\s|/]?\d{3}[-|\s]?\d{4}$'

# 2 Regular Expressions testing
phonePattern = r'[1]?[-]?\d{3}[)|\s]?[-|\s|/]?\d{3}[-|\s]?\d{4}$'
phonePattern2 = r'[(]?\d{3}[)|\s]?[-|\s|/]?\d{3}[-|\s]?\d{4}$'

isPhoneNumber = re.match(phonePattern, phoneNumberString)
isPhoneNumber2 = re.match(phonePattern2, phoneNumberString2)

# If the phone number matches the regular expression then valid is printed.
# If the phone number does not match the regular expression then invalid is printed
if isPhoneNumber:
	print('valid phone number.')
elif isPhoneNumber2:
	print('valid phone number.')
else:
	print('invalid phone number.')

