import socket

dec_key = input("Give the size of Encryption Key:") #2 layer of security
d_msg = ""

if len(dec_key) == 45:
	#AF_INET is a address family our program can communicate only with this family, SOCK_STREAM is telling its a TCP connection
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 

	s.connect((socket.gethostname(),567))

	message = s.recv(10000) #receive from sender
	message = message.decode("utf-8")

	val = dec_key[::-1]

	d_dict = dict(zip(val,dec_key))

	for words in message.lower():
		d_msg += d_dict[words] # decoded it with the key

	print(d_msg)

else:
	# print(dec_key_size)
	print("Wrong Key size")