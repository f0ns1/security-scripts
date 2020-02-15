#/bin/bash

echo init
for i in `seq 1 6553` 
do 
timeout 1 bash -c "echo > /dev/tcp/$1/$i" 2>/dev/null && echo " Open port : $i on Host: 10. $1" &
done; wait


echo end
