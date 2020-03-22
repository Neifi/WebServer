from http.server import HTTPServer, BaseHTTPRequestHandler
import argparse
from pathlib import Path

class server(BaseHTTPRequestHandler):

    def controller(self):
        
        fking_correct_path = Path("webServer\practica_utf.html")
        file = open(fking_correct_path).read()
        self.send_response(200)
        return file
    
    def _set_headers(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        self.wfile.write(bytes(self.controller(), 'utf-8'))

def run(server_class=HTTPServer, handler_class=server, addr="localhost", port=8000):
    print ("Running server in "+ addr+ "port "+ str(port))
    server_address = (addr, port)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

if __name__ == "__main__":

    run()