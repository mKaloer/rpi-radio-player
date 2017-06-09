python -m grpc_tools.protoc -I protos --python_out=api-server/api-server --grpc_python_out=api-server/api-server protos/radiomessages.proto
python -m grpc_tools.protoc -I protos --python_out=web-radio/web-radio --grpc_python_out=web-radio/web-radio protos/radiomessages.proto
docker-compose build
