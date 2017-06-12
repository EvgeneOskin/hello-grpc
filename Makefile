.PHONY: build
build:
	python3 -m grpc_tools.protoc \
		-Iprotos --python_out=. \
		--grpc_python_out=. protos/hello.proto

.PHONY: install
install:
	pip3 install -r requirements.txt
