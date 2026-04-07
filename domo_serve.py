import http.server, sys, os, socketserver

port = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
# Use script's own directory as the serve root if no dir given
# (launch.json will set working dir to project folder)
directory = os.path.dirname(os.path.abspath(__file__))

# Override with arg if provided (rejoin in case of space-splits)  
if len(sys.argv) > 2:
    directory = ' '.join(sys.argv[2:])

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=directory, **kwargs)
    def log_message(self, format, *args):
        sys.stdout.write(format % args + '\n')
        sys.stdout.flush()

class ReusableTCPServer(socketserver.TCPServer):
    allow_reuse_address = True

print(f'Serving {directory!r} on port {port}', flush=True)
httpd = ReusableTCPServer(('', port), Handler)
httpd.serve_forever()
