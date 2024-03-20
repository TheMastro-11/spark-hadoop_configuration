ip = input("Enter the master's public IP address: ")


def core_site(ip_):
    # Reading the data inside the xml
    # file to a variable under the name 
    # data
    with open('core-site.xml', 'r') as f:
        data = f.read()

    data = data.replace("PUBLICADDRESS", ip_)

    with open("core-site.xml", "wb") as f1:
        f1.write(data.encode())
        
def etc_hosts(ip_):
    with open('hosts', 'r') as f:
        data = f.read()
    
    data = data.replace("IPMASTER", ip_)
    
    with open("hosts", "wb") as f1:
        f1.write(data.encode())

def spark_env(ip_):
    with open('spark-env.sh', 'r') as f:
        data = f.read()
    
    data = data.replace("PUBLICADDRESS", ip_)
    
    with open("spark-env.sh", "wb") as f1:
        f1.write(data.encode())

core_site(ip)
etc_hosts(ip)
spark_env(ip)

