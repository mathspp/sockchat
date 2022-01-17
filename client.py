import socket


class ChatClient:
    def __init__(self, host, port):
        self._host = host
        self._port = port
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        self._socket.connect((self._host, self._port))
        while True:
            msg = input(">>> ")
            self._socket.send(msg.encode("utf8"))


if __name__ == "__main__":
    client = ChatClient("localhost", 7342)
    client.connect()
