import sys
sys.path.append('/home/treeplate/lib/python')
from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket
clients = []
users = []
class SimpleChat(WebSocket):

    def handleMessage(self):
       #if self.data not in users:
             #users.append(self.data)
       for client in clients:
             #client.sendMessage(users)
             if self.data.startswith("user "):
                users[clients.index(self)] = self.data[5:];
                print self.address[0] + u' is called ' + users[clients.index(self)]
                client.sendMessage(self.address[0] + u' is called ' + users[clients.index(self)])
             elif self.data == "request":
                self.sendMessage(", ".join(users))
             else:
                client.sendMessage(users[clients.index(self)] + ' said "' + self.data + '".')
    def handleConnected(self):
       print self.address, 'connected'
       #self.sendMessage(users);
       for client in clients:
          client.sendMessage(self.address[0] + u' - connected')
          
       clients.append(self)
       users.append("unnamed")    

    def handleClose(self):
       clients.remove(self)
       users.remove(users[clients.index(self)])
       print self.address, 'closed'
       for client in clients:
          client.sendMessage(users[clients.index(self)] + '- disconnected')
       print(users[clients.index(self)] + '- disconnected')

server = SimpleWebSocketServer('', 8000, SimpleChat)
server.serveforever()
