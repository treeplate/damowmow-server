import sys
import traceback
sys.path.append('/home/treeplate/lib/python')
from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket
clients = []

def satisfy(pattern, input):
    marks = [true]
    for x in range(0, pattern.length-1):
        if pattern[x] == '?':
            marks.append(input[x])
        elif pattern[x] == input[x]:
            b = 'c'
        else:
            marks[0] = false
    return marks
            
            

class SimpleChat(WebSocket):

    def handleMessage(self):
        try:
            print(self, ', message')
        except:
            traceback.print_exc()

    def handleConnected(self):
        try:
            clients.append(self)
            print(self.address, 'connected')
        except:
                traceback.print_exc()
    def handleClose(self):
        try:
            clients.remove(self)
            print(self.address, 'closed')
        except:
            traceback.print_exc()


server = SimpleWebSocketServer('', 8001, SimpleChat)
server.serveforever()
