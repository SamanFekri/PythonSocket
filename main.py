__author__ = 'SKings'
from ServerSocket import *

server = ServerSocket("127.0.0.1",7777,"saman")
server.startServer()
exit = input("write exit to exit : ")
while exit != "exit":
    print(exit)
    exit = input("write exit to exit : ")

server.kill_server()