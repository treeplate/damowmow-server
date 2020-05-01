import sys
import traceback
sys.path.append('/home/treeplate/lib/python')
from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket
clients = []

def satisfy(list):
    pattern = list[1]
    input = list[2]
    print(list[0] + ": pattern " + pattern + " input " + input);
    marks = [True]
    if len(pattern) == len(input):
        print(len(pattern));
        for x in range(0, len(pattern)):
            print(pattern[x] + input[x]);
            if pattern[x] == '?':
                marks.append(input[x])
            elif pattern[x] == input[x]:
                b = 'c'
            else:
                marks[0] = False
            
        return marks
    return [False]
            
            

class SimpleChat(WebSocket):

    def handleMessage(self):
        try:
            print("recieved " + self.data);
            self.sendMessage(','.join(map(str, satisfy(self.data.split(",")))))
            print('sent ' + ','.join(map(str, satisfy(self.data.split(",")))))
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
