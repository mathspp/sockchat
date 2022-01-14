import selectors
import socket


class ChatServer:
    def __init__(self, host, port):
        """Initialise the server attributes."""
        self._host = host
        self._port = port
        self._socket = None
        self._read_selector = selectors.DefaultSelector()

    def _accept_connection(self, sock):
        """Callback function for when the server is ready to accept a connection."""
        client, _ = sock.accept()
        print("Registering client...")
        self._read_selector.register(client, selectors.EVENT_READ, self._receive_message)

    def _receive_message(self, sock):
        """Callback function for when a client socket is ready to receive."""
        msg = sock.recv(1024)
        print(msg.decode("utf8"))

    def _init_server(self):
        """Initialises the server socket."""

        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.bind((self._host, self._port))
        self._socket.listen()
        # Put the socket in the selector "bag":
        self._read_selector.register(
            self._socket,
            selectors.EVENT_READ,
            self._accept_connection,
        )

    def run(self):
        """Starts the server and accepts connections indefinitely."""

        self._init_server()
        print("Running server...")
        while True:
            for key, _ in self._read_selector.select():
                sock, callback = key.fileobj, key.data
                callback(sock)


if __name__ == "__main__":
    cs = ChatServer("localhost", 7342)
    cs.run()
