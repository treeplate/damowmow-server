import sys
sys.path.append('/home/treeplate/lib/python')
from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket
clients = []
users = []
class SimpleChat(WebSocket):

    def handleMessage(self):
       if self.data.startswith("user "):
          users[clients.index(self)] = self.data[5:];
          print self.address[0] + u' is called ' + users[clients.index(self)]
       elif self.data == "request":
          self.sendMessage(", ".join(users))
       for client in clients:
             if self.data.startswith("user "):
                client.sendMessage(self.address[0] + u' is called ' + users[clients.index(self)])
             elif self.data != "request":
                client.sendMessage(users[clients.index(self)] + ' said "' + self.data + '".')
    def handleConnected(self):
       print self.address, 'connected'
       for client in clients:
          client.sendMessage(self.address[0] + u' - connected')
          
       clients.append(self)
       users.append("unnamed")    

    def handleClose(self):
       print(users[clients.index(self)] + '- disconnected')
       for client in clients:
          client.sendMessage(users[clients.index(self)] + '- disconnected')r
       users.remove(users[clients.index(self)])
       clients.remove(self)
       print self.address, 'closed'
       

server = SimpleWebSocketServer('', 8000, SimpleChat)
server.serveforever()
