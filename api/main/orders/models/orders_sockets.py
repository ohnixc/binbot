from socketIO_client import SocketIO, BaseNamespace
import os
import logging

class OrderUpdates(BaseNamespace):
    logging.getLogger('socketIO-client').setLevel(logging.DEBUG)
    logging.basicConfig(filename='socketio.log')

    def __init__(self):
        self.key = os.getenv("BINANCE_KEY")
        self.secret = os.getenv("BINANCE_SECRET")
        self.host = os.getenv("WS_BASE")
        self.port = os.getenv("WS_BASE_PORT")        

    def on_connect(self):
        print("connect")

    def on_disconnect(self):
        print("disconnect")

    def on_reconnect(self):
        print("reconnect")

    def on_executionReport(self, *args):
        print("on_executionReport", args)

    def _start_socket(self):
        headers = {'X-MBX-APIKEY': self.key}
        socketIO = SocketIO(self.host, self.port, headers=headers)
        socketIO.on("connect", self.on_connect)
        # socketIO.on("disconnect", self.on_disconnect)
        # socketIO.on("reconnect", self.on_reconnect)
        return socketIO

    def listen_orders(self):
        socketIO = self._start_socket()
        print('listening to orders')
        # Listen
        socketIO.on("executionReport", self.on_executionReport)
        socketIO.emit("aaa")
        socketIO.wait(seconds=1)
        print("listening to orders")
        return

