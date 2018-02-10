import socket

sk = socket.socket()
address = ('127.0.0.1', 8000)

sk.bind(address)
sk.listen(3)

conn, addr = sk.accept()
print(conn)
conn.send(bytes('Hello!', 'utf-8'))
conn.close()
sk.close()


# Client
skClient = socket.socket()
addressServer = ('127.0.0.1', 8000)

skClient.connect(addressServer)
msg = skClient.recv(1024)
print(str(msg, 'utf-8'))

socket.close()   # now client will sent a null date to server, server need to if not msg: conn.close() or try(recommend)
