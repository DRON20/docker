#!/usr/bin/python
# -*- coding: utf-8 -*-
#from __future__ import unicode_literals

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import time
import os
import logging
import cgi
import ConfigParser

serviceIni = "fake_server.ini"
serviceLog = "fake_server.log"

# Чтение из  ini файла
def getConfig ():
	parser = ConfigParser.ConfigParser()
	if (os.path.exists(serviceIni)):
		parser.read(serviceIni)
	else:
		print(serviceIni + " don`t exists")
		sys.exit()
	config = {}
	options = parser.options('default')
	for option in xrange(len(options)):
		config[option] = parser.get('default', options[option])
	return config

config = getConfig()
robinCount = 0
hashCount = 0

logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s', filename=serviceLog, level=logging.DEBUG)
logging.getLogger().addHandler(logging.StreamHandler())


class HttpProcessor(BaseHTTPRequestHandler):

    def do_POST(self):
        print self.requestline.split(" ")[1]
        if self.headers.gettype() == "text/plain":

            t1 = time.time()
            # 1
            sendResult(self, "('fake_class', fake_probability)")

            logging.debug('All do_post = %s', str(time.time() - t1))
        else:
            self.send_response(415)

    def do_GET(self):
        global robinCount, hashCount
        if self.requestline.split(" ")[1] == "/round-robin":
            self.send_response(200)
            robinCount += 1
        if self.requestline.split(" ")[1] == "/round-robin/stat":
            self.send_response(200)
            self.wfile.write(robinCount)
        if self.requestline.split(" ")[1] == "/hash":
            self.send_response(200)
            hashCount += 1
        if self.requestline.split(" ")[1] == "/hash/stat":
            self.send_response(200)
            self.wfile.write(hashCount)
        if self.requestline.split(" ")[1] == "/query":
	    time.sleep(0.1)
            self.send_response(200)
        if self.requestline.split(" ")[1] == "/stop":
            sys.exit()


def sendResult(self, resultStr):
    self.send_response(200)
    self.send_header("Content-Type", 'text/plain; charset=iso-8859-1')    
    count = len(resultStr)
    self.send_header("Content-Length", str(count))
    self.end_headers()
    self.wfile.write(resultStr)
    self.wfile.write('\n')




def init(port):
    global net

    logging.info('port = %s', port)

    logging.info('=========Starting server=========')
    serv = HTTPServer(("0.0.0.0", port), HttpProcessor)
    serv.serve_forever()

def main(argv):
    cur = os.getcwd()
    port = int(config[3])

    init(port)


if __name__ == "__main__":
    main(sys.argv)
