FROM python:2.7.12-slim

RUN mkdir /opt/fake_server

COPY /fake_server/fake_server.* /opt/fake_server/

EXPOSE 8001

WORKDIR /opt/fake_server/

ENTRYPOINT ["python", "fake_server.py", "&"]
CMD ["/bin/bash"]

