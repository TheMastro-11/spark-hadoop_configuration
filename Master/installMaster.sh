#!/bin/sh
# move file
rm /home/ubuntu/.bashrc
mv spark-hadoop_configuration/Master/* .
mv spark-hadoop_configuration/Master/.[!.]* .
mv spark-hadoop_configuration/startHadoop.sh .
mv spark-hadoop_configuration/stopHadoop.sh .
mv spark-hadoop_configuration/.bashrc .
rm -rf spark-hadoop_configuration/.git
rm -r spark-hadoop_configuration/

# python install
sudo apt-get install python3

# set ip master
python3 ip_set.py

# clear
rm ip_set.py

# install java
sudo apt-get update && sudo apt-get dist-upgrade
sudo apt-get install openjdk-8-jdk

# ssh config
mv config /home/ubuntu/.ssh/config

# template ip & hostname
sudo mv hosts /etc/hosts 

# shh authorization
ssh-keygen -f /home/ubuntu/.ssh/id_rsa -t rsa -P '' #authorization
cat /home/ubuntu/.ssh/id_rsa.pub >> /home/ubuntu/.ssh/authorized_keys

sudo chown -R ubuntu .ssh
