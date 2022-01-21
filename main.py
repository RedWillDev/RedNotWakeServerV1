import socket
import os


UDP_IP = "192.168.1.20"
UDP_PORT = 28075
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))
while True:
    data, addr = sock.recvfrom(1024)
    print("received message: %s" % data)

    if data == b'TurnOff':
        os.system("shutdown /s /t 30")
    elif data == b'TurnON':
        os.system("shutdown /a")
