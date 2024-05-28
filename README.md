# Before Start
* This installation is for a native AWS machine running ubuntu.  
* Static public IP and DNS are used. An ELASTIC IP is required. (Fee may applied)
* It is possible to use this guide on other machines, also if they have dinamic IPs, but [some precautions](OtherMachines.md) must be taken during the installation.

Thanks to sedaatalay for the [original guide](https://github.com/sedaatalay/How-to-Setup-Hadoop-Single-Node-Cluster-on-AWS-EC2)

# Download and Install
Clone the repo:
> \$ git clone https://github.com/TheMastro-11/spark-hadoop_configuration.git

select the line of code according to your needs:
> \$ sudo bash spark-hadoop_configuration/Master/installMaster.sh

or:
> \$ sudo bash spark-hadoop_configuration/Slave/installSlave.sh

update ambient variables:
> \$ source /home/ubuntu/.bashrc

Give permission:
> \$ sudo chown -R ubuntu $HADOOP_HOME 

delete installation file:
> \$ rm installMaster.sh

or
> \$ rm installSlave.sh

## SSH (Master)
First from your local pc transfer the \[name].pem key to remote istance
> \$ scp path/to/\[name].pem ubuntu@\[dns]:/home/ubuntu/.ssh

Then from istance:
> \$ mv /home/ubuntu/.ssh/[name].pem  /home/ubuntu/.ssh/my-key.pem

### FOR EACH NEW DATANODE ADDED:
You have to configure the ssh connection:
> \$ nano /home/ubuntu/.ssh/config

Must be like this: 
```
Host namenode
    HostName <publicdns>
    User ubuntu
    IdentityFile /home/ubuntu/.ssh/my-key.pem

Host datanode1
    HostName <publicdns>
    User ubuntu
    IdentityFile /home/ubuntu/.ssh/my-key.pem

Host datanode2
    HostName <publicdns>
    User ubuntu
    IdentityFile /home/ubuntu/.ssh/my-key.pem
```

update this file:
> \$ sudo nano $HADOOP_CONF_DIR/slaves

Transfer the rsa key to the slave.
> \$ ssh datanode2 'cat >> /home/ubuntu/.ssh/authorized_keys '</home/ubuntu/.ssh/id_rsa.pub  <br>

Run these commands to reset the configurations before starting the cluster with new data nodes.

> \$ bash resetHadoop.sh

On slaves:
> \$ sudo rm -rf $HADOOP_HOME/data/hdfs/*

# START
## Hadoop
**USE THIS COMMANDS FROM MASTER**
To start Hadoop the first time is necessary to format the namenode:
> \$ hdfs namenode -format 

Then simply run this script, even on subsequent reboots:
> \$ bash startHadoop.sh 

to check if all is start correctly just do this:
> \$  hdfs dfsadmin -report

and you will see how many datanodes are online

To stop:
> \$ bash stopHadoop.sh

## Spark
To start spark launch this from Master:
> \$ ./spark/sbin/start-master.sh

If it has started up correctly, you can view the web UI at *IPMASTERPUBLIC*:8080

Then use this command to start workers (replace ADDRESS with the *spark://privateaddress:7070* you will find in the web page above):
> \$ ./spark/sbin/start-slave.sh ADDRESS

To start a process use this (change ADDRESS with the same above and PATHFILE with the file you wanna run):
> \$ ./spark/bin/spark-submit --master ADDRESS PATHFILE

*WARNING* <br>
Python file are not supported in cluster mode, so only master local cores will run. <br>
For more information about spark-submit visit the [Official Documentation](https://spark.apache.org/docs/latest/submitting-applications.html)
