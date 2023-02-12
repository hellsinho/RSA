import socket

host = 'localhost'
port = 50000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))

server.listen()

print("Aguardando conexão com o cliente")

conn, ender = server.accept()

print("Conectado em", ender)

while True:
    data = conn.recv(1024)
    print(data)
    if not data:
        print("Encerrando conexão")
        conn.close()
        break
    else:
        print(data)
    conn.send((input("Mensagem: ").encode("utf-8")))
              
conn.close()