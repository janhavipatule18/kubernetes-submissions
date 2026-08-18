from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.request import urlopen

PINGPONG_URL = "http://ping-pong-svc:8080/pingpong"


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            try:
                with urlopen(PINGPONG_URL) as response:
                    pingpong = response.read().decode().strip()
            except Exception as e:
                pingpong = f"Error: {e}"

            response = f"Ping / Pongs: {pingpong}\n"

            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(response.encode())
        else:
            self.send_response(404)
            self.end_headers()

    def log_message(self, format, *args):
        return


server = HTTPServer(("0.0.0.0", 8080), Handler)
print("Reader server started in port 8080", flush=True)
server.serve_forever()
