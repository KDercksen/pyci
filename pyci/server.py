#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socketserver


class PYCIHandler(socketserver.BaseRequestHandler):

    def handle(self):
        chunks = []
        ch = b''
        while b'\n' not in ch:
            ch = self.request.recv(16)
            chunks.append(ch)
        msg = b''.join(chunks)
        self.request.sendall(msg)


if __name__ == "__main__":
    host, port = '0.0.0.0', 9999
    server = socketserver.TCPServer((host, port), PYCIHandler)
    server.serve_forever()
