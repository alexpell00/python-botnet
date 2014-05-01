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

    def addConnection(self, host, portaconn = connection()
        conn.connect(host, port)
        self.connections.append(conn)

    def listenForInput(self):


bot = bot()
        
