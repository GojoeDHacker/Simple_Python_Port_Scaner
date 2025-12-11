import socket # handle connectivity with the other machines
import sys    #handle command line arguments
from datetime import datetime  #time , how long the scan takes
if len (sys.argv)==2:
	target=socket.gethostbyname(sys.argv[1]) #hostname to ip translation
else: 
	print ("invalid")
	sys.exit ()   #if no ip is provided
#add a banner
print ("_" * 50)
print (f"scanning target: {target}")
print (f"time started: {datetime.now()}")
print ("_" *50)
try: 
# scan ports from 1 to 65535 but 50 to 85 is faster for testing	
	for port in range(50, 85):
		#socket obj, AF_INET for IPv4  , SOCK_STREAM for TCP port
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		#set a default timeout sothat we don't hang if port is closed
		socket.setdefaulttimeout(1)
		#attempt connection, if connect_ex retur 0 then succesful
		result= s.connect_ex((target,port))
		if result== 0:
			print (f"port{port} is open")
		#move to next port by closing
		s.close()
except KeyboardInterrupt:
	print ("\nExiting porgram.")  #ctrl+c
	sys.exit()
except socket.gaierror:
	print ("hostname couldn't be resolved")
	sys.exit()
except socket.error:
	print ("couldn't connet to the server")
	sys.exit()

