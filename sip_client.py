
import socket

R_IP = '192.168.2.1'
R_PORT = 5060 

message = 'INVITE sip:user1110000000350@.com SIP/2.0 To: <sip:user4110000000350@whatever.com>\x0d\x0aFrom: sip:user9990000000000@rider.com;tag=R400_BAD_REQUEST;taag=4488.1908442942.0\x0d\x0aP-Served-User: sip:user4110000000350@whatever.com\x0d\x0aCall-ID: 00000000-00001188-71C0873E-0@10.44.40.47\x0d\x0aCSeq: 1 INVITE\x0d\x0aContact: sip:user9990000000000@rider.com\x0d\x0aMax-Forwards: 70\x0d\x0aVia: SIP/2.0/TCP 10.44.40.47;branch=z9hG4bK1908442942.4488.0\x0d\x0aContent-Length: 10\x0d\x0a\x0d\x0aRandomText'

def sendPacket():
   #proto = socket.getprotobyname('tcp')                         
   s = socket.socket() 

   try:
       s.connect((R_IP , R_PORT)) 
       print ("Connected to server")
       s.sendall(message)   
       print ("SIP request sent to server")                                    
   except socket.error:
       pass
   finally:
       s.close()

sendPacket()