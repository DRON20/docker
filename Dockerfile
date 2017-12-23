FROM python2.7

COPY /home/atiunov/workspace/fake_server /opt
COPY /home/atiunov/workspace/fake2_server /opt

EXPOSE 8001

RUN cd /opt/fake_server/
    python fake_server.py &
    cd ../fake2_server/
    python fake_server.py &
