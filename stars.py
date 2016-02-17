#!/usr/bin/python3
#-------------------------
# Name: Michael Ghizzi
# Lab Project #5
# CPSC 254 8:00pm T/Th 
# stars.py
# This programs prints a right-alrighed triangle based upon the integer which is imported from the argument.
#-------------------------
import sys
import re

def stars(count):
  stars = count
  starChar = '*' 
  starCount = 1
  spaceChar = ' '
  for spaces in range(count - 1, -1, -1): #Counts Down from the number 
					  #entered from the user.
					  #This is so we can have
					  #one less star for each line
					  #from the bottom up
    print( spaceChar * spaces, end='') #print spaces for right aligning
    print( starChar * starCount) 
    starCount += 1	#increments max stars to print

def main():
  if len(sys.argv) != 2: #Checks if there more than one argument
			 #if there is, it prints out an error message
    print("ERROR: Must contain one argument. Usage: ./stars.py 'INTEGER'")
  else:
# We need to use a regular expression to make sure the argument is [0-#]
# We use '^d$' to see what we want to match.
# Next we use ^ which is the start of the line
# \d is a digit, for the [0-9]
# + more than one digit
# $ end of line
    m = re.search(r'^\d+$', sys.argv[1])
# We use sys.argv[1] to implement the regular expression
    if m: #Prevents negative/floating point #s
      starCount = int(m.group(0))
      stars(starCount)
    else:
	#prints an error if there are negative/floating point #s
      print("ERROR: Invalid argument. Usage: ./stars.py 'INTEGER'")

#Pythonese needed to run the program by itself, gives the
#program permission to use anything inside the program itself.
#If we take this out, the program will not run properly.
#Lets the program be called from outside
if __name__ == "__main__":
  main()
