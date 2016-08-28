###############################################################################
# CPSC 471 Assignment 1
# Fall 2015
#
# Authors: 	Rudy Alvarado, Michael Ghizzi
# Date: 	11/27/2015
# Purpose:  This file implements a client for sending commands to
#            download, upload, list directory, and to disconnect
###############################################################################
import socket
import os
import subprocess
import sys, re

#sanity checks
if len(sys.argv) != 3:
    print('Usage: python cli.py <server maching> <server port>')
    exit(1)

lookup = sys.argv[1]
port_no = sys.argv[2]

# Server address
serverAddr = "localhost"

# Server port
serverPort = 1234


# Create a TCP socket
connSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
connSock.connect((serverAddr, serverPort))

# The number of bytes sent
numSent = 0

# The file data
fileData = None

def menu():
    print("\nftp> get <filename>\nftp> put <filename>\nftp> ls\nftp> quit\n")
    
# this code was provided by the file sendfileserv.py
def recvAll(sock, numBytes):

	# The buffer
	recvBuff = ""
	
	# The temporary buffer
	tmpBuff = ""
	
	# Keep receiving till all is received
	while len(recvBuff) < numBytes:
		
		# Attempt to receive bytes
		tmpBuff =  sock.recv(numBytes)
		
		# The other side has closed the socket
		if not tmpBuff:
			break
		
		# Add the received bytes to the buffer
		recvBuff += tmpBuff
	
	return recvBuff
    
#print(lookup, port_no)
while True:
    #menu will be displayed 
    menu()

    choice = str(raw_input('Please enter a choice: '))
    
    nchoice = choice.split()
    choiceSizeStr = str(len(choice))
    # pad choice with 0's for protocol purposes
    while len(choiceSizeStr) < 10:
        choiceSizeStr = '0' + choiceSizeStr
    choice = choiceSizeStr+ choice    
    
    # sends choice to server
    connSock.send(choice)
    
    #if choice is get the client will now download file from seerver
    if nchoice[0] == 'get':
        choiceData = choice.rsplit(' ',1)
        
        if len(choiceData) < 2:
            print ' no file was given, now disconnecting '
            connSock.close()
            exit(1)
            
        print 'Downloading',choiceData[1]
        
    	# The buffer to all data received from the
    	# the client.
       
        fileData = ""
	
    	# The temporary buffer to store the received
    	# data.
        recvBuff = ""
	
    	# The size of the incoming file
        fileSize = 0	
	
    	# The buffer containing the file size
        fileSizeBuff = ""
            
    	# Receive the first 10 bytes indicating the
    	# size of the file
        fileSizeBuff = recvAll(connSock, 10)
		
    	# Get the file size
        fileSize = int(fileSizeBuff)
        print "The file size is: ", fileSize
	
    	# Get the file data
        fileData = recvAll(connSock, fileSize)
    
        print "The file data is: "
        print fileData
    # if choice is put the client will not upload the file to server
    elif nchoice[0] == 'put':

        choiceData = choice.rsplit(' ',1)
        
        #if choiceData is less than two no file was given
        if len(choiceData) < 2:
            print 'No file was given, now disconnecting '
            connSock.close()
            exit(1)
    
        print 'You are now sending '+choice.rsplit(' ',1)[1]
    
        fileName = choice.rsplit(' ',1)[1]
        # if file does not exist then disconnect from server
        if os.path.isfile(fileName):
            pass
        else:
            print fileName, ' does not exist on server'
            exit(1)
            connSock.close()
            
        fileObj = open(fileName, "r")
        numSent = 0
        fileData = None
        # opens and sends file to server for upload
        while True: 
            fileData = fileObj.read(65536)
        
            if fileData:
                dataSizeStr = str(len(fileData))
            
                while len(dataSizeStr) < 10:
                    dataSizeStr = "0" + dataSizeStr
                
                fileData = dataSizeStr + fileData
            
                numSent = 0

                while len(fileData) > numSent:
                     numSent += connSock.send(fileData[numSent:])         
            else:
                break  
                      
        print 'Successfully sent'+choice.rsplit(' ',1)[1]

    #if choice was ls the client will ask server for a list of the directory
    elif nchoice[0] == 'ls':

        print 'These are the file in the server directory'
        
        #instances for recieving list
        
        revcBuff = ""
        listSize = 0
        listSizeBuff = ""
        listSizeBuff = recvAll(connSock,10)

        listSize = int(listSizeBuff)
        #calls recvall fucntion to retrieve list from server
        listData = recvAll(connSock,listSize)
        
        print listData

    #if choice is quit then client will disconnect
    elif nchoice[0] == 'quit':

        print "You are now disconnecting from the server"
        connSock.close()
        print 'You have now disconnected from the server'
        break

    #if choice is not one of the above an error message will occur then client will disconnect
    else:
        print "Invalid option you will now be disconnected, try again :)"
        connSock.close()
        break




