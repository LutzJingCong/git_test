import socket

s = socket.socket()
s.connect(('198.13.54.81', 8899))
s.send('adadad'.encode('utf-8'))
s.close()