#!/usr/bin/python
# Send https request:
#   curl -s --cacert ~/workdir/test/k8s/certs/ca.crt --resolve lingxian.example.com:443:127.0.0.1 https://lingxian.example.com:443
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
import os
import socket
import ssl
import time

LOCAL_IP = None

def get_ip():
    global LOCAL_IP
    if LOCAL_IP is None:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            # doesn't even have to be reachable
            s.connect(('10.255.255.255', 1))
            LOCAL_IP = s.getsockname()[0]
        except:
            LOCAL_IP = '127.0.0.1'
        finally:
            s.close()
    return LOCAL_IP

class myHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        res_content = "Hello %s:%s, I'm %s - %s\n" % (self.client_address[0], self.client_address[1], get_ip(), time.strftime("%H:%M:%S", time.gmtime()))
        self.wfile.write(res_content)
        return

try:
    port = int(os.environ.get('PORT_NUMBER', 8080))
    server = HTTPServer(('', port), myHandler)
    if port == 443:
        cert_dir = os.environ.get('CERT_DIR', "/var/lib/ssl")
        server.socket = ssl.wrap_socket(server.socket, certfile='%s/ca.crt' % cert_dir, keyfile='%s/ca.key' % cert_dir, server_side=True, ssl_version=ssl.PROTOCOL_TLSv1_2)
    print('Started httpserver on port %s' % port)
    server.serve_forever()
except KeyboardInterrupt:
    print 'shutting down the web server...'
    server.socket.close()
