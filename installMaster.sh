#!/bin/sh
#install java
sudo apt-get update && sudo apt-get dist-upgrade
sudo apt-get install openjdk

#install hadoop
sudo mv hadoop /home/ubuntu/hadoop

#update ambient variables
mv .profle  /home/ubuntu/.profile
source /home/ubuntu/.profile

#ssh config
mv config /home/ubuntu/.ssh/config

#template ip & hostname
sudo mv hosts /etc/hosts 

sudo chown -R ubuntu $HADOOP_HOME #permessi

#/////////#
#install spark
sudo mv spark /home/ubuntu/spark