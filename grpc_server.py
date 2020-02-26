from concurrent import futures
import grpc

import counter_pb2
import counter_pb2_grpc

import redis

r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)


class Counter(counter_pb2_grpc.CounterServicer):

    def incr(self, request, context):
        for key, value in context.invocation_metadata():
            print('Received initial metadata: key=%s value=%s' % (key, value))
        return counter_pb2.CounterReply(count=str(r.incr(request.name)))

    def get(self, request, context):
        for key, value in context.invocation_metadata():
            print('Received initial metadata: key=%s value=%s' % (key, value))
        return counter_pb2.CounterReply(count=str(r.get(request.name)))


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    counter_pb2_grpc.add_CounterServicer_to_server(Counter(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    print('Starting gRPC Server @ 50051, use <Ctrl-C> to stop')
    serve()
