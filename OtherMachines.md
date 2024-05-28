# Alternative Configuration
If you are installing on a machine other than AWS, follow these instructions alongside the main instructions

## Download and Install && SSH
The script has set */home/ubuntu/* as the home directory, if this is different in your case, change it.

At the request **public master dns**:
* in the case of the master, enter the private ip
* for the slave, enter the word *namenode*

Change the *.config* file on master istance by setting **hostename** to the same *VALUE* as the **host**:
```
Host <VALUE>
    HostName name<VALUE>
    User ubuntu
    IdentityFile /home/ubuntu/.ssh/my-key.pem
```

Next, edit the */etc/hosts* file in **each instance** by adding the public IP addresses to the relevant aliases.
```
127.0.0.1 localhost
PUBLIC_IP namenode
PUBLIC_IP datanode1
PUBLIC_IP datanode2
# The following lines are desirable for IPv6 capable hosts
::1 ip6-localhost ip6-loopback
...
```

If the IP is dynamic, it will need to be changed at each reboot, otherwise it is not necessary.

