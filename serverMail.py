from http.server import HTTPServer, BaseHTTPRequestHandler
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path

import http.server as serverHand
import os
import pickle
import os.path
import smtplib

import os
try:
    import http.server as server
except ImportError:
    # Handle Python 2.x
    import SimpleHTTPServer as server

class HTTPRequestHandler(server.SimpleHTTPRequestHandler):
    
    def controller(self):

        

        # login
        print("Usuario")
        user = input()
        print("Password")
        password = 'dyzoniannxmgbxus'

        # create mail
        print("[INFO] Generando email")
        msg = MIMEMultipart()

        msg['subject'] = 'Consulta'
        msg['From'] = user
        msg['To'] = 'reytax96@gmail.com'
        
        
        # send mail
        print("[INFO] Enviando email")
        sender = smtplib.SMTP(host='smtp.gmail.com', port=587)
        sender.starttls()
        sender.login(user, password)
        sender.send_message(msg)
        del msg
        sender.quit()
        
        self.send_response(200)
    
    def do_GET(self):
        self.post()

    def post(self):
        
        self.controller()
        filename = os.path.basename("webServer/file.txt")
        
        open(filename, 'wb')
        
        self.send_response(201, 'Created')
        self.end_headers()
        reply_body = 'Saved "%s"\n' % filename
        self.wfile.write(reply_body.encode('utf-8'))

def run(server_class=HTTPServer, handler_class=HTTPRequestHandler, addr="localhost", port=8000):
    print("Running server in " + addr + "port " + str(port))
    server_address = (addr, port)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()


if __name__ == "__main__":
    run()
