#!/usr/bin/python

# PROGRAMMER: Michael Ghizzi
# CPSC-353 Fall 2015
# Project #2
# COMPILER: Python2.7
# FILE: encryption.py
# FILE USAGE: ./program2.py <prime> <generator> <x number> <y number> 

#Program Description:
# This program prompts the user to enter in a prime number, generator number,
# x and y value below the value of 10.
# We will then demonstrate key encryption by using the example in 415 to show how
# the users Alice and Bob will communicate with eachother, using a secure network. 

#IMPORTS:
#-----------------
import os
import sys      
import re       #Used for regular expressions
import string 
# -----------------
# Takes in FIVE arguments, the ./program2.py <prime number> <generator number> <x number> <y number>
# -----------------
if len(sys.argv) != 5:
    print('USEAGE: ./project2.py <prime number> <generator number> <x number> <y number>')
    exit(1)
#Assigns arguments to appropriate variables
#-----------------
prime = sys.argv[1]
generator = sys.argv[2]
x = sys.argv[3]
y = sys.argv[4]
#-----------------

#Assign regular expressions for correct input results. 
primeNumbers = re.compile(r'^(2|3|5|7|11|13|17|19|23|29|31|37|41|43|47|53|59|61|67|71|73|79|83|89|97)$', re.IGNORECASE)
generatorNumbers = re.compile(r'^[0-97]', re.IGNORECASE)
isPrime = primeNumbers.match(prime)
isGenerator = generatorNumbers.match(generator)

print
##Checking to see if the first number is prime and less than 100 using regular expressions. 
if isPrime:
    print "First argument is a prime number and less than 100"
else:
    print "ERROR: First number is not prime! Now exiting!"
    exit(0)

#We must typecast in order to make the arguments a valid integer (for comparison below)
prime = int(prime)
generator = int(generator)
x = int(x)
y = int(y)

# Checking to see if prime is > generator 
if prime > generator:
    print "Second argument (Generator) is less than the prime number"
else:
    print "ERROR: Generator number is greater than Prime number! Now exiting!"
    exit(0)

print "P Value:", prime
print "G Value:", generator

# Checking if x < 10
if x > 10:
    print "ERROR: X cannot be greater than 10"
    print "Now exiting!"
    exit(0)
else:
    print "x Value:", x

# Checking if y < 10
if y > 10:
    print "ERROR: Y cannot be greater than 10"
    print "Now exiting!"
    exit(0)
else:
    print "y Value:", y 

# Alice picks a random positive number x in Zp and uses it to compute
# X = g^x mod p. She sends X to Bob. 
test1 = (generator ** x) % prime
 
# Bob picks a random positive number y in Zp and uses it to compute
# Y = g^y mod p. He sends Y to Alice. 
test2 = (generator ** y) % prime

print "Sending X to Bob Value: " , test1
print "Sending Y to Alice Value: ", test2

# Alice Computes the secret key as: k1 = Y^x mod p 
K1 = (test2 ** x) % prime
print "K2 Value: ", K1

# Bob Computes the secret key as: k2 = X^y mod p 
K2 = (test1 ** y) % prime
print "\nK1 Value: ", K2

if (K1 == K2):
    print "Therefore K1 = K2"
else:
    print "ERROR: K1 != K2."
# End of program ---------------------
