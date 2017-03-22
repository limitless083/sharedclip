# -*- coding: utf-8 -*-
import sys
from socketserver import BaseRequestHandler, ThreadingTCPServer

import pyperclip


class ServerDaemonHandler(BaseRequestHandler):
    def handle(self):
        client_socket = self.request
        print("client {} has connect...".format(self.client_address[0]))
        self._copy_task(client_socket)

    def _copy_task(self, socket):
        while True:
            try:
                text = self._receive_all(socket)
            except Exception:
                break
            else:
                if not text:
                    print("client {} has disconnect...".format(self.client_address[0]))
                    break
                print("clipboard text update:{}".format(text))
                # copy text to clipboard
                pyperclip.copy(text)

    def _receive_all(self, socket, buffer_size=1024):
        data = []
        buf = socket.recv(buffer_size)
        # if server has receive some data,
        # then set receive timeout to get all text from client in timeout
        socket.settimeout(0.5)
        while buf:
            data.append(buf)
            try:
                buf = socket.recv(buffer_size)
            except:
                # clear timeout
                socket.settimeout(None)
                break

        return b"".join(data).decode("utf-8")


if __name__ == "__main__":
    port = int(sys.argv[1])
    print("server start...\nport = {}".format(port))
    if len(sys.argv) >= 3:
        clipboard = sys.argv[2]
        pyperclip.set_clipboard(clipboard)

    server_daemon = ThreadingTCPServer(("", port), ServerDaemonHandler)
    server_daemon.serve_forever()