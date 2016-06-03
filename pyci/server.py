#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .responses import fail
import json
import logging
import socketserver


logger = logging.getLogger(__name__)


class PYCIHandler(socketserver.BaseRequestHandler):

    def _dispatch(self, req):
        # for now just return request
        return req

    def respond(self, msg):
        try:
            req = json.loads(msg.decode('utf-8'))
        except ValueError:
            msg = 'Request is not a valid JSON string!'
            logger.error(msg)
            return fail(msg)

        return self._dispatch(req)

    def handle(self):
        chunks = []
        ch = b''
        while b'\n' not in ch:
            ch = self.request.recv(16)
            chunks.append(ch)
        msg = b''.join(chunks)
        self.request.sendall(self.respond(msg))


if __name__ == "__main__":
    host, port = '0.0.0.0', 9999
    server = socketserver.TCPServer((host, port), PYCIHandler)
    server.serve_forever()
