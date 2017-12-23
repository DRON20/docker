FROM python:2.7.12-slim

RUN mkdir /opt/fake_server2

COPY /fake_server2/fake_server.* /opt/fake_server2/

EXPOSE 8002

WORKDIR /opt/fake_server2/
ENTRYPOINT ["python", "fake_server.py"]


CMD ["/bin/bash"]
