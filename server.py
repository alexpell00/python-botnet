import socket

while 1:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("", 8889))
    s.listen(10)
    print("Listening")
    conn, addr = s.accept()
    print 'Connected with ' + addr[0] + ':' + str(addr[1])
    data = conn.recv(1024)
    print(data)
    s.close()
