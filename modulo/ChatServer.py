import socket
import threading
import time

SERVER_IP = ""
PORT = 8080
ADDR = (SERVER_IP, PORT)
FORMATO = 'utf-8'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

conexoes = []
mensagens = []

def enviar_mensagem_ind(conexao):
    print(f"[ENVIANDO] Enviando mensagens para {conexao['addr']}")
    for i in range(conexao['last'], len(mensagens)):
        mensagem_de_envio = 'msg' + mensagens[i]
        conexao['conn'].send(mensagem_de_envio)
        conexao['last'] = i = i
        time.sleep(0.2)

def enviar_mensagem_td():
    global conexoes
    for conexao in conexoes:
        enviar_mensagem_ind(conexao)

def handle_clients(conn, addr):
    print(f'[NOVA CONEXÃO] Novo usuário conectado via end: {addr}')
    global conexoes
    global mensagens
    nome = False

    while True:
        msg = conn.recv(2048).decode(FORMATO)
        if (msg):
            if (msg.startswith("nome=")):
                mensagem_separada = msg.split("=")
                nome = mensagem_separada[1]
                map_conexao = {
                    'conn': conn,
                    'addr': addr,
                    'nome': nome,
                    'last': 0
                }
                conexoes.append(map_conexao)
                enviar_mensagem_ind(map_conexao)

            elif(msg.startswith('msg=')):
                mensagem_separada = msg.split('=')
                mensagem = mensagem_separada[1]
                mensagens.append(mensagem)
                enviar_mensagem_td()

def start():
    print('[INICIANDO] Chat aberto')
    server.listen()
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_clients, args=(conn, addr))  # <------ executando o código em paralelo
        thread.start()

start()