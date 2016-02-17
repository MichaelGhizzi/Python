#!/usr/bin/python

#PROGRAMMER: Michael Ghizzi
#CPSC-351 Summer 2015
#ASSIGNMENT: RoundRobin.py

import os
import sys

avg = 0
count = 0
tat = []
queue = []
queue.append(5)
queue.append(2)
queue.append(7)
queue.append(6)
queue.append(4)
total = len(queue)

print "Queue at time t=0  : j1=", queue[0], "-->", "j2=", queue[1], "-->", "j3=", queue[2], "-->", "j4=", queue[3], "-->", "j5=", queue[4],  "-->", "NULL"

##CALCULATIONS FOR ROUND 1: 
#--------------------------
x = len(queue)
for n in range(x):
    if queue[n] >= 2:
        queue[n] -= 2;
        count += 2;
        if queue[n] == 0:
            tat.append(count);
    elif queue[n] == 1:
        queue[n] -= 1;
        count += 1;
        if queue[n] == 0:
            tat.append(count);
    elif queue[n] == 0:
        queue.pop(n);
##DEBUGGING:
#print "TAT ROUND 1: ", tat
#print "QUEUE ROUND 1: ", queue
#--------------------------

#PRINTING ROUND 1 RESULTS:
#--------------------------
#print "Queue after round 1: ", "j1=", queue[0], "-->", "j2=", queue[1], "-->", "j3=", queue[2], "-->", "j4=", queue[3], "-->", "j5=", queue[4],  "-->", "NULL"
print "Queue after round 1:",
if queue[0] > 0:
    print "j1=", queue[0], "-->",
else:
    queue.pop(0);
if queue[1] > 0:
    print "j2=", queue[1], "-->",
if queue[2] > 0:
    print "j3=", queue[2], "-->",
if queue[3] > 0:
    print "j4=", queue[3], "-->",
if queue[4] > 0:
    print "j5=", queue[4],
print "-->", "NULL"
#--------------------------

##CALCULATIONS FOR ROUND 2: 
#--------------------------
y = len(queue)
for n in range(y):
    if queue[n] >= 2:
        queue[n] -= 2;
        count += 2;
        if queue[n] == 0:
            tat.append(count);
    elif queue[n] == 1:
        queue[n] -= 1;
        count += 1;
        if queue[n] == 0:
            tat.append(count);
    #elif queue[n] == 0:
    #    print '',
#--------------------------    

#PRINTING ROUND 2 RESULTS:
#--------------------------
print "Queue after round 2:",
if queue[0] > 0:
    print "j1=", queue[0], "-->",
if queue[1] > 0:
    print "j2=", queue[1], "-->",
if queue[2] > 0:
    print "j3=", queue[2], "-->",
if queue[3] > 0:
    print "j4=", queue[3], "-->",
if queue[4] > 0:
    print "j5=", queue[4],
print "NULL"
#--------------------------

##CALCULATIONS FOR ROUND 3: 
#--------------------------
z = len(queue)
for n in range(z):
    if queue[n] >= 2:
        queue[n] -= 2;
        count += 2;
        if queue[n] == 0:
            tat.append(count);
    elif queue[n] == 1:
        queue[n] -= 1;
        count += 1;
        if queue[n] == 0:
            tat.append(count);
    elif queue[n] == 0:
        sys.stdout.write("")
#--------------------------

#PRINTING ROUND 3 RESULTS:
#--------------------------
print "Queue after round 3:",
if queue[0] > 0:
    print "j1=", queue[0], "-->",
if queue[1] > 0:
    print "j2=", queue[1], "-->",
if queue[2] > 0:
    print "j3=", queue[2], "-->",
if queue[3] > 0:
    print "j4=", queue[3], "-->",
if queue[4] > 0:
    print "j5=", queue[4],
print "NULL",
#--------------------------

##CALCULATIONS FOR ROUND 4: 
#--------------------------
s = len(queue)
for n in range(s):
    if queue[n] >= 2:
        queue[n] -= 2;
        count += 2;
        if queue[n] == 0:
            tat.append(count);
    elif queue[n] == 1:
        queue[n] -= 1;
        count += 1;
        if queue[n] == 0:
            tat.append(count);
    elif queue[n] == 0:
        sys.stdout.write("")
#--------------------------   

#PRINTING ROUND 4 RESULTS:
#--------------------------
print "\nQueue after round 4:",
if queue[0] > 0:
    print "j1=", queue[0], "-->",
if queue[1] > 0:
    print "j2=", queue[1], "-->",
if queue[2] > 0:
    print "j3=", queue[2], "-->",
if queue[3] > 0:
    print "j4=", queue[3], "-->",
if queue[4] > 0:
    print "j5=", queue[4],
print "NULL"
#--------------------------

#CALCULATING AVERAGE:
#--------------------------
for x in tat:
	avg += x
#--------------------------

#PRINTING RESULTS OF AVG:
#--------------------------
print "\tAverage TAT =", float(float(avg)/float(total))
#--------------------------

#END OF PROGRAM

#OUTPUT:
#--------------------------
# Queue at time t=0  : j1= 5 --> j2= 2 --> j3= 7 --> j4= 6 --> j5= 4 --> NULL
# Queue after round 1: j1= 3 --> j3= 5 --> j4= 4 --> j5= 2 --> NULL
# Queue after round 2: j1= 1 --> j3= 3 --> j4= 2 --> NULL
# Queue after round 3: j3= 1 --> NULL
# Queue after round 4: NULL
#     Average TAT = 17.6
#--------------------------
#END OF OUTPUT
