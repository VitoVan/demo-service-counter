FROM python:3
RUN pip install redis
COPY server.py .
ENTRYPOINT ["python", "server.py"]
