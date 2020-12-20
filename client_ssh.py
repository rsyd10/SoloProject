import socket
import sys
from Crypto.Cipher import AES
import paramiko

def encrypt(encryption):
    obj = AES.new(b"a1b2c3d4e5f6g7h8", AES.MODE_CFB,b"a1b2c3d4e5f6g7h8")
    ecpt = obj.encrypt(encryption)
    return ecpt

def decrypt(encryption):
    obj = AES.new(b"a1b2c3d4e5f6g7h8", AES.MODE_CFB,b"a1b2c3d4e5f6g7h8")
    dcpt = obj.decrypt(encryption)
    return dcpt

hostname = "192.168.0.164"
port = "22"
user = "rasyad"
passwd = "rasyad26"

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname, port=port, username=user, password=passwd)

print ("____Welcome to my server!____ ")

servername = "192.168.0.155"
port = 1999
csock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
csock.connect((servername, port))
cmd = input(" Enter command: ")
while cmd!= "exit":
   cmde = encrypt(cmd)
   csock.send(cmde)
   cont = csock.recv(2048)
   snd = decrypt(cont)
   cmd = snd.decode()
   print ( cmd, "\n")
   stdin,stdout,stderr = client.exec_command(cmd)
   print (stdout.read().decode())
   cmd = input("Enter command: ")
   if cmd == "exit":
      break;
csock.close()
client.close()
sys.exit()
