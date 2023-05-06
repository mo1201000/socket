import socket
import os, shutil , sys
from PIL import ImageTk, Image 
c = socket.socket()
import time
host_ip = '192.168.1.2'
socket.gethostbyname(socket.gethostname())
c.connect((host_ip, 9998))
m = 0
condition = True
i = open((str(m) + ".JPG") , "wb") 
while True:
    l = c.recv(1024)
    if l == b'next':
        c.send(b"data")
        m = m + 1
        i = open((str(m) + ".JPG") , "wb")
        print(str(m) + "received")
    if l != b'next' and l != b'':
        i.write(l)


