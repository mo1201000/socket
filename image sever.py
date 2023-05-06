
import socket
import os , shutil
import time
from PIL import Image
address = 0
m = 0
data = ""
data1 = ''
s = socket.socket()
host_ip = ''
s.bind((host_ip,9998))
s.listen(5)
dirs = os.listdir("Images_here")

while address == 0:
    c , address = s.accept()
time.sleep(0.1)
for file in dirs:
    i = open("Images_here/" + file , "rb")
    for k in i:
        c.send(k)
    print(file + "Sent")
    time.sleep(0.5)#if the images are more in number increase this, it prevents image loss to client
    c.send(b"next")
while True:
    pass