# -*- coding: utf-8 -*-
import sys
import socket
import threading
import pyperclip


class ClientDaemon:
    def __init__(self, address):
        self.address = address
        self.text = ""

    def start(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(self.address)
        self._paste_task(s)

    def _paste_task(self, socket):
        # get text from clipboard and send to server daemon
        text = pyperclip.paste()
        if self.text != text:
            print("text:{}".format(text))
            self.text = text
            try:
                socket.sendall(text.encode('utf-8'))
            except:
                socket.close()
                sys.exit(0)
        threading.Timer(2.0, self._paste_task, [socket]).start()


if __name__ == "__main__":
    host = sys.argv[1]
    port = int(sys.argv[2])
    if len(sys.argv) >= 4:
        clipboard = sys.argv[3]
        pyperclip.set_clipboard(clipboard)
    print("host={}, port={}".format(host, port))
    client_daemon = ClientDaemon((host, port))
    client_daemon.start()
