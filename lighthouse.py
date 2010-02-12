#!/usr/bin/env python

import re
from flup.server.fcgi import WSGIServer

class Response():
    def __init__(self):
        self._status = 200
        self._msg = "OK"
        self._headers = {"Content-type": "text/html"}
        self.content = ""

    def make_headers(self):
        return list(self._headers.items())

    def __str__(self):
        return "%d %s" % (self._status, self._msg)

class Lighthouse():
    def __init__(self, urls = None):
        self.urls = dict(urls)

    def __call__(self, environ, start_response):
        response = Response()
        path = environ['PATH_INFO']
        for url, f in self.urls.iteritems():
            r = re.compile(url)
            m = r.match(path)
            if m:
                response.content = f(*m.groups())

        start_response(str(response), response.make_headers())
        return [response.content]

def home():
    return "Hello, world"

urls = (
    ('/', home),
)

WSGIServer(Lighthouse(urls)).run()

