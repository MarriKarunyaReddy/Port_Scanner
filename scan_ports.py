import socket
from get_subnet import get_local_ip, get_subnet
from sweep_subnet import ping_host
def is_port_open(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    try:
        result = sock.connect_ex((ip, port))
        sock.close
        return result == 0
    except:
        return False
    
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

    for ip in live_hosts:
        print(f"Scanning ports on {ip}")

        for port in range (1, 101):
            if is_port_open(ip, port):
                print(f"Port {port} is open on {ip}")
