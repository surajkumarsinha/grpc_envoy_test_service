proto:
	protoc --proto_path=protos --go_out=pb --go-grpc_out=. --go_opt=paths=source_relative \
	--grpc-gateway_out ./pb \
	--grpc-gateway_opt logtostderr=true \
	--grpc-gateway_opt paths=source_relative \
	--grpc-gateway_opt generate_unbound_methods=true \
	protos/*.proto
	# --openapiv2_out . \
	# --openapiv2_opt logtostderr=true \
	# --openapiv2_opt generate_unbound_methods=true \


py:
	python3 data_service_server.py 

grpc:
	go run gateway/main.go 

client:
	python3 data_service_client.py

