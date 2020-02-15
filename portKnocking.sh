#!/bin/bash

echo "Init port knoking script with nmap"
PORT_LIST=$2
SERVER=$1
USER=$3
echo server: $SERVER
echo List of ports: $PORT_LIST
status=`nmap -p$PORT_LIST -T5 -v -n $SERVER -r`

echo $status
SSH_OPEN=`echo $status | grep 22 | grep open`

if [ "$SSH_OPEN" != "" ];
then 
	echo ssh conenction to 22
	ssh $USER@$SERVER
fi;

