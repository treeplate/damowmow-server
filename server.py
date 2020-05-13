import sys
import traceback
sys.path.append('/home/treeplate/lib/python')
from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket
clients = []
data = {}
def satisfy(list):
    if len(list) > 2:
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
    else:
        spaces = list[0].split(" ")
        if(spaces[0] == "store"):
           data[spaces[1]] = spaces[2]
           return ["AC"]
        if(spaces[0] == "get"):
           if spaces[1] in data:
             return [data[spaces[1]]]
           return null
        
            

class SimpleChat(WebSocket):

    def handleMessage(self):
        try:
            print("recieved " + self.data);
            message = ','.join(map(str, satisfy(self.data.split(","))))
            self.sendMessage(message)
            print('sent ' + message)
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
