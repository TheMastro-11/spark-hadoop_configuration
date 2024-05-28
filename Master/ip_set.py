import socket
import urllib.request

ip_public = urllib.request.urlopen('https://ident.me').read().decode('utf8')
public_dns = input("Enter the master's public dns:\n")
hostname = socket.gethostname()
ip_private = socket.gethostbyname(hostname)


def core_site(dns):
    # Reading the data inside the xml
    # file to a variable under the name 
    # data
    with open('hadoop/etc/hadoop/core-site.xml', 'r') as f:
        data = f.read()

    data = data.replace("PUBLICDNS", dns)

    with open("hadoop/etc/hadoop/core-site.xml", "wb") as f1:
        f1.write(data.encode())
        
def yarn_site(dns):
    with open('hadoop/etc/hadoop/yarn-site.xml', 'r') as f:
        data = f.read()

    data = data.replace("PUBLICDNS", dns)

    with open("hadoop/etc/hadoop/yarn-site.xml", "wb") as f1:
        f1.write(data.encode())

def mapred_site(dns):
    with open('hadoop/etc/hadoop/mapred-site.xml', 'r') as f:
        data = f.read()

    data = data.replace("PUBLICDNS", dns)

    with open("hadoop/etc/hadoop/mapred-site.xml", "wb") as f1:
        f1.write(data.encode())

def config(dns):
    with open('config', 'r') as f:
        data = f.read()

    data = data.replace("PUBLICDNS", dns)

    with open("config", "wb") as f1:
        f1.write(data.encode())
    

def etc_hosts(ip_):
    with open('hosts', 'r') as f:
        data = f.read()
    
    data = data.replace("IPMASTER", ip_)
    
    with open("hosts", "wb") as f1:
        f1.write(data.encode())

def spark_env(ip_):
    with open('spark/conf/spark-env.sh', 'r') as f:
        data = f.read()
    
    data = data.replace("PRIVATEADDRESS", ip_)
    
    with open("spark/conf/spark-env.sh", "wb") as f1:
        f1.write(data.encode())

core_site(public_dns)
yarn_site(public_dns)
mapred_site(public_dns)
config(public_dns)

etc_hosts(ip_public)
spark_env(ip_private)