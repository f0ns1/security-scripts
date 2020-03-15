#!/bin/bash


FILE=$1
DICT=$2
OUT="decrypti_bruteforce.txt"

echo  Inis script:
echo  FILE= $FILE
echo  DICT = $DICT
i=0
MAX=100
while read line;
do 
	openssl aes-256-cbc -d -in $FILE -out $OUT -k "friends" 2> /dev/null && echo "Credentials found : $line \n" && cat $OUT && break 
#	i=$((i+1))
#	echo I : $i
#	if [ "$i" == "$MAX" ];
#	then 
#		echo MAX: $MAX
#		MAX=$(($MAX+100))
#		wait
		#break
#	fi	
	
done < $DICT;
