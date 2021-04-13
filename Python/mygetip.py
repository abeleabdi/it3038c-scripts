import socket, sys

def gethostbynameIP(h):
    try:
        hostname = str(h)
        ip = socket.gethostbyname(hostname)
        print(hostname + ' has an IP of ' + ip)
    except:
        print("Oops, something is wrong with your host")

gethostbynameIP(sys.argv[1])