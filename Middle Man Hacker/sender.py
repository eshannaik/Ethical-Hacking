import socket

message = input("Enter your message:")
e_msg = ""

#AF_INET is a address family our program can communicate only with this family, SOCK_STREAM is telling its a TCP connection
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #instance of server
s.bind((socket.gethostname(),567))

s.listen(5)

while True:
	clt,add = s.accept() #object and address has been got
	key = "abcdefghijklmnopqrstuvwxyz0123456789 !@#$%^&*" #key
	val = key[::-1]

	e_dict = dict(zip(key,val)) #dictionary of key and val

	for words in message.lower():
		e_msg += e_dict[words]

	clt.send(bytes(e_msg,"utf-8")) # send to sender
