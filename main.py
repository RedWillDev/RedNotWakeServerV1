import socket
import os

def UDP():
    UDP_IP = "192.168.1.20"
    UDP_PORT = 80
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((UDP_IP, UDP_PORT))
    while True:
        data, addr = sock.recvfrom(1024)
        print("received message: %s" % data)

        if data == b'TurnOff':
            os.system("shutdown /s /t 30")
        elif data == b'TurnON':
            print("test")

def TCP():
    UDP_IP = "192.168.1.20"
    UDP_PORT = 80
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((UDP_IP, UDP_PORT))
    while True:
        data, addr = sock.recvfrom(1024)
        print("received message: %s" % data)

        if data == b'TurnOff':
            os.system("shutdown /s /t 30")
        elif data == b'TurnON':
            print("test")



var = input("? : ")

if var == "UDP" or var == "udp":
    UDP()
elif var == "TCP" or var == "tcp":
    TCP()


