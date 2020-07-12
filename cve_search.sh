#!/bin/bash

if [ $# -eq 1 ]; then

echo "	search CVE: $1"
echo ""
	curl -i "https://cve.circl.lu/api/cve/$1"
elif [ $# -eq 2 ]; then
	echo "CVE list: $2"
	for i in $(echo $2 | tr "," "\n")
	do
  		echo "CVE: $i"
		curl -i "https://cve.circl.lu/api/cve/$i"
	done 

else
	echo "Usage : script.sh CVE-x-x | list CVE1,CV2,CV3...CVEN"
fi;
echo ""
echo "	search Finished"
