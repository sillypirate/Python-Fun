###########################
# smtp.py                 #
# @arthor Matthew Collins #
# Feb 13, 2015		  #
###########################

#"""This program sends a default message to a default email address using the"""
#"""Simple Mail Transfer protocol"""

from socket import *
import ssl
import sys

#Begins attempting to establish a connection with gmail.com
mailserver = "smtp.gmail.com"
port = 465 #gmail must connect on port 465
clientSocket = socket(AF_INET, SOCK_STREAM)
ssl_clientSocket = ssl.wrap_socket(clientSocket)
ssl_clientSocket.connect((mailserver, port))
recv = ssl_clientSocket.recv(1024)
print recv
print "Connecting to gmail.com\n"


#Sending the Helo command in order establish a mail connection
#If it is successful, it will respond with a 250
#If not, it will print an error messag and will terminate
HELO = 'HELO Alice\r\n'
ssl_clientSocket.send(HELO)
recv1 = ssl_clientSocket.recv(1024)
if recv1[:3] == '250':
	print recv1
	print "Connection established with gmail.com\n"
else:
	print "Could not connect with gmail.com."
	sys.exit()
#/Helo Command	
	
#Sending the Auth Login command in order to log into gmail.com
#If it is successful, it will respond with a 334
#If it fails, it will print an error message and will terminate
auth = 'AUTH LOGIN\r\n'
ssl_clientSocket.send(auth)
recv2 = ssl_clientSocket.recv(1024)
if recv2[:3] == '334':
	print recv2
	print "Starting Login Attempt\n"
else:
	print "Login attempt failed"
	sys.exit()
#/Auth Login Command

#Sending sillypirate24@gmail.com as a username
#The username must be Encoded in Base64 Format
#If it is successful, it will respond with 334
#If not, it will print an error message and will terminate
user = 'c2lsbHlwaXJhdGUyNEBnbWFpbC5jb20=\r\n'
ssl_clientSocket.send(user)
recv3 = ssl_clientSocket.recv(1024)
if recv3[:3] == '334':
	print recv3
	print "Logging in as sillypirate24@gmail.com\n"
else:
	print "Login name not accepted"
	sys.exit()
#/user name input

#Sending the password
#The password must be Encoded in Base64 Format
#If it is successful, it will respond with 235
#If not, it will print an error message and will terminate
pswrd = 'MTc1a2VuaXRoYQ==\r\n'
ssl_clientSocket.send(pswrd)
recv4 = ssl_clientSocket.recv(1024)
if recv4[:3] == '235':
	print recv4
	print "Login Successful\n"
else:
	print "Login attempt failed"
	sys.exit()
#/password input

#Sending the MAIL FROM command for a return address
#If it is successful, it will respond with a 250
#If not, it will print an error message and will terminate
mailFrom = 'MAIL From: <sillypirate24@gmail.com>\r\n'
ssl_clientSocket.send(mailFrom)
recv5 = ssl_clientSocket.recv(1024)
if recv5[:3] == '250':
	print recv5
	print "Generating Return Address\n"
else:
	print "Could not read Return Address"
	sys.exit()
#/MAIL FROM command

#Sending the RCPT TO command to give the message a destination
#If it is successful, it will respond with a 250
#If not, it will print an error message and will terminate
rcpt = 'RCPT To: <kaptain06@live.com>\r\n'
ssl_clientSocket.send(rcpt)
recv6 = ssl_clientSocket.recv(1024)
if recv6[:3] == '250':
	print recv6
	print "Generating Receiver Address\n"
else:
	print "Receiving address could not be accepted"
	sys.exit()
#/RCPT TO command

#Sending the DATA command to being filling in the message
#If it is successful, it will respond with a 254
#If not, it will print an error message and will terminate
data = 'DATA\r\n'
ssl_clientSocket.send(data)
recv7 = ssl_clientSocket.recv(1024)
if recv7[:3] == '354':
	print recv7
	print "Sending Message\n"
else:
	print "Error with Message contents"
	sys.exit()
#/DATA command

#Creating and sending the subject line
subject = 'Subject: smtp project\r\n'
ssl_clientSocket.send(subject)

#Creating and sending the message content and ending
message = '\r\n  This is Matthew Collins. I am sending you an email through gmail.com using my smtp.py program. I hope I get an A on this.'
end = '\r\n.\r\n'
ssl_clientSocket.send(message)
ssl_clientSocket.send(end)

#Sending the QUIT command to tell the server the connection is ending
#If it is successful it will respond with a 250
quit = 'QUIT\r\n'
ssl_clientSocket.send(quit)
recv8 = ssl_clientSocket.recv(1024)
print recv8


print "Your message has been sent. Have a great day!"
clientSocket.close() #Closes the socket

###############
# End of File #
###############
