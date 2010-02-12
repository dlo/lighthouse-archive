#!/usr/bin/env python

import re

class Response():
    def __init__(self):
        self.status = 200
        self.msg = "OK"
        self.headers = {"Content-type": "text/html"}
        self.content = ""

    def make_headers(self):
        return list(self.headers.items())

    def __str__(self):
        return "%d %s" % (self.status, self.msg)

class Lighthouse():
    def __init__(self, urls = None):
        self.urls = urls

    def __call__(self, environ, start_response):
        response = Response()
        path = environ['PATH_INFO']
        for url, f in self.urls:
            r = re.compile(url)
            m = r.match(path)
            if m:
                response.content = f(*m.groups())

        start_response(str(response), response.make_headers())
        return [response.content]

