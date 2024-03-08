# Download
Download the repository on your pc
> \$ wget https://github.com/TheMastro-11/spark-hadoop_configuration 

Unzip file
> \$ tar -xvf spark-hadoop_configuration

# Install
> bash install.sh

## Manual Step
substituite NAMENODEADDRESS with the master's public address:
> sudo nano $HADOOP_CONF_DIF/core-site.xml

In the you'll find this template:
> IPMASTER namenode 
> IPMASTER datanode1 
> IPSLAVE datanode2

Substituite **IPMASTER** with the public address of each istance, if you have more than 2 write another line:
> IPSLAVE datanode3
> IPSLAVE datanodex
> ...

and also update this file:
> sudo nano $HADOOP_CONF_DIF/slaves

Give authorization for **ssh-key**, the last line has to be repeatead for each datanode.
> ssh-keygen -f /home/ubuntu/.ssh/id_rsa -t rsa -P '' #authorization
> cat /home/ubuntu/.ssh/id_rsa.pub  >> /home/ubuntu/.ssh/authorized_keys
> echo datanode1 'cat >> /home/ubuntu/.ssh/authorized_keys '</home/ubuntu/.ssh/id_rsa.pub

### Spark
Again substituite NAMENODEADDRESS with the master's public address
> sudo nano spark/conf/spark-env.sh -> insert the HOSTNAMEPUBBLICO manually
> export SPARK_MASTER_HOST="NAMENODEADDRESS" 
> export HADOOP_CONF_DIR="/home/ubuntu/hadoop/conf"






