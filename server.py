from http.server import BaseHTTPRequestHandler
import redis

r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

class Server(BaseHTTPRequestHandler):

  def do_GET(self):
      count = r.get('counter')
      self.resp('{"count": ' + str(count) + ' }')

  def do_PUT(self):
      count = r.incr('counter')
      self.resp('{"count": ' + str(count) + ' }')

  def resp(self, msg):
      self.send_response(200)
      self.send_header('Content-type', 'application/json')
      self.end_headers()
      self.wfile.write(bytes(msg, 'UTF-8'))

if __name__ == '__main__':
    from http.server import HTTPServer
    server = HTTPServer(('0.0.0.0', 8080), Server)
    print('Starting server @ 8080, use <Ctrl-C> to stop')
    server.serve_forever()
