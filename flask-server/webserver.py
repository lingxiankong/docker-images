#!/usr/bin/python
# python3.7 -m pip install Flask
# Run webserver:
#   export FLASK_APP=hello.py
#   flask run --host=0.0.0.0 --port 8080

from flask import Flask
import socket

app = Flask(__name__)
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

@app.route("/")
def hello():
    return f"Hello, I'm {get_ip()}"

@app.route("/ping")
def ping():
    return f"Pong, I'm {get_ip()}"
