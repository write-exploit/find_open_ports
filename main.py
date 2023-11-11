import socket
import threading

def port_scanner(ip,port):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(3)
    try:
        s.connect((ip,port))
        print(port,": open")
    except:
        pass
    s.close()

def main():
    target_ip = "192.168.1.42" #change this
    for target_port in range(65535):
        başla = threading.Thread(target=port_scanner,args=(target_ip,target_port))
        başla.start()

if __name__ == "__main__":
    main()
