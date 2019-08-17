import socket

s = socket.socket()
s.bind(('127.0.0.1', '8899'))
s.listen()

while True:
    print('连接成功')
    c = s.accept()
    print(c.recv(1024))