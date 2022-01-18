import time
import threading
import selectors
import socket


class ChatClient:
    def __init__(self, host, port):
        self._host = host
        self._port = port
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._read_selector = selectors.DefaultSelector()

    def _input_and_send_loop(self):
        while True:
            msg = input()
            self._socket.send(msg.encode("utf8"))

    def connect(self):
        self._socket.connect((self._host, self._port))
        threading.Thread(target=self._input_and_send_loop).start()
        while True:
            msg = self._socket.recv(1024).decode("utf8")
            print(" < " + msg)


if __name__ == "__main__":
    client = ChatClient("localhost", 7342)
    client.connect()
