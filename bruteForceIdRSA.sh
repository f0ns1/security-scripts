#!/bin/bash

echo init script

#Set input vars 
HOST=$1
ID_RSA=$2
DICT=$3

##Manage threads
counter=0
top=30

##iterate dictionary
while read username; do
	echo $username
	ssh -i $ID_RSA $username@$HOST -oStrictHostKeyChecking=no -tt 2>/dev/null &

	let counter=1
	if [ "${counter}" == "${top}" ];then 
		wait; sleep 0.5
		let top+=30
	fi
done <$DICT
echo end script
