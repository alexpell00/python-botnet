import socket, random, string
from threading import Thread

global bot
global botid

class connection:

    def __init__(self, sock=None):
        pass
        
    def connect(self, host, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = host
        self.port = port
        self.sock.connect((self.host, int(self.port)))
        message = "0~"+toolbox().getid()+"~"+toolbox().getLocalIP()
        self.sock.sendall(message)
        while 1:
            message = self.sock.recv(4096)
            if message != " ":
                print("Message: " + message)
                self.sock.close()
                break
                                  
    def sendall(self, msg):
        self.sock.sendall(msg[totalsent:])
            
    def receive(self):
        msg = ''
        while len(msg) < MSGLEN:
            chunk = self.sock.recv(MSGLEN-len(msg))
            if chunk == '':
                raise RuntimeError("socket connection broken")
            msg = msg + chunk
        return msg
    
class bot:
    
    def __init__(self):
        self.connections = []
        self.ip = toolbox().getLocalIP()
        self.id = toolbox().idGenerator(toolbox().strGenerator(20), self.ip)
        global botid
        botid = self.id
        print("Inializing with id: " + self.id)
        Thread(target = self.listenForUser).start()
        Thread(target = self.listener).start()
        
    def addConnection(self, host,port=8889):
        conn = connection()
        try:
            conn.connect(host, port)
            self.connections.append(conn)
            return "Bot added at " + host + ":" + port
        except:
            return "Could not connect to bot at " + host + ":" + port
    def listener(self):
        self.listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        port = 8889
        self.listener.bind(("", port))
        self.listener.listen(10)
        print("Listening for bot input on port " + str(port))
        while 1:
            conn, addr = self.listener.accept()           
            message = conn.recv(1024).strip("\n").split("~")
            
            
        
    def listenForUser(self):
        self.uListener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        port = 8888
        self.uListener.bind(("", port))
        self.uListener.listen(10)
        print("Listening for user input on port " + str(port))
        while 1:
            #wait to accept a connection - blocking call
            conn, addr = self.listener.accept()
            #print 'Connected with ' + addr[0] + ':' + str(addr[1])
            message = conn.recv(1024).strip("\n").split(" ")
            if not message: 
                break
            if message[0] == "addcon":
                if len(message) == 2:
                    output = self.addConnection(message[1])
                else:
                    output = self.addConnection(message[1], message[2])
                conn.sendall(output)
                print(output + "\n")
    

class toolbox:
    def __init__(self):
        pass
    def strGenerator(self,size=6, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))
    def getLocalIP(self):
        return socket.gethostbyname(socket.gethostname())
    def idGenerator(self,hashcode , ip):
        hashls = list(hashcode)
        ipls = list("".join(ip.split(".")))
        result = [item for sublist in zip(hashls,ipls) for item in sublist]
        return "".join(result)
    def getid(self):
        global bot
        return bot.id
   
def main():
    global bot
    bot = bot()


main()
