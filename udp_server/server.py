import socket
import threading
import asyncio
import time
import _thread

#SERVER_UDP_IP = "131.159.195.115"
SERVER_UDP_PORT = 5001
SERVER_UDP_IP = "127.0.0.1"


class ServerProtocol:
    def connection_made(self, transport):
        self.transport = transport

    def datagram_received(self, data, addr):
        message = data.decode()
        print('Received %r from %s' % (message, addr))
        
        # needed for echo server
        #print('Send %r to %s' % (message, addr))
        #self.transport.sendto(data, addr)

loop = asyncio.get_event_loop()
print("Starting UDP server")
# One protocol instance will be created to serve all client requests
listen = loop.create_datagram_endpoint(ServerProtocol, local_addr=('127.0.0.1', 5001))
transport, protocol = loop.run_until_complete(listen)

t = threading.Thread(target=loop.run_forever, args=())
t.start()


print("Test")

def send_data():
    UDP_IP = "192.168.2.72"
    UDP_PORT = 5003
    MESSAGE = b"Ehrenmann"

    print("UDP target IP:", UDP_IP)
    print("UDP target port:", UDP_PORT)
    print("message:", MESSAGE)

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
    sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))


#def launch_server():
#    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
#    sock.bind((SERVER_UDP_IP, SERVER_UDP_PORT))
#
#    while True:
#        data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
#        print("received message:", data)

#launch_server()
#

while 1:
    print("Send Data")
    send_data()
    time.sleep(2)
exit(1)