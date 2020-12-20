import os
import subprocess
import socket
from Crypto.Cipher import AES

def encrypt(encryption):
    obj = AES.new(b"a1b2c3d4e5f6g7h8", AES.MODE_CFB,b"a1b2c3d4e5f6g7h8")
    ecpt = obj.encrypt(encryption)
    return ecpt

def decrypt(encryption):
    obj = AES.new(b"a1b2c3d4e5f6g7h8", AES.MODE_CFB,b"a1b2c3d4e5f6g7h8")
    dcpt = obj.decrypt(encryption)
    return dcpt

host = "192.168.0.155"
port = 1999
ssocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ssocket.bind((host, port))
ssocket.listen(5)
if True:
   print ("Connection complete.")

while True:
   try:
      consocket,addr = ssocket.accept()
      rec = consocket.recv(2048)
      temp = decrypt(rec)
      cmd = temp.decode()
      while(cmd != "exit" and cmd != ""):
         print (addr, "  ", cmd)
         snd  = encrypt(cmd)
         consocket.send(snd)
         rec = consocket.recv(2048)
         rep = decrypt(rec)
         cmd = rep.decode()
      if (cmd == "exit"):
         print ("broken")
         break
   except:
      print ("Youfailed")
      consocket.close()
ssocket.close()
