import socket

HOST = '127.0.0.1'  # Локальный адрес
PORT = 8080        # Произвольный порт (не занят по умолчанию)

# Создаем сокет
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Устанавливаем соединение с сервером
    s.connect((HOST, PORT))
    # Цикл обмена данными
    while True:
        # Отправляем данные серверу
        message = input('Введите сообщение: ')
        s.sendall(message.encode())
        # Получаем данные от сервера
        data = s.recv(1024)
        print('Получено:', data.decode())

