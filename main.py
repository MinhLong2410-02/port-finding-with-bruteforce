import socket

def scan_port(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1) 
    try:
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"Port {port} is open on {ip}.")
        sock.close()
    except socket.error as err:
        print(f"Couldn't connect to port {port}: {err}")
    finally:
        sock.close()

def main():
    ip_address = '103.190.38.50'
    for port in range(1, 65536): 
        scan_port(ip_address, port)

main()
