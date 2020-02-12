import socket
import select
import sys

def get_listening_socket():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    server_socket.listen(2)
    return server_socket


LIMIT = 3
HOST = ''
PORT = 33000

server_socket = get_listening_socket()
sockets_list = [server_socket]
clients = {}

print(f'Listening for connections on {HOST}:{PORT}...')


def receive_message(client_socket):
    try:
        mensagem_header = client_socket.recv(10)

        if not len(mensagem_header):
            return False

        mensagem_length = int(mensagem_header.decode('utf-8').strip())

        return {'header': mensagem_header, 'data': client_socket.recv(mensagem_length)}

    except:
        return False


while True:

    # ler, enviar, erros
    read_sockets, _, exception_sockets = select.select(sockets_list, [], sockets_list)

    for notified_socket in read_sockets:

        if notified_socket == server_socket:
            client_socket, client_address = server_socket.accept()
            user = receive_message(client_socket)
            if user is False:
                continue

            sockets_list.append(client_socket)

            clients[client_socket] = user
            print('Nova conexão aceita de{}:{}, nome: {}'.format(*client_address, user['data'].decode('utf-8')))
        else:

            message = receive_message(notified_socket)
            # Cliente desconectou
            if message is False:
                if (len(sockets_list) <= LIMIT):
                    print('Conexão termiada por: {}'.format(clients[notified_socket]['data'].decode('utf-8')))

                sockets_list.remove(notified_socket)

                del clients[notified_socket]

                continue

            user = clients[notified_socket]

            print(f'Mensagem recebida de: {user["data"].decode("utf-8")}: {message["data"].decode("utf-8")}')

            for client_socket in clients:

                if client_socket != notified_socket:
                    client_socket.send(user['header'] + user['data'] + message['header'] + message['data'])

    for notified_socket in exception_sockets:
        sockets_list.remove(notified_socket)

        del clients[notified_socket]
