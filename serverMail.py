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

    def sendEmail(self):

        # login
        user = 'mi_gmail'
        password = 'mi_appkey_de_google'

        # create mail
        print("[INFO] Generando email")
        msg = MIMEMultipart()

        #get ip
        ip = str(self.client_address).split("'")[1]

        msg['subject'] = "Nueva conexión"
        msg['From'] = user
        msg['To'] = 'reytax96@gmail.com'
        msg.attach(MIMEText("Nueva conexión desde la dirección ip: "+ip, 'plain'))

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
        self.load()
        self.sendEmail()

    def load(self):
        filename = os.path.basename("webServer/file.txt")
        open(filename, 'wb')
        self.send_response(201, 'Created')
        self.end_headers()


def run(server_class=HTTPServer, handler_class=HTTPRequestHandler, addr="localhost", port=8000):
    print("Running server in " + addr + "port " + str(port))
    server_address = (addr, port)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()


if __name__ == "__main__":
    run()
