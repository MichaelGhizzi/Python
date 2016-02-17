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
#FILE: project1.py inputfile.txt outputfile.txt
#FILE USAGE: ./project1.py <inputfile.txt> <outputfile.txt>

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
#-----------------

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
outfile = open(outputfile, 'w')
outfile.write("OUTPUT:\n")

#REGULAR EXPRESSIONS:
#-----------------
#the = re.compile(r'^(The|tHe|thE|THE|the)$', re.IGNORECASE)
the = re.compile(r'^(the)$', re.IGNORECASE)
principles = re.compile(r'(principles)$', re.IGNORECASE) 
punc = re.compile(r'^([_]|[-]|[:]|[;]|["]|[\']|[?]|[.]|[,]|[>]|[<]|[~]|[`]|[!]|[@]|[$]|[%]|[&]|[*]|[(]|[)]|[[]|(])|[|]|[/]|[+]|[=]|[{]|[}]|[\^]|[\#])$', re.IGNORECASE)
alphabet = re.compile(r'^[a-z]', re.IGNORECASE)
a = re.compile(r'^[a]', re.IGNORECASE)
b = re.compile(r'^[b]', re.IGNORECASE)
c = re.compile(r'^[c]', re.IGNORECASE)
d = re.compile(r'^[d]', re.IGNORECASE)
e = re.compile(r'^[e]', re.IGNORECASE)
f = re.compile(r'^[f]', re.IGNORECASE)
g = re.compile(r'^[g]', re.IGNORECASE)
h = re.compile(r'^[h]', re.IGNORECASE)
i = re.compile(r'^[i]', re.IGNORECASE)
j = re.compile(r'^[j]', re.IGNORECASE)
k = re.compile(r'^[k]', re.IGNORECASE)
l = re.compile(r'^[l]', re.IGNORECASE)
m = re.compile(r'^[m]', re.IGNORECASE)
n = re.compile(r'^[n]', re.IGNORECASE)
o = re.compile(r'^[o]', re.IGNORECASE)
p = re.compile(r'^[p]', re.IGNORECASE)
q = re.compile(r'^[q]', re.IGNORECASE)
r = re.compile(r'^[r]', re.IGNORECASE)
s = re.compile(r'^[s]', re.IGNORECASE)
t = re.compile(r'^[t]', re.IGNORECASE)
u = re.compile(r'^[u]', re.IGNORECASE)
v = re.compile(r'^[v]', re.IGNORECASE)
w = re.compile(r'^[w]', re.IGNORECASE)
x = re.compile(r'^[x]', re.IGNORECASE)
y = re.compile(r'^[y]', re.IGNORECASE)
z = re.compile(r'^[z]', re.IGNORECASE)

# Implementing a counter variable for each letter initialized to 0
# Can make into an 27 size array, I WILL DO THIS LATER
countA = 0
countB = 0
countC = 0
countD = 0
countE = 0
countF = 0
countG = 0
countH = 0
countI = 0
countJ = 0
countK = 0
countL = 0
countM = 0
countN = 0
countO = 0
countP = 0
countQ = 0
countR = 0
countS = 0
countT = 0
countU = 0
countV = 0
countW = 0
countX = 0
countY = 0
countZ = 0
countThe = 0
countPrinciples = 0
stack = []
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

def parser(stack, countA, countB, countC, countD, countE, countF, countG, countH, countI, countJ, countK, countL, countM, countN, countO, countP, countQ, countR, countS, countT, countU, countV, countW, countX, countY, countZ, countThe, countPrinciples):
    if len(stack) > 0:
        if stack[0] == 'a':
            countA += 1
            stack.pop(0)
            parser(stack, countA, countB, countC, countD, countE, countF, countG, countH, countI, countJ, countK, countL, countM, countN, countO, countP, countQ, countR, countS, countT, countU, countV, countW, countX, countY, countZ, countThe, countPrinciples
);
        elif stack[0] == 'b':
            countB += 1
            stack.pop(0)
            parser(stack, countA, countB, countC, countD, countE, countF, countG, countH, countI, countJ, countK, countL, countM, countN, countO, countP, countQ, countR, countS, countT, countU, countV, countW, countX, countY, countZ, countThe, countPrinciples
);
        elif stack[0] == 'c':
            countC += 1
            stack.pop(0)
            parser(stack, countA, countB, countC, countD, countE, countF, countG, countH, countI, countJ, countK, countL, countM, countN, countO, countP, countQ, countR, countS, countT, countU, countV, countW, countX, countY, countZ, countThe, countPrinciples
);
        elif stack[0] == 'd':
            countD += 1
            stack.pop(0)
            parser(stack, countA, countB, countC, countD, countE, countF, countG, countH, countI, countJ, countK, countL, countM, countN, countO, countP, countQ, countR, countS, countT, countU, countV, countW, countX, countY, countZ, countThe, countPrinciples
);
        elif stack[0] == 'e':
            countE += 1
            stack.pop(0)
            parser(stack, countA, countB, countC, countD, countE, countF, countG, countH, countI, countJ, countK, countL, countM, countN, countO, countP, countQ, countR, countS, countT, countU, countV, countW, countX, countY, countZ, countThe, countPrinciples
);
        elif stack[0] == 'f':
            countF += 1
            stack.pop(0)
            parser(stack, countA, countB, countC, countD, countE, countF, countG, countH, countI, countJ, countK, countL, countM, countN, countO, countP, countQ, countR, countS, countT, countU, countV, countW, countX, countY, countZ, countThe, countPrinciples
);
        elif stack[0] == 'g':
            countG += 1
            stack.pop(0)
            parser(stack, countA, countB, countC, countD, countE, countF, countG, countH, countI, countJ, countK, countL, countM, countN, countO, countP, countQ, countR, countS, countT, countU, countV, countW, countX, countY, countZ, countThe, countPrinciples
);
        elif stack[0] == 'h':
            countH += 1
            stack.pop(0)
            parser(stack, countA, countB, countC, countD, countE, countF, countG, countH, countI, countJ, countK, countL, countM, countN, countO, countP, countQ, countR, countS, countT, countU, countV, countW, countX, countY, countZ, countThe, countPrinciples
);
        elif stack[0] == 'i':
            countI += 1
            stack.pop(0)
            parser(stack, countA, countB, countC, countD, countE, countF, countG, countH, countI, countJ, countK, countL, countM, countN, countO, countP, countQ, countR, countS, countT, countU, countV, countW, countX, countY, countZ, countThe, countPrinciples
);
        elif stack[0] == 'j':
            countJ += 1
            stack.pop(0)
            parser(stack, countA, countB, countC, countD, countE, countF, countG, countH, countI, countJ, countK, countL, countM, countN, countO, countP, countQ, countR, countS, countT, countU, countV, countW, countX, countY, countZ, countThe, countPrinciples
);
        elif stack[0] == 'k':
            countK += 1
            stack.pop(0)
            parser(stack, countA, countB, countC, countD, countE, countF, countG, countH, countI, countJ, countK, countL, countM, countN, countO, countP, countQ, countR, countS, countT, countU, countV, countW, countX, countY, countZ, countThe, countPrinciples
);
        elif stack[0] == 'l':
            countL += 1
            stack.pop(0)
            parser(stack, countA, countB, countC, countD, countE, countF, countG, countH, countI, countJ, countK, countL, countM, countN, countO, countP, countQ, countR, countS, countT, countU, countV, countW, countX, countY, countZ, countThe, countPrinciples
);
        elif stack[0] == 'm':
            countM += 1
            stack.pop(0)
            parser(stack, countA, countB, countC, countD, countE, countF, countG, countH, countI, countJ, countK, countL, countM, countN, countO, countP, countQ, countR, countS, countT, countU, countV, countW, countX, countY, countZ, countThe, countPrinciples
);
        elif stack[0] == 'n':
            countN += 1
            stack.pop(0)
            parser(stack, countA, countB, countC, countD, countE, countF, countG, countH, countI, countJ, countK, countL, countM, countN, countO, countP, countQ, countR, countS, countT, countU, countV, countW, countX, countY, countZ, countThe, countPrinciples
);
        elif stack[0] == 'o':
            countO += 1
            stack.pop(0)
            parser(stack, countA, countB, countC, countD, countE, countF, countG, countH, countI, countJ, countK, countL, countM, countN, countO, countP, countQ, countR, countS, countT, countU, countV, countW, countX, countY, countZ, countThe, countPrinciples
);
        elif stack[0] == 'p':
            countP += 1
            stack.pop(0)
            parser(stack, countA, countB, countC, countD, countE, countF, countG, countH, countI, countJ, countK, countL, countM, countN, countO, countP, countQ, countR, countS, countT, countU, countV, countW, countX, countY, countZ, countThe, countPrinciples
);
        elif stack[0] == 'q':
            countQ += 1
            stack.pop(0)
            parser(stack, countA, countB, countC, countD, countE, countF, countG, countH, countI, countJ, countK, countL, countM, countN, countO, countP, countQ, countR, countS, countT, countU, countV, countW, countX, countY, countZ, countThe, countPrinciples
);
        elif stack[0] == 'r':
            countR += 1
            stack.pop(0)
            parser(stack, countA, countB, countC, countD, countE, countF, countG, countH, countI, countJ, countK, countL, countM, countN, countO, countP, countQ, countR, countS, countT, countU, countV, countW, countX, countY, countZ, countThe, countPrinciples
);
        elif stack[0] == 's':
            countS += 1
            stack.pop(0)
            parser(stack, countA, countB, countC, countD, countE, countF, countG, countH, countI, countJ, countK, countL, countM, countN, countO, countP, countQ, countR, countS, countT, countU, countV, countW, countX, countY, countZ, countThe, countPrinciples
);
        elif stack[0] == 't':
            countT += 1
            stack.pop(0)
            parser(stack, countA, countB, countC, countD, countE, countF, countG, countH, countI, countJ, countK, countL, countM, countN, countO, countP, countQ, countR, countS, countT, countU, countV, countW, countX, countY, countZ, countThe, countPrinciples
);
        elif stack[0] == 'u':
            countU += 1
            stack.pop(0)
            parser(stack, countA, countB, countC, countD, countE, countF, countG, countH, countI, countJ, countK, countL, countM, countN, countO, countP, countQ, countR, countS, countT, countU, countV, countW, countX, countY, countZ, countThe, countPrinciples
);
        elif stack[0] == 'v':
            countV += 1
            stack.pop(0)
            parser(stack, countA, countB, countC, countD, countE, countF, countG, countH, countI, countJ, countK, countL, countM, countN, countO, countP, countQ, countR, countS, countT, countU, countV, countW, countX, countY, countZ, countThe, countPrinciples
);
        elif stack[0] == 'w':
            countW += 1
            stack.pop(0)
            parser(stack, countA, countB, countC, countD, countE, countF, countG, countH, countI, countJ, countK, countL, countM, countN, countO, countP, countQ, countR, countS, countT, countU, countV, countW, countX, countY, countZ, countThe, countPrinciples
);
        elif stack[0] == 'x':
            countX += 1
            stack.pop(0)
            parser(stack, countA, countB, countC, countD, countE, countF, countG, countH, countI, countJ, countK, countL, countM, countN, countO, countP, countQ, countR, countS, countT, countU, countV, countW, countX, countY, countZ, countThe, countPrinciples
);
        elif stack[0] == 'y':
            countY += 1
            stack.pop(0)
            parser(stack, countA, countB, countC, countD, countE, countF, countG, countH, countI, countJ, countK, countL, countM, countN, countO, countP, countQ, countR, countS, countT, countU, countV, countW, countX, countY, countZ, countThe, countPrinciples
);
        elif stack[0] == 'z':
            countZ += 1
            stack.pop(0)
            parser(stack, countA, countB, countC, countD, countE, countF, countG, countH, countI, countJ, countK, countL, countM, countN, countO, countP, countQ, countR, countS, countT, countU, countV, countW, countX, countY, countZ, countThe, countPrinciples
);  
    elif len(stack) <= 0:
        print "Count A: ", countA
        print "Count B: ", countB
        print "Count C: ", countC
        print "Count D: ", countD
        print "Count E: ", countE
        print "Count F: ", countF
        print "Count G: ", countG
        print "Count H: ", countH
        print "Count I: ", countI
        print "Count J: ", countJ
        print "Count K: ", countK
        print "Count L: ", countL
        print "Count M: ", countM
        print "Count N: ", countN
        print "Count O: ", countO
        print "Count P: ", countP
        print "Count Q: ", countQ
        print "Count R: ", countR
        print "Count S: ", countS
        print "Count T: ", countT
        print "Count U: ", countU
        print "Count V: ", countV
        print "Count W: ", countW
        print "Count X: ", countX
        print "Count Y: ", countY
        print "Count Z: ", countZ
        print "Count The: ", countThe
        print "Count Principles: ", countPrinciples

        infile.close()
        outfile.close()

        exit(0)

parser(stack, countA, countB, countC, countD, countE, countF, countG, countH, countI, countJ, countK, countL, countM, countN, countO, countP, countQ, countR, countS, countT, countU, countV, countW, countX, countY, countZ, countThe, countPrinciples
);
