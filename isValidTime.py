#!/usr/bin/python3
#---------------------
# Name: Michael Ghizzi
# Lab Project #5
# CPSC 254 8:00pm T/TH
# isValidTime.py
# This program has the user enter in a specific time via arguments, and the program defines if the time is valid or not.
#---------------------

import sys
import re

def main(): 
# defines main function
  if len(sys.argv) != 2:  # if there are more than 2 arguments
			  # the time is invalid
    print("ERROR: Invalid time. Usage: ./isValidTime.py '##:## am|AM|pm|PM'") # prints invalid
  else:
# Regular expression used to make sure the time is between 1-12
# followed by a am/pm at the end of the two numbers.
# the result is then assigned the the first argument
    #pattern = re.compile(r"(12|11|10|0?[1-9]):([0-5][0-9]) ?([aApP])[mM]")
    pattern = re.compile(r"(12|11|10|0?[1-9]):([0-5][0-9])(\s)?(AM|am|pm|PM)")
    result = pattern.match(sys.argv[1])
    if result:	# if result is valid, prints is time valid
      print("is valid time")
    else:	# if result is not valid, prints invalid time
      print("invalid time")

# Pythonese needed to run the program by itself, gives the
# program permission to use anything inside the program itself
# If we take this out, the program will not run properly.
# Allows the program to be called from outside
if __name__ == "__main__":
  main()
