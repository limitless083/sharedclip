# -*- coding: utf-8 -*-
import socketserver
import sys

import pyperclip


class ServerDaemonHandler(socketserver.BaseRequestHandler):
    def handle(self):
        client_socket = self.request
        print("client {} has connect...".format(self.client_address[0]))

        while True:
            try:
                text = receive_all(client_socket)
            except Exception:
                break
            else:
                if not text:
                    print("client {} has disconnect...".format(self.client_address[0]))
                    break
                print("clipboard text update:{}".format(text))
                # copy text to clipboard
                pyperclip.copy(text)


def receive_all(socket, buffer_size=1024):
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
    if len(sys.argv) >= 3:
        clipboard = sys.argv[2]
        pyperclip.set_clipboard(clipboard)
    print("server start...\nport = {}".format(port))
    server_daemon = socketserver.ThreadingTCPServer(("", port), ServerDaemonHandler)
    server_daemon.serve_forever()