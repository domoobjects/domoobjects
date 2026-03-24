import http.server, os, sys
os.chdir(os.path.dirname(os.path.abspath(__file__)))
port = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
httpd = http.server.HTTPServer(('', port), http.server.SimpleHTTPRequestHandler)
print(f'Serving on http://localhost:{port}')
httpd.serve_forever()
