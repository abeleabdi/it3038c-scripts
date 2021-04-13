import socket

host = ["www.uc.edu", "www.google.com", "www.bing.com"]

print('Working from host: ' + socket.getfqdn())
for h in host:
    print(h + ': ' + socket.gethostbyname(h))
