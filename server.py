from time import sleep
import grpc
from concurrent import futures
import hello_pb2
import hello_pb2_grpc


class HelloServicer(hello_pb2_grpc.HelloServicer):

    def World(self, request, context):
        sleep(2)
        return hello_pb2.Welcome(
            output=f"Hello {request.first} {request.last}. I'm World!"
        )

    def Person(self, request_iterator, context):
        number = 1
        for i in request_iterator:
            sleep(2 * number)
            yield hello_pb2.Welcome(output=f"Hello {i.first} {i.last}.")
            number += 1


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    hello_pb2_grpc.add_HelloServicer_to_server(HelloServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Running a grpc hello service on localhost:50051")
    while True:
        sleep(10)


if __name__ == '__main__':
    serve()
