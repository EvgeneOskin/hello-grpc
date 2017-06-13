# Hello gRPC

This is a hello-world like project for [gRPC](http://www.grpc.io) on python.

## Features

It provides 2 endpoints:

- `World`: it accepts a single `(first, last)` pair and returns a welcome
  string.
- `Person`: it accepts a stream/iterator of `(first, last)` pairs and
  returns welcome strings.

## Requirements

The project use Python 3.

```bash
$ make install
# pip3 install -r requirements.txt
# ...
```

## Build Stub and Servicer

```bash
$ make build
# python3 -m grpc_tools.protoc \
#                 -Iprotos --python_out=. \
#                 --grpc_python_out=. protos/hello.proto
# Updates hello_pb2.py and hello_pb2_grpc.py
```

## Run server

```bash
$ python3 server.py
# Running a grpc hello service on localhost:50051
```

## Run dummy-client

```bash
$ python3 client.py
# Hello Eugene Oskin. I'm World!
# Hello Gabriel Márquez.
# Hello Martin Fowler.
```
