#!/usr/bin/python3
import json
from http.server import BaseHTTPRequestHandler, HTTPServer


class SimpleAPIHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        if self.path == '/':
            response = {"message": "Hello, this is a simple API!"}
        elif self.path == '/data':
            response = {"name": "John", "age": 30, "city": "New York"}
        elif self.path == '/status':
            response = {"status": "OK"}
        else:
            self.send_response(404)
            self.wfile.write(b"Endpoint not found")

        self.wfile.write(json.dumps(response).encode('utf-8'))


def run(server_class=HTTPServer, handler_class=SimpleAPIHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting server on port {port}...")
    httpd.serve_forever()


if __name__ == "__main__":
    run()
