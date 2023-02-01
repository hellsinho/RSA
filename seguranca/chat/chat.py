import socket

class chat():
    def __init__(self, host, port):
        self.host = host
        self.port = port
    
    def client(self):
#        host = '127.0.0.1'
#        port = 50000

        socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        socket_client.connect((self.host, self.port))
        socket_client.sendall(str.encode("Mensagem enviada"))

        data = socket_client.recv(1024)

        print("Mensagem ecoada", data.decode())
        
    def server(self):
#        host = 'localhost'
#        port = 50000

        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        server.bind((self.host, self.port))

        server.listen()

        print("Aguardando conexão com o cliente")

        conn, ender = server.accept()

        print("Conectado em", ender)

        while True:
            data = conn.recv(1024)
            if not data:
                print("Encerrando conexão")
                conn.close()
                break
            conn.sendall(data)