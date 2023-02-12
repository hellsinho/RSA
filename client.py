import socket
from RSA.criptografia import Criptografia

cripto = Criptografia(13, 41)
host = 'localhost'
port = 50000

socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socket_client.connect((host, port))

def exibe():
    print("COMANDOS DO CHAT")
    print("exit - Para encerrar a conexão")
    print("Chave_e - Para ")

((e, n),(d, n)) = cripto.getKeys()
while True:
    socket_client.send(e.encode)
    msg = input("Mensagem: ")
    socket_client.send(msg.encode('utf-8'))
    
    socket_client.send(input("Mensagem: ").encode('utf-8'))
    mensagem = socket_client.recv(1024).decode('utf-8')
    if mensagem.lower() == 'exit':
        print("Conexão encerrada")
        break
    else:
        print(mensagem)
        
socket_client.close()