from http.server import HTTPServer,BaseHTTPRequestHandler

class HelloHTTPRequestHandler(BaseHTTPRequestHandler):
  def do_GET(self):
    self.send_response(200)
    self.send_header('Content-Type','text/html')
    self.end_headers()
    self.wfile.write('Hello World\n'.encode())
    self.wfile.flush()

def run():
  print('Listening on port 8000')
  server_address = ('',8000)
  httpd = HTTPServer(server_address,HelloHTTPRequestHandler)
  httpd.serve_forever()



if __name__ == "__main__":
  run()
