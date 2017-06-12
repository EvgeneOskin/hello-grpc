import grpc
import hello_pb2
from hello_pb2_grpc import HelloStub


channel = grpc.insecure_channel('localhost:50051')
stub = HelloStub(channel)

welcome = stub.World(hello_pb2.Name(first='Eugene', last='Oskin'))
print(welcome.output)


def names():
    yield hello_pb2.Name(first='Gabriel', last='Márquez')
    yield hello_pb2.Name(first='Martin', last='Fowler')


persons = stub.Person(names())
for i in persons:
    print(i.output)
