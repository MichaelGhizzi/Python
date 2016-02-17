#!/usr/bin/python3
#------------------
# Name: Michael Ghizzi
# Lab Project #5
# CPSC 254 8:00pm T/TH
# sortNames.py
# This program reads in one file as an argument and puts them in a seperate files which sorts them.
#------------------

import sys
import re
import os.path

# Checks if there are no arguments 
fileDirectory=str(sys.argv[0])
fileDirectory=fileDirectory[2:]

# Checks if argument takes in file, if not, outputs an error message
if len(sys.argv) < 1:
    print('ERROR: Usage: ./sortNames.py "filename.txt"')
    exit(1)

# Checks if the file exists
# If the file does not exist, then an error message is outputted
# and it exits the program
if os.path.isfile(sys.argv[1]):
    pass
else:
    print('ERROR: File does not exist. Usage: ./sortNames.py "filename.txt"')
    exit(1)

# Saves and lists the names
inputfile  = sys.argv[1]
outputfile = 'sortedNames.txt'
Names=[]

# Regular expression to show the first, middle, and last names
firstMiddleLast = re.compile(r'^(\w+) (\w\.?|\w+) (\w+)$')
firstLast = re.compile(r'^(\w+) (\w+)$')

# Opens the file 
infile = open(inputfile, 'r')

# Checks if the names match the regular expression
# if they do then the name is used with the append command
for line in infile:
    isFML = firstMiddleLast.match(line)
    isFL = firstLast.match(line)
    if isFML:
        Names.append(isFML.group(3)+ ', ' + isFML.group(1) + ' ' + isFML.group(2) + '\n')
    elif isFL:
        Names.append(isFL.group(2)+ ', ' + isFL.group(1) + '\n')
infile.close()

# Sorts names in a list
Names = sorted(Names)
# Assigns the first argument to fileDirectory
fileDirectory=str(sys.argv[0])
# Finds the '/' in the fileDirectory
lastForwardSlash = fileDirectory.rfind('/')
# Combines the current directory with the file directory
fileDirectory = os.getcwd() + fileDirectory[1:lastForwardSlash]
print( "{}, current {}, file dir".format(os.getcwd(), fileDirectory))

# Compare the current directory with the file directory
# If they are not in the same directory, then they go into the 
# file directory
if os.getcwd() != fileDirectory:
    os.chdir(fileDirectory)
with open(outputfile, 'w') as outfile:
# Writes names to the output file
    for name in Names:
        outfile.write(name)
