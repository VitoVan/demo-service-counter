FROM python:3
RUN pip install redis grpcio protobuf -i https://pypi.doubanio.com/simple/
COPY ./ ./
ENTRYPOINT ["bash", "start.sh"]
