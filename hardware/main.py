from picozero import Servo, Buzzer
from time import sleep

import sys
import struct
import socket
import network

SSID = "Pixel_3443"
PASS = "lycheecalpico"

PW_MIN = 0.0005
PW_MAX = 0.0025



def connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(SSID, PASS)
    
    while not wlan.isconnected():
        print("Waiting for connection...")
        sleep(1)
    
    ip = wlan.ifconfig()[0]
    print(f"Connected on {ip}")
    
    return ip

def open_socket(ip):
    addr = socket.getaddrinfo(ip, 8000)[0][-1]
    sock = socket.socket()
    sock.bind(addr)
    sock.listen()
    return sock

def handle_msg(client):
    typ = client.read(1)[0]

    if typ == 2:
        f1, f2 = struct.unpack("!ff", client.read(8))
        print(f"pos {f1} {f2}")
        
        if f1 < 0 or 1 < f1 or f2 < 0 or 1 < f2:
            print("Invalid position")
            return
        
        sb.value = f1
        su.value = f2
        
    elif typ == 1:
        bz.on()
        print("on")
        
    elif typ == 0:
        bz.off()
        print("off")
        

sb = Servo(16, 0, PW_MIN, PW_MAX)
su = Servo(17, 0, PW_MIN, PW_MAX)
bz = Buzzer(14)

try:    
    ip = connect()
    sock = open_socket(ip)
    
    while True:
        client, _ = sock.accept()
        
        try:
            sb.on(0)
            su.on(0)
            
            while True:
                handle_msg(client)
                
        except Exception as e:
            print(e)
            
        finally:
            client.close()
            sb.off()
            su.off()
        
except Exception as e:
    print(e)

finally:
    sock.close()
    sb.close()
    su.close()