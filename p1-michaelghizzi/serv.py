###############################################################################
# CPSC 471 Assignment 1
# Fall 2015
#
# Authors: 	Rudy Alvarado, Michael Ghizzi
# Date: 	11/27/2015
# Purpose:  This file implements a server for receiving commands to
#            download, upload, list directory, and to disconnect
###############################################################################
import commands
import subprocess
import sys, re
import socket
import os.path
import time


# sanity check
if len(sys.argv) != 2:
    print('Usage: python serv.py <server port>')
    exit(1)
    
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
        #print(recvBuff)
	
	return recvBuff
    

port_no = sys.argv[1]

# The port on which to listen
listenPort = int(port_no)

# Create a welcome socket. 
welcomeSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
welcomeSock.bind(('', listenPort))

# Start listening on the socket
welcomeSock.listen(5)


print 'Waiting for connections....'
clientSock, addr = welcomeSock.accept() 

while True:
    # Socket will timeout within 2 mins
    welcomeSock.settimeout(120)  
    clientSock.settimeout(120)
    print 'Accepted connection from client: ', addr 
    
    # creating instances for command message to be recieved
    command = ""
    recvBuff = ""
    commandSize = 0
    commandSizeBuff = ""
    # stores the number of bytes from clients command
    commandSizeBuff = recvAll(clientSock, 10)
    commandSize = int(commandSizeBuff)
    commandData = recvAll(clientSock, commandSize)
    command = commandData.rsplit(" ",1)[0]
    # if command is get the server will send file to client
    if command == "get":
        clientSock.settimeout(1)
        start = time.time()
        if len(commandData.rsplit(' ',1)) < 2: 
            print 'Error: Client did not specify a file name'
            exit(1)
        
        elif commandData.rsplit(' ',1)[1] == '':
            print 'Error: Client entered a null file name'
            exit(1)
            
        fileName = commandData.rsplit(' ',1)[1] 
        
        if os.path.isfile(fileName):
            pass
        else:
            print fileName, ' does not exist on server'
            exit(1)
            clientSock.close()
  
        print 'Client is now downloading '+fileName
   
        fileObj = open(fileName, "r")
        numSent = 0
        fileData = None
    
        while True:
        
            fileData = fileObj.read(65536)
        
            if fileData:
                dataSizeStr = str(len(fileData))
            
                while len(dataSizeStr) < 10:
                    dataSizeStr = "0" + dataSizeStr
                
                fileData = dataSizeStr + fileData
            
                numSent = 0
                while len(fileData) > numSent:
                     numSent += clientSock.send(fileData[numSent:])         
            else:
                break        
        
        print 'Client has Successfully downloaded '+ fileName
        print 'The file size was ', str(numSent), 'bytes.'
        
        clientSock.settimeout(None)
            
    # if the command is put the server will recieve an upload from client
    elif command == "put":
        clientSock.settimeout(1)
        numSent = 0
        fileData = None
        fileName = commandData.rsplit(' ',1)[1]
        
        print 'Client is now uploading '+fileName
        
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
        fileSizeBuff = recvAll(clientSock, 10)
		
    	# Get the file size
        fileSize = int(fileSizeBuff)
        print "The file size is: ", fileSize
	
    	# Get the file data
        fileData = recvAll(clientSock, fileSize)
    
        print "The file data is: "
        print fileData
        clientSock.settimeout(None)
    # if command is ls it will perform ls -l and send a list to client 
    elif command == "ls":
        clientSock.settimeout(1)
        # server performs ls -l
        print 'Client is now listing the directing'
        listOfDir = commands.getstatusoutput('ls -l')
    
        if listOfDir[0] > 0:
            print 'Error: ls command exited with status of ' + listOfDir[0]
        
        lengthListStr = str(len(listOfDir[1]))
            
        while len(lengthListStr) < 10:
            lengthListStr = '0' +lengthListStr
        commandData = lengthListStr + listOfDir[1]

        numSent = 0
    
        while len(listOfDir[1]) > numSent:  
            numSent += clientSock.send(commandData[numSent:])
        
        print 'Successfully sent this many bytes:', numSent
        clientSock.settimeout(None)
    # if command is quit server and client will disconnect from each other
    elif command == "quit" :
        clientSock.settimeout(1)
        print 'Client is now disconnecting from server'
        clientSock.close() 
        print 'Client sucessfully disconnected from server'
        break
        clientSock.settimeout(None)
    # if command is none of the above a Failure message will be shown    
    else:
    
        print 'Failure, ' + command + 'not recognized.'
        clientSock.close()
        break
        
# python serv.py localhost portnumber


        
