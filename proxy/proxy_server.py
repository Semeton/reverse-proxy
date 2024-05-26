from http.server import HTTPServer
from .config import Config
from .request_handler import RequestHandler, logger

class ProxyServer:
    def __init__(self, config_file='config.json'):
        self.config = Config(config_file)
        self.host = self.config.get('host', '0.0.0.0')
        self.port = self.config.get('port', 8080)
        self.target = self.config.get('target')

        if not self.target:
            raise Exception("Target server not specified in the config file.")

    def run(self):
        server_address = (self.host, self.port)
        httpd = HTTPServer(server_address, RequestHandler)
        httpd.target = self.target
        logger.info(f"Starting proxy server on {self.host}:{self.port} forwarding to {self.target}")
        httpd.serve_forever()
