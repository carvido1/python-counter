#!/usr/bin/env python3

import http.server
import os

counter = int(os.getenv("PYTHON_COUNTER_START", 999))

class handler(http.server.BaseHTTPRequestHandler):
    def do_GET(s):
        global counter
        s.send_response(200)
        s.send_header('Content-type', 'text/html')
        s.end_headers()
        s.wfile.write(b'%d\n' % counter)
        counter += 1


server = http.server.HTTPServer(('', 8080), handler)
server.serve_forever()