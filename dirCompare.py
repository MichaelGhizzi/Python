#!/usr/bin/python
#----------------------------
# Name: Michael Ghizzi
# CPSC 254 8:00pm T/Th
# dirCompare.py dirDiffs.txt
# This program compares the contents of 2 directories
# which are supplied by 2 arguments.
# Three sorted lists are created in dirDiffs.txt
# which compares the similiarities and differences
# from the two directories/arguments
# --------------------------
import os
import sys

# SAME FUNCTION
# Gathers the similarities between both given directories,
# and appends them to a list inside dirDiffs.txt.
# This operation is done recursivly.
def same(dir1, dir2, differencelist):	
    # Base case to exit recursive function
    # if len of directory == 0 then program returns 
    # differencelist	
	if len(dir1)==0:
		return differencelist		
	else:
    # If anything is the same in the files, then they are saved into the same list
		for x in dir2:
			if dir1[0] == x:
				differencelist.append(x)
		return same(dir1[1:],dir2, differencelist)
        
# DIFFERENT FUNCTION
# Gathers the differences between both given directories,
# and appends them to a list inside dirDiffs.txt. 
# This operation is done recursivly.
def different(dir1, dir2, differencelist):	
    # Base case to exit recursive function
    # if len of directory == 0 then program returns 
    # difflist
	if len(dir1)==0:
		return differencelist			
	else:
    # Counter shows how many files are not similar 
    # Then if the count is different combine them to a list
		count=0
		for name in dir2:
			if dir1[0] != name:
				count=1+count
		if count == len(dir2):
			differencelist.append(dir1[0])
	return different(dir1[1:],dir2, differencelist)


# MAIN FUNCTION
def main():
    # Assigns two supplied arguments to the assigned variables
	directOne=sys.argv[1]
	directTwo=sys.argv[2]
    # If the paths do not exist, an error message is displayed and the program exits
	if not os.path.exists(directOne):
		print('ERROR: Path '+directOne+' not available')
		exit(1)
	elif not os.path.exists(directTwo):
		print('ERROR: Path '+directTwo+' not available')
		exit(1)
        
    # Sorts the given lists
	directoryOneList=sorted(os.listdir(directOne))
	directoryTwoList=sorted(os.listdir(directTwo))
    
    # If directory is empty, an error is displayed and the program exits. 
	if len(directoryOneList) == 0:
		print('ERROR: Directory {} is empty'.format(directOne))
		exit(1)
	elif len(directoryTwoList) == 0:
		print('ERROR: Directory {} is empty'.format(directOne))
		exit(1)

    # Declares lists to be saved inside dirDiffs.txt
	differenceOne=[]
	differenceTwo=[]
	sameList=[]
    
    # Saves lists into variables above 
	differenceOne=different(directoryOneList, directoryTwoList, differenceOne)
	differenceTwo=different(directoryTwoList, directoryOneList, differenceTwo)
	sameList=same(directoryOneList, directoryTwoList,sameList)
    
    # Makes sure list is big enough for file length 
	length=[str(len(differenceOne)), str(len(differenceTwo)), str(len(sameList))]
    
    # Assigns file directory to first argument 
	fileDirectory=str(sys.argv[0])
    
    # Assigns forward slash to variable  for formatting purposes 
	format = fileDirectory.rfind('/')
    
	fileDirectory=os.getcwd()+fileDirectory[1:format]

	if os.getcwd() != fileDirectory:
		os.chdir(fileDirectory)
        # Writing the similarities / differences to the file 
	with open('dirDiff.txt','w') as outfile:
		outfile.write('Files inside '+directOne+' that are not in ' +directTwo+'.\n  size of list:'+length[0]+'\n')
		for x in differenceOne:
			outfile.write(x+'\n')
		outfile.write('\nFiles inside '+directTwo+' that are not in ' +directOne+'.\n  size of list:'+length[1]+'\n')
		for x in differenceTwo:
			outfile.write(x+'\n')
		outfile.write('\nSimilar Files inside '+directOne+' and directory '+directTwo+' \n  size of list:'+length[2]+'\n')
		for x in sameList:
			outfile.write(x+'\n')

# If there are three or more arguments, then the program displays an error message 
if __name__ == "__main__":
	if len(sys.argv) == 3:
		main()
	else:
		print("ERROR! USAGE: ./dirCompare.py PATH PATH")
