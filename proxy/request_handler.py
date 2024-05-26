from http.server import BaseHTTPRequestHandler
from .utils import forward_request, setup_logging

logger = setup_logging()

class RequestHandler(BaseHTTPRequestHandler):
    def _forward(self):
        target_url = f"{self.server.target}{self.path}"
        headers = {key: self.headers[key] for key in self.headers.keys()}

        content_length = self.headers.get("Content-Length")
        if(content_length):
            post_data = self.rfile.read(int(content_length))
        else:
            post_data = None

        response = forward_request(self.command, target_url, headers, post_data)

        if(response):
            self.send_response(response.status_code)
            for key, value in response.headers.items():
                self.send_header(key, value)
            self.end_headers()
            self.wfile.write(response.content)
        else:
            self.send_response(502)
            self.end_headers()
            self.wfile.write(b"Bad Gateway")
    
    def do_GET(self):
        self._forward()

    def do_POST(self):
        self._forward()

    def do_PUT(self):
        self._forward()

    def do_DELETE(self):
        self._forward()

    def do_HEAD(self):
        self._forward()

    def do_OPTIONS(self):
        self._forward()

    def do_PATCH(self):
        self._forward()