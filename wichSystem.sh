#!/bin/bash

COMMAND=`ping -c 1 $1`
TTL=`echo $COMMAND | awk -F"ttl=" '{print $2}' |awk -F " " '{print $1}'`
echo System ttl = $TTL
if [ $TTL -le 120 ]
then 
	SYSTEM="linux"
elif [ $TTL -le 250 ]
then
	SYSTEM="windows"
elif [ $TTL -ge 250 ]
then 
	SYSTEM="IOS" 
fi;

echo system detected: $SYSTEM
