import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

addr = input('Dirección del servidor a conectar: ')
server_address = (addr, 4050)
print('Conectando a {} puerto {}'.format(*server_address))
sock.connect(server_address)

try:
    message = input("Nombre de archivo (.bat) a ejecutar en servidor: ")
    print('Enviando {!r}'.format(message))
    sock.sendall(bytes(message, 'utf-8'))

    conf = input("¿Desea ejecutar el archivo en caso de encontrarlo? Y/N: ")
    print('Enviando respuesta a servidor: {!r}'.format(conf))
    sock.sendall(bytes(conf, 'utf-8'))

    amount_received = 0
    amount_expected = len(message)

    while amount_received < amount_expected:
        data = sock.recv(50)
        amount_received += len(data)
        print('Mensaje recibido: ' + data.decode('UTF-8'))

finally:
    print('Cerrando el socket')
    message2 = input("Presione ENTER para salir ")
    sock.close()