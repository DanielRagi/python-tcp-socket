import socket
import sys
import os

# Definicion de socket con listening en todas las direcciones del servidor
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('0.0.0.0', 4050)
print('Iniciando servidor {} puerto {}'.format(*server_address))
sock.bind(server_address)

sock.listen(1)

while True:
    print('Esperando una conexión')
    connection, client_address = sock.accept()
    try:
        print('Conexión desde: ', client_address)
        while True:
            data = connection.recv(50)
            print('Recibido del cliente: {!r}'.format(data))
            conf = connection.recv(50)
            print('Confirmacion de ejecucion del cliente: {!r}'.format(conf))
            if data:
                print('Enviando respuesta al cliente')
                fname = data.decode('UTF-8')+".bat"

                if conf.decode('UTF-8').upper() != 'Y':
                    connection.send("Archivo no ejecutado".encode())
                elif os.system(fname) == 0 and conf.decode('UTF-8').upper() == 'Y':
                    connection.send("Archivo encontrado y ejecutado".encode())
                elif os.system(fname) != 0:
                    connection.send("El archivo no fue encontrado".encode())
                break
            else:
                print('No se recibió información del cliente', client_address)
                break

    finally:	
        connection.close()