from http.server import BaseHTTPRequestHandler, HTTPServer
import redis
import os
import grpc

import counter_pb2
import counter_pb2_grpc


class Server(BaseHTTPRequestHandler):

    def __init__(self, *args, **kwargs):
        self.name = 'counter'
        if os.environ['HTTP_BACKEND'] == 'GRPC':
            self.backend = 'grpc'
        else:
            self.backend = 'redis'

        if self.backend == 'redis':
            self.r = redis.Redis(host='localhost', port=6379,
                                 db=0, decode_responses=True)
        elif self.backend == 'grpc':
            self.g = counter_pb2_grpc.CounterStub(
                grpc.insecure_channel('localhost:50051'))
        super().__init__(*args, **kwargs)

    def get(self):
        if self.backend == 'redis':
            return self.r.get('counter')
        else:
            header_metadata = tuple([(k.lower(), v)
                                     for k, v in self.headers.items()
                                     if k.startswith('x-')])
            response, call = self.g.get.with_call(
                counter_pb2.CounterRequest(name='counter'),
                metadata=header_metadata)
            return response.count

    def incr(self):
        if self.backend == 'redis':
            return self.r.incr('counter')
        else:
            header_metadata = tuple([(k.lower(), v)
                                     for k, v in self.headers.items()
                                     if k.startswith('x-')])
            response, call = self.g.incr.with_call(
                counter_pb2.CounterRequest(name='counter'),
                metadata=header_metadata)
            return response.count

    def do_GET(self):
        print(self.headers)
        count = self.get()
        self.resp(f'{{ "count": "{count}" }}')

    def do_PUT(self):
        print(self.headers)
        count = self.incr()
        self.resp(f'{{ "count": "{count}" }}')

    def resp(self, msg):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(bytes(msg, 'UTF-8'))


if __name__ == '__main__':
    server = HTTPServer(('0.0.0.0', 80), Server)
    print('Starting server @ 80, use <Ctrl-C> to stop')
    server.serve_forever()
