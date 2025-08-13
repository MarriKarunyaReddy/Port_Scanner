import subprocess  #module to run system commands
import platform    #module to detect host os
from get_subnet import get_local_ip, get_subnet
from pythonping import ping

def ping_host(host):
    response = ping(host, count= 1, timeout= 1)
    return response.success()


if __name__ == "__main__":
    local_ip = get_local_ip()
    print("Local IP: ",local_ip)

    subnet = get_subnet(local_ip)
    print("Subnet: ", subnet)

    live_hosts= []
    for i in range(1,255):
        ip = subnet + str(i)
        if ping_host(ip):
            print(f"{ip} is alive")
            live_hosts.append(ip)
    
    print("Live Hosts: ", live_hosts)