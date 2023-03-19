import socket

HOST = '127.0.0.1'  # Локальный адрес
PORT = 8080        # Произвольный порт (не занят по умолчанию)

# Создаем сокет
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Привязываем сокет к адресу и порту
    s.bind((HOST, PORT))
    # Слушаем входящие соединения
    s.listen()
    # Ожидаем подключения клиента
    conn, addr = s.accept()
    with conn:
        print('Соединение установлено с адресом', addr)
        # Цикл обмена данными
        while True:
            # Получаем данные от клиента
            data = conn.recv(1024)
            if not data:
                break
            print('Получено:', data.decode())
            # Отправляем данные обратно клиенту
            conn.sendall(data)

