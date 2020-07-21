import asyncore
import time

class Handler(asyncore.dispatcher_with_send):
    def handle_read(self):
        data = self.recv(8196)
        if data:
            self.send(data)

    def handle_write(self):
        sent = self.send(self.buffer)
        self.buffer = self.buffer[sent:]

    def handle_accepted(self, sock, addr):
        print('accepted')


class Server(asyncore.dispatcher):
    def __init__(self, host, port):
        asyncore.dispatcher.__init__(self)
        self.buffer = bytes("hey hey\r\n", 'ascii')
        self.create_socket()
        self.set_reuse_addr()
        self.bind((host, port))
        self.listen(5)

    def handle_accepted(self, sock, addr):
        print(f'incomming {repr(addr)}')
        handler = Handler(sock)


server = Server('127.0.0.1', 1024)
asyncore.loop()
