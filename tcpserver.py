# first of all import the socket library
import socket			

# next create a socket object
s = socket.socket()		
print ("Socket successfully created")
f = open('msg_dump.txt','wb')
# reserve a port on your computer in our
# case it is 12345 but it can be anything
port = 8000			
host = '192.168.1.24'
# Next bind to the port
# we have not typed any ip in the ip field
# instead we have inputted an empty string
# this makes the server listen to requests
# coming from other computers on the network
s.bind((host, port))
print ("socket binded to %s" %(port))

# put the socket into listening mode
s.listen(5)	
print ("socket is listening")		

# a forever loop until we interrupt it or
# an error occurs
while True:

    # Establish connection with client.
    c, addr = s.accept()	
    print ('Got connection from', addr )
    recieve = False

    while True:
        # data = c.recv(1024)
        # print(data)
        try:
            while (recieve):
                print(recieve)
                data = c.recv(1024)
                # print("Receiving...",data)
                if(data):
                    print("Receiving...")
                    f.write(data)
                if (not data or "---END OF JOB---" in str(data)):
                    print("cancelled", data)
                    recieve = False
                    f.close()
                    break
            val = input("Enter Command: ")
            if(val):
                c.send(f"{val}\n".encode("UTF-8"))
                recieve = True
                #     recieve = False
                #     break
        except Exception as e:
            print(e)
            # c.close()
        # val = input("Enter Command: ")
        # c.send(f"{val}\n".encode("UTF-8"))
        # break
        # data = c.recv(1024)
        # print(data)
    # send a thank you message to the client. encoding to send byte type.
    # c.send('Thank you for connecting'.encode())
    
    
    # Close the connection with the client
    # c.close()

    # Breaking once connection closed
    # break
