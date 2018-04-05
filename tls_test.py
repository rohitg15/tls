import sys
import socket
import struct

if __name__ == "__main__":
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_IP)
    port = 443

    # construct test payload
    payload = struct.pack('>B', 0x16)
    payload += struct.pack('>H', 0x0303)
    payload += struct.pack('>H', 0x4)
    payload += struct.pack('>I', 0xDEADBEEF)

    try:
        host = socket.gethostbyname('www.google.com')
        s.connect((host, port))
        res = s.send(payload)
        print (host)
        print (res)

    except:
        print ("Error: ", sys.exc_info())

    s.close()