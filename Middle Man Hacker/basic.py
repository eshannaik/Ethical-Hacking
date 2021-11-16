### Basic encoder and decoder code

message = input("Enter your message:")
e_msg = ""
d_msg = ""

key = "abcdefghijklmnopqrstuvwxyz0123456789 " #key
val = key[::-1] #val

e_dict = dict(zip(key,val)) 

for words in message.lower():
	e_msg += e_dict[words] #encoding the input

print(e_msg) 

d_dict = dict(zip(val,key))

for words in e_msg.lower():
	d_msg += d_dict[words] #decoding the encoded input

print(d_msg)
