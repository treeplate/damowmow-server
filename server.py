import sys
import traceback
sys.path.append('/home/treeplate/lib/python')
from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket
clients = []

def satisfy(pattern, input):
    marks = [True]
    for x in range(0, len(pattern)-1):
        if pattern[x] == '?':
            marks.append(input[x])
        elif pattern[x] == input[x]:
            b = 'c'
        else:
            marks[0] = False
    return marks
            
            

class SimpleChat(WebSocket):

    def handleMessage(self):
        try:
            print satisfy("???", self.data) + ', message'
        except:
            traceback.print_exc()

    def handleConnected(self):
        try:
            clients.append(self)
            print self.address, 'connected'
        except:
                traceback.print_exc()
    def handleClose(self):
        try:
            clients.remove(self)
            print self.address, 'closed'
        except:
            traceback.print_exc()


server = SimpleWebSocketServer('', 8001, SimpleChat)
server.serveforever()
