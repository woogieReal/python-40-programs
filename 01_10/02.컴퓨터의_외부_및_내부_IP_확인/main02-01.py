import socket

print(socket.gethostname());
# -> A66411-002.local

print(socket.gethostbyname(socket.gethostname()));
# -> 127.0.0.1

in_addr = socket.gethostbyname(socket.gethostname());

