import socket

class connection:

    def __init__(self, sock=None):
        self.port = 8888
        if sock is None:
            self.sock = socket.socket(
                socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock

    def connect(self, host, port):
        self.host = host
        self.port = port
        self.sock.connect((self.host, self.port))

    def sendall(self, msg):
        totalsent = 0
        while totalsent < MSGLEN:
            sent = self.sock.sendall(msg[totalsent:])
            if sent == 0:
                raise RuntimeError("socket connection broken")
            totalsent = totalsent + sent

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
        self.ip = ""
        self.listenForInput()

    def addConnection(self, host, port):
        conn = connection()
        try: 
            conn.connect(host, port)
            self.connections.append(conn)
            return "Bot added at " + host + ":" + port
        except:
            return "Could not connect to bot at " + host + ":" + port
            
 

    def listenForInput(self):
        self.listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.listener.bind(("", 8888))
        self.listener.listen(10)
        while 1:
            #wait to accept a connection - blocking call
            conn, addr = self.listener.accept()
            print 'Connected with ' + addr[0] + ':' + str(addr[1])
            message = conn.recv(1024).strip("\n").split(" ")
            if not message: 
                break
            print(message)
            if message[0] == "addcon":
                output = self.addConnection(message[1], message[2])
                conn.sendall(output)


print("Running \n")
bot = bot()

        
