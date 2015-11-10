__author__ = 'SKings'

import socket

class ServerSocket:

    ServersCount = 0
    def __init__(self, ip, port, name=None):
        self.name = name
        self.ip = ip
        self.port = port
        ServerSocket.ServersCount += 1

    def startServer(self):
        self.live = True
        self.s = socket.socket()
        self.s.bind((self.ip , self.port))

        print("server ", self.name , " listening")

        self.s.listen(1)
        while(self.live):
            try:
                connection ,client_address = self.s.accept()
                try:
                    print("connect to ", client_address)
                    data = ""
                    while True:
                        data_segment = connection.recv(1024)
                        data = data + data_segment
                        if data_segment:
                            print("continue")
                        else:
                            break
                    print("get this " , data ," from ",client_address)
                    connection.send(data)
                finally:
                    #close connection after get datas
                    connection.close();
            except:
                print("connection error")

    def kill_server(self):
        self.live =False
        self.s.close()

    def ip_port(self,ip=None,port=None):
        if ip is not None:
            self.ip = ip
        if port is not None:
            self.port = port
        return (self.ip , self.port)