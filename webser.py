from http.server import BaseHTTPRequestHandler, HTTPServer
import socketserver

class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        self.wfile.write("<html><body><h1>hi!</h1></body></html>")

    def do_HEAD(self):
        self._set_headers()

    def do_POST(self):
        # Doesn't do anything with posted data
        self._set_headers()
        self.wfile.write("<html><body><h1>POST!</h1></body></html>")
def run(server_class=HTTPServer, handler_class=S, port=8005):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print('STarting httpd...')
    httpd.serve_forever()

if __name__ == "__main__":
       run()
