#!/usr/bin/python3

import ldap3

def dump_data(value, connection):
	print("\tDump value: ",value)
	#connection.search( search_base=value, search_filter='(objectclass=*)', search_scope='SUBTREE', attributes='*', get_operational_attributes=True)
	try:
		connection.search(search_base=value, search_filter='(objectclass=*)', search_scope='SUBTREE', attributes='*', get_operational_attributes=True)
		print(connection.entries)
	except:
		pass
	
def list_manually(domain, connection):
	connection.search(domain, '(objectclass=*)')
	for data in connection.entries:
		#data=str(i).split("-")[0].split(":")[1].replace(" ","",1)
		print("\t entry : ",data)

def dump_all(domain, connection):
	connection.search(domain, '(objectclass=*)')
	for i in connection.entries:
		data=str(i).split("-")[0].split(":")[1].replace(" ","",1)
		print("\t entry : ",data)
		dump_data(data, connection)

server = ldap3.Server('192.168.168.122', get_info = ldap3.ALL, port = 389, use_ssl=False)
connection = ldap3.Connection(server)
print("Extablished connection--->")
connection.bind()
if connection.bind():
	print(server.info)
	try:
		domain = str(input())
		list_manually(domain, connection)
		while True:
			print('Select data to dump: \n\t1 List all\n\t2 Dump Entry\n')
			value = int(input())
			print("select value : ", value)
			if value == 1:
				list_manually(domain,connection)
			if value == 2: 
				dump = str(input())
				dump_data(dump, connection)
	except:
		print("Wrong Domain name : ", domain)                
