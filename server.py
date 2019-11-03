import sys
sys.path.append('/home/treeplate/lib/python')
from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket
clients = []
users = []
class SimpleChat(WebSocket):

    def handleMessage(self):
       if self.data not in users:
             users.append(self.data)
       for client in clients:
             client.sendMessage(users)
             client.sendMessage(self.address[0] + u' - ' + self.data)

    def handleConnected(self):
       print self.address, 'connected'
       self.sendMessage(users);
       for client in clients:
          client.sendMessage(self.address[0] + u' - connected')
          
       clients.append(self)

    def handleClose(self):
       clients.remove(self)
       print self.address, 'closed'
       for client in clients:
          client.sendMessage(self.address[0] + u' - disconnected')

server = SimpleWebSocketServer('', 8000, SimpleChat)
server.serveforever()
