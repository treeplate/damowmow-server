import sys
import traceback
sys.path.append('/home/treeplate/lib/python')
from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket
clients = []
info = []
class SimpleChat(WebSocket):

    def handleMessage(self):
        try:
            if self.data.startswith("user "):
                userinfo = self.data[5:].split(" ")
                if(userinfo[0] in info):
                    if(userinfo[1] == info[clients.index(self)][1]):
                        info[clients.index(self)][2] = True
                    else:
                        self.sendMessage("incorrect password")
                        info[clients.index(self)][2] = False
                else:
                    info[clients.index(self)][0] = userinfo[0]
                    info[clients.index(self)][1] = userinfo[1]
                    info[clients.index(self)][2] = True
                    
                    print self.address[0] + u' is called ' + info[clients.index(self)][0]
            elif self.data == "request":
                users = []
                for user in info:
                       users.append(user[0])
                self.sendMessage("request:" + (",".join(users)))
                print info[clients.index(self)][0], " has requested."
            for client in clients:
                if self.data.startswith("user "):
                    client.sendMessage("usernamed:"+self.address[0] + u' is called ' + info[clients.index(self)][0])
                elif self.data != "request":
                    if(info[clients.index(self)][2] == True):
                        client.sendMessage("message:"+info[clients.index(self)][0] + ' said "' + self.data + '".')
                    
        except:
                traceback.print_exc()

    def handleConnected(self):
        try:
            print(self.address, 'connected')
            for client in clients:
                client.sendMessage("connection:"+self.address[0] + u' - connected')
            if(self in clients):
                print info[clients.index(self)][0] + " connected"     
            else:
                clients.append(self)
                info.append(["unnamed", "", False])
        except:
                traceback.print_exc()
    def handleClose(self):
        print(users[clients.index(self)] + '- disconnected')
        for client in clients:
            client.sendMessage("disconnection:"+users[clients.index(self)] + '- disconnected')
        info[clients.index(self)][2] == False
        print(self.address, 'closed')


server = SimpleWebSocketServer('', 8001, SimpleChat)
server.serveforever()
