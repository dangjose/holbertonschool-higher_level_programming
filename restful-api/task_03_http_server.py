#!/usr/bin/python3
"""Task 3. Develop a simple API using Python with the `http.server` module"""

from http.server import HTTPServer, BaseHTTPRequestHandler
import json


class NeuralHTTP(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == '/':
            self.send_response(200)

            self.send_header('Content-type', 'text/plain')
            self.end_headers()

            self.wfile.write(b"Hello, this is a simple API!")
        elif self.path == '/data':
            dataset = {"name": "John", "age": 30, "city": "New York"}

            json_data = json.dumps(dataset)

            self.send_response(200)

            self.send_header('Content-type', 'application/json')
            self.end_headers()

            self.wfile.write(json_data.encode('utf-8'))
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Endpoint not found")


server_address = ('', 8000)
server = HTTPServer(server_address, NeuralHTTP)

server.serve_forever()
server.server_close()
