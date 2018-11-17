import socket
import threading
import asyncio
import time
import _thread

#SERVER_UDP_IP = "131.159.195.115"
SERVER_UDP_PORT = 5001
SERVER_UDP_IP = "127.0.0.1"


class ServerProtocol:
    def __init__(self):
        self.__callback = None

    def connection_made(self, transport):
        self.transport = transport

    def datagram_received(self, data, addr):
        print(data)
        message = data.decode()
        print('Received %r from %s' % (message, addr))
        if self.__callback:
            self.__callback(message)

    def set_callback(self, callback):
        self.__callback = callback
        
        # needed for echo server
        #print('Send %r to %s' % (message, addr))
        #self.transport.sendto(data, addr)

class Server:
    def __init__(self, ip, port, callback):
        self.__loop = asyncio.get_event_loop()
        listen = self.__loop.create_datagram_endpoint(ServerProtocol, local_addr=(ip, port))
        transport, protocol = self.__loop.run_until_complete(listen)
        protocol.set_callback(callback)

        self.__server_thread = threading.Thread(
            target=self.__loop.run_forever, args=()
        )
        print("Starting UDP server")
        self.__server_thread.start()

class Client:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def send_data(self, message):
        print("message:", message)

        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
        sock.sendto(message.encode(), (self.ip, self.port))

#while 1:
#    print("Send Data")
#    send_data()
#    time.sleep(2)
#exit(1)
