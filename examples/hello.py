from lighthouse import Lighthouse
from flup.server.fcgi import WSGIServer

def home():
    return "Hello, world"

urls = (
    ('/', home),
)

WSGIServer(Lighthouse(urls)).run()

