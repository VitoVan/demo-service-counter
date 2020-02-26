if [[ "$SERVER_TYPE" == "GRPC" ]]; then
    python grpc_server.py
elif  [[ "$SERVER_TYPE" == "HTTP" ]]; then
    if [[ "$HTTP_BACKEND" == "GRPC" ]]; then
        HTTP_BACKEND=GRPC python http_server.py
    else
        HTTP_BACKEND=REDIS python http_server.py
    fi
else
    HTTP_BACKEND=REDIS python http_server.py
fi
