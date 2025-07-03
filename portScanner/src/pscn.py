import socket
import sys

#Portscan <IP> <start IP> <end IP>



def scanPorts(ip,port1,port2):

    for port in range(port1,port2+1):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        try:
            s.connect((ip,port))
            print(port)
            
        except (ConnectionRefusedError, socket.timeout):
            pass


def scanallports(ip):
    scanPorts(ip,0,65535)


def ScanPorts():
    if not len(sys.argv) == 2 and not len(sys.argv) == 4:
        print("[USAGE] python pscn.py <IP> (optional) <start ip> <end ip>")
        sys.exit()
    
   
    ip = sys.argv[1]


    if (len(sys.argv) == 2):
        scanallports(ip)
    else:
        port1 = int(sys.argv[2]) 
        port2 = int(sys.argv[3])
       
        if port2<port1:
            print("port must go in ascending order")
            sys.exit()
        scanPorts(ip,port1,port2)


if __name__ == "__main__":
    ScanPorts()
