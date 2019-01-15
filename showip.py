#!/usr/bin/env python3

from sense_hat import SenseHat
import socket

def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect("192.255.255.255", 1)
        ip = s.getsockname()[0]
    except:
        ip = "127.0.0.1"
    finally:
        s.close()
    return ip

def main():
    sense = SenseHat()
    ip = get_local_ip()
    for _ in range(10):
        sense.show_message(ip, scroll_speed=0.2)
