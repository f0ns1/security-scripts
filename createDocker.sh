#!/bin/bash -x

CONTAINER=$2
TMP_DIR=$1
HACK_PARTITION=$3

mkdir $TMP_DIR && cd $TMP_DIR
echo "Create docker container and use it "

echo "FROM $CONTAINER:18.04

MAINTAINER f0ns1 fonso.gonzalezsan@gmail.com

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && apt-get install -y git net-tools iputils-ping
" > Dockerfile

#build docker container
docker build . -t  $CONTAINER

#show docker active images
docker images 

#run container noninteractive
#docker run -dit --network bridge --name application_$CONTAINER $CONTAINER

#list docker  process
docker ps

#run container non interactive with mount partition with root admin permissio 
docker run -v $HACK_PARTITION:/mnt/ -dit --network bridge --name application_$CONTAINER -t $CONTAINER bash

docker ps 

#launch bash terminal on application (no login) 
docker exec -it application_$CONTAINER bash

####################
# delete all docker process
#####
#sudo docker rm -f `sudo docker ps -a -q`
###############
#delet all docker images
#############
#sudo docker rmi -f `sudo docker images -q`

