from searcher import cbot_query
import socketserver
import http.server

PORT = 5000
DIRECTORY ='UI'

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def do_POST(self):
        self.send_response(200)
        content_length = int(self.headers['content-Length'])
        post_body = self.rfile.read(content_length)
        self.end_headers()
        print('user query', post_body)
        google_search_chatbot_reply = cbot_query(post_body)
        self.wfile.write(str.encode(google_search_chatbot_reply))
        
with socketserver.TCPServer(('', PORT), Handler) as httpd:
    print('serving at port', PORT)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()

