#!/usr/bin/env python3

from sense_hat import SenseHat
import socket

def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("1.1.1.1", 80))
    try:
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

if __name__ == '__main__':
    while True:
         try:
             main()
             break
         except OSError:
             continue
