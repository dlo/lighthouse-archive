#!/usr/bin/env python

import sys
sys.path.append("..")

from lighthouse import Lighthouse
from flup.server.fcgi import WSGIServer

def home():
    return "Hello, world"

def regex(*a):
    return str(a)

urls = (
    ('/', home),
    ('/(.+)', regex),
)

WSGIServer(Lighthouse(urls)).run()

