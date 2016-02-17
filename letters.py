#!/usr/bin/python
#shebang line, also includes imports for files and regular expressions
#shebang line found using command: 'which python' in terminal
#Need 'python' to run, cannot use 'python3'
#'python3' uses different syntax and there will be a compiler/printing error 
#when using the 'python3' shebang line

#PROGRAMMER: Michael Ghizzi
#CPSC-353 Fall 2015
#Project #1
#COMPILER: Python2.7
#FILE: letters.py inputfile.txt outputfile.txt
#FILE USAGE: ./letters.py <inputfile.txt> <outputfile.txt>

#Program Description: 
# This program will read each word and determine if it is 'the' or 'principles'.
# If the regular expression does not match any of those two words, the program will then
# read character by character, while incrementing a conter for each letter.
# Once the file is done reading, it will write the results of the counters in an output file.

#IMPORTS:
#-----------------
import os
import sys      
import os.path  #Used to read / write files
import re       #Used for regular expressions
import string
#-----------------
sys.setrecursionlimit(15000)
#Takes in THREEE arguments, the ./project1.py python script and the
#"inputname.txt" which includes the source code we want to read
#"outputname.txt" includes where the output will be written too
#-----------------
if len(sys.argv) != 3:
    print('USEAGE: ./project1.py <inputname.txt> <outputname.txt>')
    exit(1)
if os.path.isfile(sys.argv[1]):
    pass
else:
    print('ERROR: File does not exist. Usage ./project1.py <inputname.txt> <outputname.txt>')
    exit(1)
#-----------------

#Assigns files to appropriate variables  
#-----------------
inputfile = sys.argv[1]
outputfile = sys.argv[2]
#-----------------

#Opens the files to be read / written to
infile = open(inputfile, 'r')
sys.stdout = open(outputfile, 'w')

#REGULAR EXPRESSIONS:
#-----------------
the = re.compile(r'^(the)$', re.IGNORECASE)
principles = re.compile(r'(principles)$', re.IGNORECASE) 
punc = re.compile(r'^([_]|[-]|[:]|[;]|["]|[\']|[?]|[.]|[,]|[>]|[<]|[~]|[`]|[!]|[@]|[$]|[%]|[&]|[*]|[(]|[)]|[[]|(])|[|]|[/]|[+]|[=]|[{]|[}]|[\^]|[\#])$', re.IGNORECASE)
alphabet = re.compile(r'^[a-z]', re.IGNORECASE)

# Implementing a counter variable (array) for each letter initialized to 0
# Can make into an 26 size array
letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','Q','X','Y','Z']
        #A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
array = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
stack = []
# Two variables that will keep track of the number of times 'the' and 'principles' is in the file
countThe = 0
countPrinciples = 0
index1 = 0
countLong = 0

#First we read in each character from the file.
#If the character matches our regular expression for the alphabet characters
#It will then append the character a-z onto the stack
for line in infile:                         ##For each line in the file
    line = line.rstrip('\n')                ## Getting rid of all white space
    line1 = line.lower().split()            ## Makes sure all characters are lower case

    for lol in line:                          
        isAlphabet = alphabet.match(lol)
        for ch in lol:                      ##Make sure we are adding only characters we want to the stack
            if isAlphabet:                  ##Checking our isAlphabet regular expression
                stack.append(lol)           ##Appending the character to the stack a-z
infile.close()                              ##Closes the file

#We re-open the file to find the words 'the' and 'principles'
infile = open(inputfile, 'r')
for line in infile:
    line = line.rstrip('\n')
    line1 = line.lower().split()

    for lol in line1:
        isThe = the.match(lol)
        isPrinciples = principles.match(lol)

       ##Adding all words 'The' and 'Principles' to increment variable
        if isThe:
            countThe += 1
        elif isPrinciples:
            countPrinciples += 1
infile.close    #Close the file

#Makes a stack with all the words in the file
wordLong = []
maxLength = []
with open('input.txt','r') as f:
    for line in f:
        for word in line.split():
           word = ''.join([c for c in word if c not in ('.',':',';','!', '?', '\'',',','[',']','(',')','_','-','\"',)])
           wordLong.append(word)
           maxLength.append(word)
#--------------------------------

#Find the words with the longest length
#-------------------------------
y = 0
longestWords = []
for item in wordLong:
    if len(item) > y:
        longestWords = [item]
        y = len(item)
    elif len(item) == y:
        longestWords.append(item)
#-------------------------------
## This function will increment our array variable for each character [a-z] in the stack
## Once the stack is empty, it will output each count of character and exit the program

#for line in stack:                              ##If stack length is > 0 
   # if len(stack) >= 0:
while stack:
    if len(stack) < 0:
        break  
    elif stack[0].lower() == 'a':                        ##If the stack is 'a'
        array[0] = array[0] + 1                        ##Increment first element in the array stack by 1
        stack.pop(0)                                   ##Pop off the 'a' from the stack
    elif stack[0].lower() == 'b':
        array[1] = array[1] + 1
        stack.pop(0)
    elif stack[0].lower() == 'c':
        array[2] = array[2] + 1
        stack.pop(0)
    elif stack[0].lower() == 'd':
        array[3] = array[3] + 1
        stack.pop(0)
    elif stack[0].lower() == 'e':
        array[4] = array[4] + 1
        stack.pop(0)
    elif stack[0].lower() == 'f':
        array[5] = array[5] + 1
        stack.pop(0)
    elif stack[0].lower() == 'g':
        array[6] = array[6] + 1
        stack.pop(0)
    elif stack[0].lower() == 'h':
        array[7] = array[7] + 1
        stack.pop(0)
    elif stack[0].lower() == 'i':
        array[8] = array[8] + 1
        stack.pop(0)
    elif stack[0].lower() == 'j':
        array[9] = array[9] + 1
        stack.pop(0)
    elif stack[0].lower() == 'k':
        array[10] = array[10] + 1
        stack.pop(0)
    elif stack[0].lower() == 'l':
        array[11] = array[11] + 1
        stack.pop(0)
    elif stack[0].lower() == 'm':
        array[12] = array[12] + 1
        stack.pop(0)
    elif stack[0].lower() == 'n':
        array[13] = array[13] + 1
        stack.pop(0)
    elif stack[0].lower() == 'o':
        array[14] = array[14] + 1
        stack.pop(0)
    elif stack[0].lower() == 'p':
        array[15] = array[15] + 1
        stack.pop(0)
    elif stack[0].lower() == 'q':
        array[16] = array[16] + 1
        stack.pop(0)
    elif stack[0].lower() == 'r':
        array[17] = array[17] + 1
        stack.pop(0)
    elif stack[0].lower() == 's':
        array[18] = array[18] + 1
        stack.pop(0)
    elif stack[0].lower() == 't':
        array[19] = array[19] + 1
        stack.pop(0)
    elif stack[0].lower() == 'u':
        array[20] = array[20] + 1
        stack.pop(0)
    elif stack[0].lower() == 'v':
        array[21] = array[21] + 1
        stack.pop(0)
    elif stack[0].lower() == 'w':
        array[22] = array[22] + 1
        stack.pop(0)
    elif stack[0].lower() == 'x':
        array[23] = array[23] + 1
        stack.pop(0)
    elif stack[0].lower() == 'y':
        array[24] = array[24] + 1
        stack.pop(0)
    elif stack[0].lower() == 'z':
        array[25] = array[25] + 1
        stack.pop(0)
        
index = 0
index4 = 0;

print "Number of letters: "
for char in letters:        ##For each character in letters, print out the letters and array
    print letters[index],"-", array[index]
    index += 1              ##Increments index array by 1
print "Count The: ", countThe   ##Prints out countThe and countPrinciples
print "Count Principles: ", countPrinciples
print "Longest Words:",
for word in longestWords:   
    if len(longestWords) >= 0:      ##Prints out array which contains the longest words
        print longestWords[index4],
        index4 += 1

infile.close()
exit(0)         ##Exits the program

##Note: I would of loved to make the for loop a recursive function, however my computer
##      did not have enough memory to run it

