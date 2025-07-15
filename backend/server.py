import sqlite3
from assessor import Assessor
from http.server import BaseHTTPRequestHandler, HTTPServer
import json

connection = sqlite3.connect("assessores.db")
cursor = connection.cursor()

class Handler(BaseHTTPRequestHandler):

    def do_POST(self):

        # mensagem vinda do post
        body = self.rfile.read(int(self.headers.get('Content-Length', 0))).decode('utf-8')
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

        self.wfile.write(json.dumps(response_data).encode())

    def do_OPTIONS(self):
        self.send_response(200, "ok")
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header("Access-Control-Allow-Headers", "X-Requested-With")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()


def add_credentials(assessor: Assessor):
    cursor.execute(f"INSERT INTO credenciais VALUES ('{assessor.email}',"
                   f"'{assessor.password}')")
    connection.commit()
    print(assessor.email + " adicionado com sucesso.")

def remove_credentials():
    pass

def edit_credentials():
    pass

def run(server_class=HTTPServer, handler_class=Handler, port=8080):
    server_addres = ('', port)
    httpd = server_class(server_addres, handler_class)
    print(f'starting httpd on port {port}')
    httpd.serve_forever()

def authenticate_credentials(assessor: Assessor):
    pass

def json_to_object(body: str) -> Assessor:
    return Assessor(**json.loads(body))




run()