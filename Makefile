.PHONY: build
build:
	python3 -m grpc_tools.protoc \
		-Iprotos --python_out=. \
		--grpc_python_out=. protos/hello.proto
