# -------------------------------------------------------------
#  Copyright (c) 2022 Red Hat, Inc. All rights reserved.
#  Licensed under the MIT License. See LICENSE in project root.
# -------------------------------------------------------------
# This program prints Hello, world!
from http.server import BaseHTTPRequestHandler, HTTPServer
import os
import socket

class DemoHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        hostname = socket.gethostname()
        user = os.getenv('USER', 'developer')

        html = f"""
        <html>
        <head>
            <title>Dev Spaces Demo</title>
            <style>
                body {{ font-family: Arial, sans-serif; margin: 40px; }}
                h1 {{ color: #0066cc; }}
                .info {{ background: #f0f0f0; padding: 20px; border-radius: 5px; }}
            </style>
        </head>
        <body>
            <h1>Hello from OpenShift Dev Spaces!</h1>
            <div class="info">
                <p><strong>This code was written in a cloud-based IDE</strong></p>
                <p>Running on server: {hostname}</p>
                <p>Developer: {user}</p>
                <p>Platform: OpenShift Dev Spaces</p>
            </div>
        </body>
        </html>
        """

        self.wfile.write(html.encode())

if __name__ == '__main__':
    server = HTTPServer(('0.0.0.0', 8080), DemoHandler)
    print('Server running on http://0.0.0.0:8080')
    print('Press Ctrl+C to stop')
    server.serve_forever()
