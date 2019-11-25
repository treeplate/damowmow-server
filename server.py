import sys
import traceback
sys.path.append('/home/treeplate/lib/python')
from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket
clients = []
users = []
class SimpleChat(WebSocket):

    def handleMessage(self):
        try:
            if self.data.startswith("user "):
                users[clients.index(self)] = self.data[5:]
                if("," in users[clients.index(self)]):
                    while "," in users[clients.index(self)]:
                        users[clients.index(
                            self)][users[clients.index(self)].indexOf(",")] = "-"
                print self.address[0] + u' is called ' + users[clients.index(self)]
            elif self.data == "request":
                self.sendMessage("request:" + (",".join(users)))
                print users[clients.index(self)], " has requested."
            for client in clients:
                if self.data.startswith("user "):
                    client.sendMessage(
                        "usernamed:"+self.address[0] + u' is called ' + users[clients.index(self)])
                    # print self.address[0] + u' is called ' + users[clients.index(self)]
                elif self.data != "request":
                    print users[clients.index(self)] + "request" 
                    client.sendMessage(
                        "message:"+users[clients.index(self)] + ' said "' + self.data + '".')
        except:
                traceback.print_exc()

    def handleConnected(self):
        print(self.address, 'connected')
        for client in clients:
            client.sendMessage("connection:"+self.address[0] + u' - connected')

        clients.append(self)
        users.append("unnamed")

    def handleClose(self):
        print(users[clients.index(self)] + '- disconnected')
        for client in clients:
            client.sendMessage(
                "disconnection:"+users[clients.index(self)] + '- disconnected')
        users.remove(users[clients.index(self)])
        clients.remove(self)
        print(self.address, 'closed')


server = SimpleWebSocketServer('', 8001, SimpleChat)
server.serveforever()
