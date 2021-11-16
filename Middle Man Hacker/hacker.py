import socket

d_msg = ""

#AF_INET is a address family our program can communicate only with this family, SOCK_STREAM is telling its a TCP connection
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 

s.connect((socket.gethostname(),567))

message = s.recv(10000) #receive from sender
message = message.decode("utf-8")

print("The enoded message is :" + message)