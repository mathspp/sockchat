import socket


class ChatServer:
    def __init__(self, host, port):
        """Initialise the server attributes."""
        self._host = host
        self._port = port
        self._socket = None

    def _init_server(self):
        """Initialises the server socket."""
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.bind((self._host, self._port))
        self._socket.listen()

    def run(self):
        """Starts the server and accepts connections indefinitely."""
        self._init_server()
        while True:
            client, _ = self._socket.accept()
            print("Connection accepted.")


if __name__ == "__main__":
    cs = ChatServer("localhost", 7342)
    cs.run()
