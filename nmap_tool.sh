#!/bin/bash

HOST=$1
echo "Evaluate $HOST"
filter=$(nmap -p- --min-rate=1000 -T4 $HOST  | grep ^[0-9] | cut -d '/' -f 1 | tr '\n' ',' | sed s/,$//)
echo "Open ports $filter"


echo "Scanning services and version .... "
nmap -p$filter -sC -sV $HOST -oN target_nmap
