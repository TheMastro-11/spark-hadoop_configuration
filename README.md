# Download
Download the repository on your pc
> \$ wget https://github.com/TheMastro-11/spark-hadoop_configuration 

Unzip file
> \$ tar -xvf spark-hadoop_configuration

# Install
Set public address via script
**disclaimer**: if you not have python3 installed, use
> sudo apt-get install pythonx.x

Otherwise
> python3 ip_set.py

and then
> bash installMaster.sh

## Manual Step
Than you have to indicate the ip addresses of slaves:
> sudo nano /etc/hosts

and you'll find this template (IPMASTER are already updated by the python script):
> IPMASTER namenode <br>
> IPMASTER datanode1 <br>
> IPSLAVE datanode2 <br>

Substituite **IPxxxxx** with the public address of each istance, if you have more than 2 write another line:
> IPSLAVE datanode3 <br>
> IPSLAVE datanodex <br>
> ...

and also update this file:
> sudo nano $HADOOP_CONF_DIF/slaves

Give authorization for **ssh-key**, the last line has to be repeatead for each datanode.
> ssh-keygen -f /home/ubuntu/.ssh/id_rsa -t rsa -P '' #authorization <br>
> cat /home/ubuntu/.ssh/id_rsa.pub  >> /home/ubuntu/.ssh/authorized_keys <br>
> echo datanode1 'cat >> /home/ubuntu/.ssh/authorized_keys '</home/ubuntu/.ssh/id_rsa.pub  <br>







